from typing import List, Optional

from ..client import OpenFDAClient
from ..models import Classification
from ..query import paging_query

class ClassificationAccessor:
    """
    Provides access to the openFDA device classification endpoint.
    """

    def __init__(self, client: OpenFDAClient):
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[Classification]:
        """
        Fetches device classification records from the openFDA API.

        Args:
            search: The search query string.
            limit: The number of results to return.
            skip: The number of results to skip.

        Returns:
            A list of Classification records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/classification.json", params=params)
        results = (await response.json()).get("results", [])
        return [Classification(**item) for item in results]
