from typing import List, Optional

from ..client import OpenFDAClient
from ..models import UDI
from ..query import term_query, paging_query

class UDIAccessor:
    """
    Provides access to the openFDA UDI endpoint.
    """

    def __init__(self, client: OpenFDAClient):
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[UDI]:
        """
        Fetches UDI records from the openFDA API.

        Args:
            search: The search query string.
            limit: The number of results to return.
            skip: The number of results to skip.

        Returns:
            A list of UDI records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/udi.json", params=params)
        results = (await response.json()).get("results", [])
        return [UDI(**item) for item in results]

    async def get_by_di(self, di: str) -> Optional[UDI]:
        """
        Fetches a UDI record by its DI.

        Args:
            di: The Device Identifier (DI) of the UDI record.

        Returns:
            The UDI record, or None if not found.
        """
        search_query = term_query("di", di)
        results = await self.fetch(search=search_query, limit=1)
        return results[0] if results else None
