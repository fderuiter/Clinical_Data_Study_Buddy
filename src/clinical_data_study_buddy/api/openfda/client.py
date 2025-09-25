"""
This module provides a client for interacting with the OpenFDA API.

It includes functions for fetching adverse event and drug label data, with
built-in support for retries with exponential backoff to handle transient
network issues.
"""

import logging
import os
from typing import Any, Dict, List

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

# Logger
logger = logging.getLogger(__name__)

# Configuration
BASE_URL = os.environ.get("OPENFDA_API_URL", "https://api.fda.gov")
REQUEST_TIMEOUT = (10, 30)  # (connect, read)

# Retry configuration
RETRY_WAIT = wait_exponential(multiplier=1, min=4, max=10)
RETRY_STOP = stop_after_attempt(5)
RETRY_ON_EXCEPTION = retry_if_exception_type(requests.exceptions.RequestException)


def log_retry(retry_state):
    """
    Logs a warning message when a retryable API call is attempted.

    Args:
        retry_state: The state of the tenacity retry decorator.
    """
    logger.warning(
        f"Retrying API call for {retry_state.fn.__name__}, attempt {retry_state.attempt_number}..."
    )


@retry(
    wait=RETRY_WAIT, stop=RETRY_STOP, retry=RETRY_ON_EXCEPTION, before_sleep=log_retry
)
def get_adverse_events(
    drug_name: str, max_results: int = 10, start_date: str = None, end_date: str = None
) -> List[Dict[str, Any]]:
    """
    Fetches adverse events for a given drug from the OpenFDA API.

    This function handles pagination and date filtering, and automatically
    retries on failure.

    Args:
        drug_name (str): The name of the drug to search for.
        max_results (int): The maximum number of adverse events to return.
        start_date (str, optional): The start date for the search (YYYY-MM-DD).
        end_date (str, optional): The end date for the search (YYYY-MM-DD).

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, where each dictionary
                              represents an adverse event record.
    """
    all_results = []
    skip = 0
    limit_per_page = 100  # Max limit per request

    search_query = f'patient.drug.medicinalproduct:"{drug_name}"'
    if start_date and end_date:
        search_query += f"+AND+receivedate:[{start_date}+TO+{end_date}]"

    while len(all_results) < max_results:
        results_to_fetch = min(limit_per_page, max_results - len(all_results))
        if results_to_fetch <= 0:
            break

        url = f"{BASE_URL}/drug/event.json"
        params = {"search": search_query, "limit": results_to_fetch, "skip": skip}
        logger.info(f"Querying OpenFDA API: {url} with params: {params}")
        response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        data = response.json()
        results = data.get("results", [])
        if not results:
            break

        all_results.extend(results)

        total_available = data.get("meta", {}).get("results", {}).get("total", 0)
        if len(all_results) >= total_available:
            break

        skip += len(results)

    return all_results


@retry(
    wait=RETRY_WAIT, stop=RETRY_STOP, retry=RETRY_ON_EXCEPTION, before_sleep=log_retry
)
def get_drug_label(drug_name: str) -> Dict[str, Any]:
    """
    Fetches the drug label for a given drug from the OpenFDA API.

    This function searches for the drug by its brand or generic name and
    returns the first matching label.

    Args:
        drug_name (str): The brand or generic name of the drug to search for.

    Returns:
        Dict[str, Any]: A dictionary containing the drug label information,
                        or an empty dictionary if not found.
    """
    url = f"{BASE_URL}/drug/label.json"
    search_query = (
        f'openfda.brand_name:"{drug_name}" OR openfda.generic_name:"{drug_name}"'
    )
    params = {"search": search_query, "limit": 1}
    logger.info(f"Querying OpenFDA API: {url} with params: {params}")
    response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    results = response.json().get("results", [])
    if results:
        return results[0]
    return {}
