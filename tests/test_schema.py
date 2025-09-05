import json

from cdisc_data_symphony.builder.crfgen.schema import Form


def test_fixture_loads():
    data = json.load(open("tests/.data/sample_crf.json"))
    forms = [Form(**d) for d in data]
    assert forms, "fixture empty"
    vs = [f for f in forms if f.domain == "VS"]
    assert vs and vs[0].fields, "Vitals missing fields"
