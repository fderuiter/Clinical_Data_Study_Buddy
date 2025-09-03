"""
This module provides access to the OpenFDA device enforcement endpoint.
"""
from typing import List, Optional

from ..client import OpenFDAClient
from ..models import EnforcementReport
from ..query import paging_query

class EnforcementAccessor:
    """
    Provides access to the openFDA device enforcement endpoint.

    This class is responsible for fetching and counting device enforcement reports
    from the OpenFDA API.
    """

    def __init__(self, client: OpenFDAClient):
        """
        Initializes the EnforcementAccessor.

        Args:
            client (OpenFDAClient): An instance of the OpenFDA client.
        """
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[EnforcementReport]:
        """
        Fetches device enforcement reports from the openFDA API.

        Args:
            search (Optional[str]): A search query string to filter the results.
            limit (Optional[int]): The maximum number of results to return.
            skip (Optional[int]): The number of results to skip for pagination.

        Returns:
            List[EnforcementReport]: A list of EnforcementReport records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/enforcement.json", params=params)
        results = response.json().get("results", [])
        return [EnforcementReport(**item) for item in results]

    async def count(self, field: str) -> dict:
        """
        Counts enforcement reports by a given field.

        Args:
            field (str): The field to count on.

        Returns:
            dict: A dictionary containing the count results.
        """
        params = {"count": field}
        response = await self.client.get("/device/enforcement.json", params=params)
        return response.json()
