import os
import subprocess
from pathlib import Path

from crfgen.schema import load_forms
from crfgen.exporter import EXPORTERS
import crfgen.exporter.csv  # register csv exporter


def test_render_csv(tmp_path: Path):
    forms = load_forms("tests/.data/sample_crf.json")
    exporter = EXPORTERS["csv"]
    exporter(forms, tmp_path)
    csv_file = tmp_path / "forms.csv"
    assert csv_file.exists()
    text = csv_file.read_text().splitlines()
    assert text
    # header present
    assert text[0].startswith("form,domain,scenario,oid,prompt,datatype,codelist")
    # should produce a row per field
    num_fields = sum(len(f.fields) for f in forms)
    assert len(text) == num_fields + 1


def test_build_script_csv(tmp_path: Path):
    cmd = [
        "python",
        "scripts/build.py",
        "--source",
        "tests/.data/sample_crf.json",
        "--outdir",
        str(tmp_path),
        "--formats",
        "csv",
    ]
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    subprocess.check_call(cmd, env=env)
    assert (Path(tmp_path) / "forms.csv").exists()
