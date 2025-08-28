import json
from pathlib import Path
from typer.testing import CliRunner
from cdisc_generators_api.cdisc_cli.main import app

runner = CliRunner()

def test_download_standard(mocker):
    """
    Tests that the download-standard command runs successfully
    and creates the expected output file.
    """
    mock_get_client = mocker.patch(
        "cdisc_generators_api.core.download_service._get_client"
    )
    mock_sdtmig_version = {
        "_links": {
            "classes": [{"title": "Events"}],
            "datasets": [{"title": "DM"}],
        }
    }
    mock_get_sdtmig_version = mocker.patch(
        "cdisc_library_client.api.sdtm_implementation_guide_sdtmig.get_mdr_sdtmig_version.sync",
        return_value=mock_sdtmig_version,
    )
    mock_get_sdtmig_version_classes = mocker.patch(
        "cdisc_library_client.api.sdtm_implementation_guide_sdtmig.get_mdr_sdtmig_version_classes.sync",
        return_value={"name": "Events"},
    )
    mock_get_sdtmig_version_datasets = mocker.patch(
        "cdisc_library_client.api.sdtm_implementation_guide_sdtmig.get_mdr_sdtmig_version_datasets.sync",
        return_value={"name": "DM"},
    )

    with runner.isolated_filesystem() as temp_dir:
        output_dir = Path(temp_dir)
        result = runner.invoke(
            app,
            [
                "download",
                "standard",
                "--standard",
                "sdtmig",
                "--version",
                "3-3",
                "--output-dir",
                str(output_dir),
            ],
        )
        assert result.exit_code == 0
        output_file = output_dir / "sdtmig_3-3.json"
        assert output_file.exists()
        with open(output_file, "r") as f:
            data = json.load(f)
        assert data["classes"][0]["name"] == "Events"
        assert data["datasets"][0]["name"] == "DM"
