import os
import subprocess
from pathlib import Path

from crfgen.schema import load_forms
from crfgen.exporter import EXPORTERS
import crfgen.exporter.odm  # register odm exporter


def test_render_odm(tmp_path: Path):
    forms = load_forms("tests/.data/sample_crf.json")
    exporter = EXPORTERS["odm"]
    exporter(forms, tmp_path)
    file = tmp_path / "forms.odm.xml"
    assert file.exists()
    txt = file.read_text()
    assert "<FormDef" in txt


def test_build_script(tmp_path: Path):
    cmd = [
        "python",
        "scripts/build.py",
        "--source",
        "tests/.data/sample_crf.json",
        "--outdir",
        str(tmp_path),
        "--formats",
        "odm",
    ]
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    subprocess.check_call(cmd, env=env)
    assert (tmp_path / "forms.odm.xml").exists()
