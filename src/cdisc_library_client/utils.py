from typing import Any, Dict


def normalize_headers(headers: Dict[str, Any]) -> Dict[str, str]:
    """
    Normalize headers to be a dictionary of strings.
    """
    normalized = {}
    for k, v in headers.items():
        if isinstance(v, bytes):
            normalized[k] = v.decode("utf-8")
        elif isinstance(v, bytearray):
            normalized[k] = v.decode("utf-8")
        else:
            normalized[k] = str(v)
    return normalized
