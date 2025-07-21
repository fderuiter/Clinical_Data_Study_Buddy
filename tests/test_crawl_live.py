import os
import pytest

from crfgen.crawl import harvest


@pytest.mark.skipif("CDISC_PRIMARY_KEY" not in os.environ, reason="no token")
def test_crawl_live():
    forms = harvest(os.environ["CDISC_PRIMARY_KEY"], ig_filter="2-2")
    assert len(forms) > 0
    assert all(f.fields for f in forms)
