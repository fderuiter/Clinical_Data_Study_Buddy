"""
This module provides a simple client for searching studies on ClinicalTrials.gov
using their V2 API.
"""

import requests

URL = "https://clinicaltrials.gov/api/v2/studies"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def search_studies(query: str):
    """
    Searches for studies on ClinicalTrials.gov using the provided query.

    Args:
        query (str): The search query term.

    Returns:
        dict: A dictionary containing the JSON response from the API.

    Raises:
        requests.exceptions.HTTPError: If the API request fails.
    """
    params = {"query.term": query}
    response = requests.get(URL, params=params, headers=HEADERS)
    response.raise_for_status()
    return response.json()
