"""
This module provides access to the OpenFDA MAUDE (device event) endpoint.
"""

from typing import List, Optional

from ..client import OpenFDAClient
from ..models import MAUDEEvent
from ..query import paging_query


class MAUDEAccessor:
    """
    Provides access to the openFDA MAUDE (event) endpoint.

    This class is responsible for fetching and counting MAUDE adverse event
    records from the OpenFDA API.
    """

    def __init__(self, client: OpenFDAClient):
        """
        Initializes the MAUDEAccessor.

        Args:
            client (OpenFDAClient): An instance of the OpenFDA client.
        """
        self.client = client

    async def fetch(
        self,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> List[MAUDEEvent]:
        """
        Fetches MAUDE event records from the openFDA API.

        Args:
            search (Optional[str]): A search query string to filter the results.
            limit (Optional[int]): The maximum number of results to return.
            skip (Optional[int]): The number of results to skip for pagination.

        Returns:
            List[MAUDEEvent]: A list of MAUDEEvent records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/event.json", params=params)
        results = (await response.json()).get("results", [])
        return [MAUDEEvent(**item) for item in results]

    async def count(self, field: str) -> dict:
        """
        Counts MAUDE event records by a given field.

        Args:
            field (str): The field to count on.

        Returns:
            dict: A dictionary containing the count results.
        """
        params = {"count": field}
        response = await self.client.get("/device/event.json", params=params)
        return response.json()
