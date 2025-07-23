import os

import pytest

from crfgen.crawl import harvest

token = os.getenv("CDISC_PRIMARY_KEY")


@pytest.mark.skipif(not token, reason="no API key in env")
def test_live_pull_small():
    forms = harvest(token, ig_filter="2-2")
    assert len(forms) >= 40  # CDASH 2.2 domains
