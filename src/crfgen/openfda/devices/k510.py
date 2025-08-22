from typing import List, Optional

from ..client import OpenFDAClient
from ..models import K510
from ..query import paging_query

class K510Accessor:
    """
    Provides access to the openFDA 510(k) endpoint.
    """

    def __init__(self, client: OpenFDAClient):
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[K510]:
        """
        Fetches 510(k) records from the openFDA API.

        Args:
            search: The search query string.
            limit: The number of results to return.
            skip: The number of results to skip.

        Returns:
            A list of K510 records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/510k.json", params=params)
        results = (await response.json()).get("results", [])
        return [K510(**item) for item in results]
