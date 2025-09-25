"""
This module provides access to the OpenFDA Premarket Approval (PMA) endpoint.
"""

from typing import List, Optional

from ..client import OpenFDAClient
from ..models import PMA
from ..query import paging_query


class PMAAccessor:
    """
    Provides access to the openFDA PMA endpoint.

    This class is responsible for fetching Premarket Approval (PMA) records
    from the OpenFDA API.
    """

    def __init__(self, client: OpenFDAClient):
        """
        Initializes the PMAAccessor.

        Args:
            client (OpenFDAClient): An instance of the OpenFDA client.
        """
        self.client = client

    async def fetch(
        self,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> List[PMA]:
        """
        Fetches PMA records from the openFDA API.

        Args:
            search (Optional[str]): A search query string to filter the results.
            limit (Optional[int]): The maximum number of results to return.
            skip (Optional[int]): The number of results to skip for pagination.

        Returns:
            List[PMA]: A list of PMA records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/pma.json", params=params)
        results = (await response.json()).get("results", [])
        return [PMA(**item) for item in results]
