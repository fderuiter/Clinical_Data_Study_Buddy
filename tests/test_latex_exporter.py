import os
import subprocess
from pathlib import Path

from crfgen.schema import load_forms
from crfgen.exporter import EXPORTERS
import crfgen.exporter.latex  # register tex exporter


def test_render_tex(tmp_path: Path):
    forms = load_forms("tests/.data/sample_crf.json")
    exporter = EXPORTERS["tex"]
    exporter(forms, tmp_path)
    files = list(tmp_path.glob("*.tex"))
    assert files
    txt = files[0].read_text()
    assert "\\textbf{OID}" in txt


def test_build_script(tmp_path: Path):
    cmd = [
        "python",
        "scripts/build.py",
        "--source",
        "tests/.data/sample_crf.json",
        "--outdir",
        str(tmp_path),
        "--formats",
        "tex",
    ]
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    subprocess.check_call(cmd, env=env)
    assert list(Path(tmp_path).glob("*.tex"))
