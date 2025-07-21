import json
import pathlib

from crfgen import crawl

FIXTURE = json.loads((pathlib.Path(__file__).parent / "fixtures" / "crawl_fixture.json").read_text())


def fake_cached_get(url: str, headers: dict[str, str], ttl_days: int = 30):
    return FIXTURE[url]


def test_harvest_offline(monkeypatch):
    monkeypatch.setattr(crawl, "cached_get", fake_cached_get)
    forms = crawl.harvest("dummy", ig_filter="2-2")
    assert len(forms) == 2
    assert forms[0].domain == "VS"
    assert forms[1].scenario == "VS.Generic"
