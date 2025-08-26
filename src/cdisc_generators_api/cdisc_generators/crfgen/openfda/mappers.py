from typing import List, Optional
import hashlib
import json

from .models import MAUDEEvent, UDI, Classification, Recall

def crosswalk_events_to_udi(events: List[MAUDEEvent], udis: List[UDI]) -> List[dict]:
    """
    Crosswalks MAUDE events to UDI records.

    Args:
        events: A list of MAUDEEvent records.
        udis: A list of UDI records.

    Returns:
        A list of dictionaries, where each dictionary represents a joined record.
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
    Enriches records with classification information.

    Args:
        records: A list of records (e.g., from a join).
        classifications: A list of Classification records.

    Returns:
        The enriched list of records.
    """
    classification_map = {c.product_code: c for c in classifications}

    for record in records:
        product_code = None
        if "recall" in record and record["recall"].product_code:
            product_code = record["recall"].product_code
        elif "event" in record:
            for device in record["event"]["device"]:
                if device["product_code"]:
                    product_code = device["product_code"]
                    break

        if product_code and product_code in classification_map:
            record["classification"] = classification_map[product_code].dict()
            if "provenance" in record:
                record["provenance"]["endpoints"].append("/device/classification.json")

    return records
