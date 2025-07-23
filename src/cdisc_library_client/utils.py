from __future__ import annotations

from typing import Any, Mapping


def normalize_headers(headers: Mapping[str, Any]) -> dict[str, str]:
    """Return ``headers`` with values coerced to plain strings.

    Any ``bytes`` or ``bytearray`` values are decoded using the default
    encoding. Other values are converted via ``str()``.
    """
    return {
        k: (v.decode() if isinstance(v, (bytes, bytearray)) else str(v))
        for k, v in headers.items()
    }
