import logging
from typing import List, Dict, Any
from cdisc_data_symphony.api.openfda import client

logger = logging.getLogger(__name__)

def populate_ae_from_fda(
    drug_name: str, max_results: int = 10, start_date: str = None, end_date: str = None
) -> List[Dict[str, Any]]:
    """
    Fetches Adverse Event data from openFDA and formats it.
    """
    logger.info(f"Fetching adverse events for drug: {drug_name} with max_results: {max_results}")
    adverse_events = client.get_adverse_events(
        drug_name, max_results=max_results, start_date=start_date, end_date=end_date
    )
    if not adverse_events:
        logger.warning(f"No adverse events found for '{drug_name}' with the given criteria.")
        return []

    # Extract reaction terms
    results = []
    for event in adverse_events:
        reactions = event.get("patient", {}).get("reaction", [])
        for reaction in reactions:
            term = reaction.get("reactionmeddrapt")
            if term:
                results.append({"reaction_term": term})

    logger.info(f"Found {len(results)} adverse event reaction terms for {drug_name}.")
    return results


def populate_label_from_fda(drug_name: str) -> Dict[str, Any]:
    """
    Fetches Drug Label data from openFDA and formats it.
    """
    logger.info(f"Fetching drug label for: {drug_name}")
    label_data = client.get_drug_label(drug_name)
    if not label_data:
        logger.warning(f"No drug label found for '{drug_name}'.")
        return {}

    # Extract key information
    result = {
        "brand_name": label_data.get("openfda", {}).get("brand_name", []),
        "generic_name": label_data.get("openfda", {}).get("generic_name", []),
        "indications_and_usage": label_data.get("indications_and_usage", []),
        "adverse_reactions": label_data.get("adverse_reactions", []),
    }
    logger.info(f"Successfully extracted label information for {drug_name}.")
    return result
