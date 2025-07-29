import subprocess
import sys


def test_help():
    result = subprocess.run(
        [sys.executable, "scripts/generate_cdash_crf.py", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Generate Word CRFs" in result.stdout


def test_generate(tmp_path):
    out_dir = tmp_path / "out"
    result = subprocess.run(
        [
            sys.executable,
            "scripts/generate_cdash_crf.py",
            "--model",
            "tests/CDASH_Model_v1.3.xlsx",
            "--ig",
            "tests/CDASHIG_v2.3 (1).xlsx",
            "--out",
            str(out_dir),
            "--domains",
            "AE",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert (out_dir / "AE_CRF.docx").exists()
