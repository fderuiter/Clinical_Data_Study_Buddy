from __future__ import annotations
from typing import Callable, Dict, List
from pathlib import Path

from ..schema import Form

EXPORTERS: Dict[str, Callable[[List[Form], Path], None]] = {}


def register(name: str) -> Callable[[Callable[[List[Form], Path], None]], Callable[[List[Form], Path], None]]:
    """Decorator to register an exporter function."""

    def decorator(func: Callable[[List[Form], Path], None]) -> Callable[[List[Form], Path], None]:
        EXPORTERS[name] = func
        return func

    return decorator
