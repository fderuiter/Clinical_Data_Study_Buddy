"""
This module provides access to the OpenFDA device registration and listing endpoint.
"""
from typing import List, Optional

from ..client import OpenFDAClient
from ..models import Registration
from ..query import paging_query

class RegListAccessor:
    """
    Provides access to the openFDA registration and listing endpoint.

    This class is responsible for fetching device registration and listing records
    from the OpenFDA API.
    """

    def __init__(self, client: OpenFDAClient):
        """
        Initializes the RegListAccessor.

        Args:
            client (OpenFDAClient): An instance of the OpenFDA client.
        """
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[Registration]:
        """
        Fetches registration and listing records from the openFDA API.

        Args:
            search (Optional[str]): A search query string to filter the results.
            limit (Optional[int]): The maximum number of results to return.
            skip (Optional[int]): The number of results to skip for pagination.

        Returns:
            List[Registration]: A list of Registration records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/registrationlisting.json", params=params)
        results = (await response.json()).get("results", [])
        return [Registration(**item) for item in results]
