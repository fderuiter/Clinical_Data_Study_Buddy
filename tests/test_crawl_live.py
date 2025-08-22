import pytest

from crfgen.auth import get_api_key
from crfgen.crawl import harvest

try:
    token = get_api_key()
    skip_test = False
except ValueError as e:
    token = None
    skip_test = True
    reason = str(e)


@pytest.mark.skipif(skip_test, reason=reason)
def test_live_pull_small():
    forms = harvest(token, ig_filter="2-2")
    assert len(forms) >= 40  # CDASH 2.2 domains
