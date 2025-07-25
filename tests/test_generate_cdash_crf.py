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
