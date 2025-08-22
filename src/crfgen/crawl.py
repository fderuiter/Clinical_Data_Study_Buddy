from __future__ import annotations

from typing import List

from crfgen.crfgen import CrfGen
from crfgen.schema import Form


def harvest(api_key: str, ig_filter: str | None = None) -> List[Form]:
    """Pull CDASH IG -> domains -> scenarios and convert to Form objects."""
    crfgen = CrfGen(api_key, ig_filter)
    return crfgen.harvest()
