from typing import List, Optional

from ..client import OpenFDAClient
from ..models import EnforcementReport
from ..query import paging_query

class EnforcementAccessor:
    """
    Provides access to the openFDA device enforcement endpoint.
    """

    def __init__(self, client: OpenFDAClient):
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[EnforcementReport]:
        """
        Fetches device enforcement reports from the openFDA API.

        Args:
            search: The search query string.
            limit: The number of results to return.
            skip: The number of results to skip.

        Returns:
            A list of EnforcementReport records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/enforcement.json", params=params)
        results = (await response.json()).get("results", [])
        return [EnforcementReport(**item) for item in results]

    async def count(self, field: str) -> dict:
        """
        Counts enforcement reports by a given field.

        Args:
            field: The field to count.

        Returns:
            A dictionary of count results.
        """
        params = {"count": field}
        response = await self.client.get("/device/enforcement.json", params=params)
        return response.json()
