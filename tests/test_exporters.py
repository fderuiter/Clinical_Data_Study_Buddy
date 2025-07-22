import pathlib, json, tempfile
from crfgen.schema import Form
from crfgen.exporter import registry as reg
import importlib

# import exporters so they register
for m in ("markdown","latex","csv"):
    importlib.import_module(f"crfgen.exporter.{m}")

forms = [Form(**json.load(open("tests/.data/sample_crf.json"))[0])]

def _tmpdir():
    return pathlib.Path(tempfile.mkdtemp())

def test_md():
    out=_tmpdir(); reg.get("md")(forms, out)
    assert any(out.glob("*.md"))

def test_csv():
    out=_tmpdir(); reg.get("csv")(forms, out)
    assert (out/"forms.csv").exists()
