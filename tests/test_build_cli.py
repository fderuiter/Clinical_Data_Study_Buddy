import pathlib
import subprocess
import sys

import pytest


@pytest.mark.parametrize("fmt", [["md"], ["csv"], ["md", "csv"]])
def test_build_cli(tmp_path: pathlib.Path, fmt):
    cmd = [
        sys.executable,
        "scripts/build.py",
        "--source",
        "tests/.data/sample_crf.json",
        "--outdir",
        str(tmp_path),
        "--formats",
        *fmt,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr

    for f in fmt:
        if f == "md":
            assert any(tmp_path.glob("*.md"))
        elif f == "csv":
            assert (tmp_path / "forms.csv").exists()
        elif f == "tex":
            assert any(tmp_path.glob("*.tex"))
