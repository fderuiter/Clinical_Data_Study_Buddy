"""
This module provides access to the OpenFDA device recall endpoint.
"""
from typing import List, Optional

from ..client import OpenFDAClient
from ..models import Recall
from ..query import paging_query

class RecallAccessor:
    """
    Provides access to the openFDA device recall endpoint.

    This class is responsible for fetching device recall records from the
    OpenFDA API.
    """

    def __init__(self, client: OpenFDAClient):
        """
        Initializes the RecallAccessor.

        Args:
            client (OpenFDAClient): An instance of the OpenFDA client.
        """
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[Recall]:
        """
        Fetches device recall records from the openFDA API.

        Args:
            search (Optional[str]): A search query string to filter the results.
            limit (Optional[int]): The maximum number of results to return.
            skip (Optional[int]): The number of results to skip for pagination.

        Returns:
            List[Recall]: A list of Recall records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/recall.json", params=params)
        results = (await response.json()).get("results", [])
        return [Recall(**item) for item in results]
