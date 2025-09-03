"""
This module provides access to the OpenFDA device classification endpoint.
"""
from typing import List, Optional

from ..client import OpenFDAClient
from ..models import Classification
from ..query import paging_query

class ClassificationAccessor:
    """
    Provides access to the openFDA device classification endpoint.

    This class is responsible for fetching device classification records from the
    OpenFDA API, handling pagination and search queries.
    """

    def __init__(self, client: OpenFDAClient):
        """
        Initializes the ClassificationAccessor.

        Args:
            client (OpenFDAClient): An instance of the OpenFDA client.
        """
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[Classification]:
        """
        Fetches device classification records from the openFDA API.

        Args:
            search (Optional[str]): A search query string to filter the results.
            limit (Optional[int]): The maximum number of results to return.
            skip (Optional[int]): The number of results to skip for pagination.

        Returns:
            List[Classification]: A list of Classification records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/classification.json", params=params)
        results = (await response.json()).get("results", [])
        return [Classification(**item) for item in results]
