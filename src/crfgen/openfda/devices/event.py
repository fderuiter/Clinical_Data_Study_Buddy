from typing import List, Optional

from ..client import OpenFDAClient
from ..models import MAUDEEvent
from ..query import paging_query

class MAUDEAccessor:
    """
    Provides access to the openFDA MAUDE (event) endpoint.
    """

    def __init__(self, client: OpenFDAClient):
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[MAUDEEvent]:
        """
        Fetches MAUDE event records from the openFDA API.

        Args:
            search: The search query string.
            limit: The number of results to return.
            skip: The number of results to skip.

        Returns:
            A list of MAUDEEvent records.
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
            field: The field to count.

        Returns:
            A dictionary of count results.
        """
        params = {"count": field}
        response = await self.client.get("/device/event.json", params=params)
        return response.json()
