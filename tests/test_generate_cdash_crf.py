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


def test_generate_sample(tmp_path):
    output = tmp_path / "out"
    cmd = [
        sys.executable,
        "scripts/generate_cdash_crf.py",
        "--model",
        "tests/CDASH_Model_v1.3.xlsx",
        "--ig",
        "tests/CDASHIG_v2.3 (1).xlsx",
        "--out",
        str(output),
        "--domains",
        "AE",
        "DM",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert (output / "AE_CRF.docx").exists()
    assert (output / "DM_CRF.docx").exists()
