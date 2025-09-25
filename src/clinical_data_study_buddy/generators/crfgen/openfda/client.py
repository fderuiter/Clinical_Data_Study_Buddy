"""
This module provides an asynchronous client for interacting with the OpenFDA API.

It includes features like rate limiting, automatic retries with exponential
backoff, and response caching to ensure efficient and reliable communication
with the API.
"""

import asyncio
import os
from typing import Optional

import httpx
from httpx_cache import AsyncClient, FileCache
from tenacity import retry, stop_after_attempt, wait_exponential


class TokenBucket:
    """
    An implementation of the token bucket algorithm for rate limiting.

    Attributes:
        capacity (float): The total capacity of the bucket.
        fill_rate (float): The rate at which tokens are added to the bucket per second.
    """

    def __init__(self, tokens, fill_rate):
        """
        Initializes the TokenBucket.

        Args:
            tokens (int or float): The initial number of tokens in the bucket.
            fill_rate (int or float): The rate at which tokens are refilled per second.
        """
        self.capacity = float(tokens)
        self._tokens = float(tokens)
        self.fill_rate = float(fill_rate)
        self.timestamp = asyncio.get_event_loop().time()

    async def consume(self, tokens):
        """
        Consumes a specified number of tokens from the bucket.

        If the bucket does not have enough tokens, this method will wait until
        enough tokens are refilled before consuming them.

        Args:
            tokens (int or float): The number of tokens to consume.

        Raises:
            ValueError: If the number of tokens to consume is greater than the
                        bucket's capacity.
        """
        if tokens > self.capacity:
            raise ValueError("Cannot consume more tokens than bucket capacity")

        now = asyncio.get_event_loop().time()
        self._tokens += (now - self.timestamp) * self.fill_rate
        self.timestamp = now

        if self._tokens > self.capacity:
            self._tokens = self.capacity

        if self._tokens < tokens:
            await asyncio.sleep((tokens - self._tokens) / self.fill_rate)

        self._tokens -= tokens


class OpenFDAClient:
    """
    An asynchronous client for interacting with the openFDA API.

    This client includes features such as:
    - Asynchronous requests using httpx.
    - Automatic retries with exponential backoff for handling transient errors.
    - Rate limiting to respect API usage policies.
    - Caching of responses to improve performance and reduce API calls.
    - Authentication using an API key from an environment variable.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.fda.gov",
        rpm: int = 200,
        cache_ttl: Optional[dict] = None,
    ):
        """
        Initializes the OpenFDAClient.

        Args:
            api_key (Optional[str]): The API key for authenticating with the openFDA API.
                                     If not provided, it will be read from the
                                     OPENFDA_API_KEY environment variable.
            base_url (str): The base URL of the openFDA API.
            rpm (int): The maximum number of requests per minute for rate limiting.
            cache_ttl (Optional[dict]): A dictionary mapping endpoints to cache TTLs in seconds.
                                        The default TTL for all endpoints is 1 week.
        """
        self.api_key = api_key or os.getenv("OPENFDA_API_KEY")
        self.base_url = base_url

        self.cache_ttl = cache_ttl or {}

        self.client = AsyncClient(cache=FileCache(".cache/openfda"))
        self.bucket = TokenBucket(rpm, rpm / 60)

    @retry(
        wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(5)
    )
    async def get(self, endpoint: str, params: Optional[dict] = None) -> httpx.Response:
        """
        Performs a GET request to a specified openFDA endpoint.

        Args:
            endpoint (str): The API endpoint to request (e.g., "/drug/event.json").
            params (Optional[dict]): A dictionary of query parameters to include
                                     in the request.

        Returns:
            httpx.Response: The response from the API.

        Raises:
            httpx.HTTPStatusError: If the request fails after all retries.
        """
        await self.bucket.consume(1)

        if params is None:
            params = {}
        if self.api_key:
            params["api_key"] = self.api_key

        url = f"{self.base_url}{endpoint}"

        headers = {}
        ttl = self.cache_ttl.get(endpoint, 604800)  # Default to 1 week
        headers["Cache-Control"] = f"max-age={ttl}"

        # Redact API key for logging
        log_params = params.copy()
        if "api_key" in log_params:
            log_params["api_key"] = "***"
        print(f"Requesting URL: {url} with params: {log_params}")

        response = await self.client.get(url, params=params, headers=headers)

        print(f"Response status code: {response.status_code}")

        await response.raise_for_status()
        return response

    async def close(self):
        """
        Closes the underlying httpx client session.
        """
        await self.client.aclose()
