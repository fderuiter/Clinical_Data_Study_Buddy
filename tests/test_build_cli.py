import pathlib
from typer.testing import CliRunner
import pytest
from cdisc_generators_api.cdisc_cli.main import app
from unittest.mock import patch

runner = CliRunner()

@pytest.mark.parametrize("fmt", [["md"], ["csv"], ["md", "csv"]])
@patch("cdisc_generators_api.cdisc_cli.main.get_api_key")
@patch("cdisc_generators_api.cdisc_cli.main.harvest")
def test_build_cli(mock_harvest, mock_get_api_key, tmp_path: pathlib.Path, fmt):
    mock_get_api_key.return_value = "test_key"
    mock_harvest.return_value = []

    cmd = [
        "build",
        "--source",
        "tests/.data/sample_crf.json",
        "--outdir",
        str(tmp_path)
    ]
    for f in fmt:
        cmd.extend(["--formats", f])

    result = runner.invoke(app, cmd)
    assert result.exit_code == 0, result.stdout

    for f in fmt:
        if f == "md":
            assert any(tmp_path.glob("*.md"))
        elif f == "csv":
            assert (tmp_path / "forms.csv").exists()
        elif f == "tex":
            assert any(tmp_path.glob("*.tex"))
