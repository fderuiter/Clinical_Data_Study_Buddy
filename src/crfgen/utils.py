from __future__ import annotations

from typing import Any, Mapping


def normalize_headers(headers: Mapping[str, Any]) -> dict[str, str]:
    """Return a new dict with all header values converted to plain strings."""
    return {
        k: (v.decode() if isinstance(v, (bytes, bytearray)) else str(v))
        for k, v in headers.items()
    }
