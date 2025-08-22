from typing import List, Optional

from ..client import OpenFDAClient
from ..models import Recall
from ..query import paging_query

class RecallAccessor:
    """
    Provides access to the openFDA device recall endpoint.
    """

    def __init__(self, client: OpenFDAClient):
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[Recall]:
        """
        Fetches device recall records from the openFDA API.

        Args:
            search: The search query string.
            limit: The number of results to return.
            skip: The number of results to skip.

        Returns:
            A list of Recall records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/recall.json", params=params)
        results = (await response.json()).get("results", [])
        return [Recall(**item) for item in results]
