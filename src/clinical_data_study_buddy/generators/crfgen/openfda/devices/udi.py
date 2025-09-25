"""
This module provides access to the OpenFDA Unique Device Identifier (UDI) endpoint.
"""

from typing import List, Optional

from ..client import OpenFDAClient
from ..models import UDI
from ..query import paging_query, term_query


class UDIAccessor:
    """
    Provides access to the openFDA UDI endpoint.

    This class is responsible for fetching Unique Device Identifier (UDI) records
    from the OpenFDA API.
    """

    def __init__(self, client: OpenFDAClient):
        """
        Initializes the UDIAccessor.

        Args:
            client (OpenFDAClient): An instance of the OpenFDA client.
        """
        self.client = client

    async def fetch(
        self,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> List[UDI]:
        """
        Fetches UDI records from the openFDA API.

        Args:
            search (Optional[str]): A search query string to filter the results.
            limit (Optional[int]): The maximum number of results to return.
            skip (Optional[int]): The number of results to skip for pagination.

        Returns:
            List[UDI]: A list of UDI records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/udi.json", params=params)
        results = (await response.json()).get("results", [])
        return [UDI(**item) for item in results]

    async def get_by_di(self, di: str) -> Optional[UDI]:
        """
        Fetches a UDI record by its Device Identifier (DI).

        Args:
            di (str): The Device Identifier (DI) of the UDI record.

        Returns:
            Optional[UDI]: The UDI record if found, otherwise None.
        """
        search_query = term_query("di", di)
        results = await self.fetch(search=search_query, limit=1)
        return results[0] if results else None
