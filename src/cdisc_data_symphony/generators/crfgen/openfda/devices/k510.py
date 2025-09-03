"""
This module provides access to the OpenFDA 510(k) premarket notification endpoint.
"""
from typing import List, Optional

from ..client import OpenFDAClient
from ..models import K510
from ..query import paging_query

class K510Accessor:
    """
    Provides access to the openFDA 510(k) endpoint.

    This class is responsible for fetching 510(k) premarket notification records
    from the OpenFDA API.
    """

    def __init__(self, client: OpenFDAClient):
        """
        Initializes the K510Accessor.

        Args:
            client (OpenFDAClient): An instance of the OpenFDA client.
        """
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[K510]:
        """
        Fetches 510(k) records from the openFDA API.

        Args:
            search (Optional[str]): A search query string to filter the results.
            limit (Optional[int]): The maximum number of results to return.
            skip (Optional[int]): The number of results to skip for pagination.

        Returns:
            List[K510]: A list of K510 records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/510k.json", params=params)
        results = response.json().get("results", [])
        return [K510(**item) for item in results]
