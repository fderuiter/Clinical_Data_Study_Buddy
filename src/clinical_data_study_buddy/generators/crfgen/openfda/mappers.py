"""
This module provides functions for mapping and enriching data from different
OpenFDA endpoints. These functions are used to create a more complete and
integrated view of the data.
"""
from typing import List, Optional
import hashlib
import json

from .models import MAUDEEvent, UDI, Classification, Recall

def crosswalk_events_to_udi(events: List[MAUDEEvent], udis: List[UDI]) -> List[dict]:
    """
    Crosswalks MAUDE events to UDI records based on the UDI-DI.

    This function joins MAUDE event records with UDI records on the `udi_di`
    key, creating a new record that includes both event and UDI information,
    as well as provenance data.

    Args:
        events (List[MAUDEEvent]): A list of MAUDEEvent records.
        udis (List[UDI]): A list of UDI records.

    Returns:
        List[dict]: A list of dictionaries, where each dictionary represents
                    a joined record containing event and UDI data.
    """
    results = []
    udi_map = {udi.di: udi for udi in udis}

    for event in events:
        for device in event.device:
            if device.udi_di and device.udi_di in udi_map:
                udi = udi_map[device.udi_di]
                joined_record = {
                    "event": event.dict(),
                    "udi": udi.dict(),
                    "provenance": {
                        "source": "openfda",
                        "endpoints": ["/device/event.json", "/device/udi.json"],
                        "join_key": "udi_di",
                        "hash": hashlib.sha256(json.dumps([event.dict(), udi.dict()], sort_keys=True).encode()).hexdigest()
                    }
                }
                results.append(joined_record)
    return results

def enrich_with_classification(records: List[dict], classifications: List[Classification]) -> List[dict]:
    """
    Enriches a list of records with device classification information.

    This function joins records (e.g., from a crosswalk) with classification
    records based on the product code.

    Args:
        records (List[dict]): A list of records to be enriched.
        classifications (List[Classification]): A list of Classification records.

    Returns:
        List[dict]: The enriched list of records, with classification
                    information added where a match was found.
    """
    classification_map = {c.product_code: c for c in classifications}

    for record in records:
        product_code = None
        if "recall" in record and record["recall"].product_code:
            product_code = record["recall"].product_code
        elif "event" in record:
            for device in record["event"]["device"]:
                if "product_code" in device and device["product_code"]:
                    product_code = device["product_code"]
                    break

        if product_code and product_code in classification_map:
            record["classification"] = classification_map[product_code].dict()
            if "provenance" in record:
                record["provenance"]["endpoints"].append("/device/classification.json")

    return records
