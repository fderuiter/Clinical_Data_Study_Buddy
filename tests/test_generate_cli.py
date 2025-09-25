from typer.testing import CliRunner

from clinical_data_study_buddy.cli.main import app

runner = CliRunner()


def test_edc_raw_dataset_package_invalid_num_subjects():
    result = runner.invoke(
        app,
        [
            "generate",
            "edc-raw-dataset-package",
            "--num-subjects",
            "5",
            "--domains",
            "DM",
        ],
    )
    assert result.exit_code != 0
    assert "Invalid value for '--num-subjects'" in result.stderr
