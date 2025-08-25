from typing import List, Optional

from ..client import OpenFDAClient
from ..models import Registration
from ..query import paging_query

class RegListAccessor:
    """
    Provides access to the openFDA registration and listing endpoint.
    """

    def __init__(self, client: OpenFDAClient):
        self.client = client

    async def fetch(self, search: Optional[str] = None, limit: Optional[int] = None, skip: Optional[int] = None) -> List[Registration]:
        """
        Fetches registration and listing records from the openFDA API.

        Args:
            search: The search query string.
            limit: The number of results to return.
            skip: The number of results to skip.

        Returns:
            A list of Registration records.
        """
        params = paging_query(limit, skip)
        if search:
            params["search"] = search

        response = await self.client.get("/device/registrationlisting.json", params=params)
        results = (await response.json()).get("results", [])
        return [Registration(**item) for item in results]
