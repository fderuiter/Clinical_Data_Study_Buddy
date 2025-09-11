import pytest
from typer.testing import CliRunner
from clinical_data_study_buddy.cli.main import app
import os
from unittest.mock import patch, MagicMock
import pandas as pd

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


def test_tfl_shell(mocker):
    mock_generator = MagicMock()
    mock_generator.generate.return_value = "TFL Shell Content"
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.TFLShellGenerator",
        return_value=mock_generator,
    )
    with runner.isolated_filesystem():
        result = runner.invoke(
            app,
            [
                "generate",
                "tfl-shell",
                "--spec",
                "myspec",
                "--output-file",
                "test.docx",
            ],
        )
        assert result.exit_code == 0
        assert "Successfully generated TFL shell" in result.stdout
        with open("test.docx", "r") as f:
            assert f.read() == "TFL Shell Content"


def test_edc_raw_dataset_package(mocker, tmp_path):
    mock_generator = MagicMock()
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.EDCRawDatasetPackageGenerator",
        return_value=mock_generator,
    )
    result = runner.invoke(
        app,
        [
            "generate",
            "edc-raw-dataset-package",
            "--num-subjects",
            "10",
            "--domains",
            "DM",
            "--output-dir",
            str(tmp_path),
        ],
    )
    assert result.exit_code == 0
    mock_generator.generate.assert_called_once()
    assert "EDC Raw Dataset Package generated successfully" in result.stdout


def test_synthetic_data(mocker, tmp_path):
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.get_api_key",
        return_value="test_key",
    )
    mock_form = MagicMock()
    mock_form.domain = "DM"
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.harvest",
        return_value=[mock_form],
    )
    mock_generator = MagicMock()
    mock_generator.generate.return_value = [{"USUBJID": "1"}, {"USUBJID": "2"}]
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.DataGenerator",
        return_value=mock_generator,
    )
    result = runner.invoke(
        app,
        [
            "generate",
            "synthetic-data",
            "--standard",
            "sdtmig",
            "--version",
            "3-3",
            "--domain",
            "DM",
            "--output-dir",
            str(tmp_path),
        ],
    )
    assert result.exit_code == 0
    assert "Saved dataset" in result.stdout
    assert (tmp_path / "DM.csv").exists()


def test_analysis_code(mocker):
    mock_generator = MagicMock()
    mock_generator.generate_code.return_value = "SAS Code"
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.AnalysisGenerator",
        return_value=mock_generator,
    )
    with runner.isolated_filesystem():
        result = runner.invoke(
            app,
            [
                "generate",
                "analysis-code",
                "--language",
                "sas",
                "--dataset",
                "ADSL",
                "--output-type",
                "Demographics",
                "--treatment-var",
                "TRT01A",
                "--output-file",
                "test.sas",
            ],
        )
        assert result.exit_code == 0
        assert "Successfully generated SAS code" in result.stdout
        with open("test.sas", "r") as f:
            assert f.read() == "SAS Code"


def test_cdash_crf(mocker, tmp_path):
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.load_ig",
        return_value=pd.DataFrame({"Domain": ["AE", "VS"]}),
    )
    mock_build_domain_crf = mocker.patch(
        "clinical_data_study_buddy.core.generation_service.build_domain_crf"
    )
    config_path = tmp_path / "crf_config.yaml"
    with open(config_path, "w") as f:
        f.write("key: value")

    result = runner.invoke(
        app,
        [
            "generate",
            "cdash-crf",
            "--ig-version",
            "v2.3",
            "--out",
            str(tmp_path),
            "--config",
            str(config_path),
            "--domains",
            "AE",
        ],
    )
    assert result.exit_code == 0
    mock_build_domain_crf.assert_called_once()
    assert "CDASH CRF generated successfully" in result.stdout


def test_study_protocols(mocker, tmp_path):
    mock_generator = MagicMock()
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.StudyProtocolsGenerator",
        return_value=mock_generator,
    )
    result = runner.invoke(
        app,
        [
            "generate",
            "study-protocols",
            "--therapeutic-area",
            "Oncology",
            "--treatment-arm",
            "A",
            "--treatment-arm",
            "B",
            "--duration-weeks",
            "12",
            "--phase",
            "3",
            "--output-dir",
            str(tmp_path),
        ],
    )
    assert result.exit_code == 0
    mock_generator.generate.assert_called_once()
    assert "Protocol documents generated" in result.stdout


def test_specification_templates(mocker, tmp_path):
    mock_generator = MagicMock()
    mocker.patch(
        "clinical_data_study_buddy.core.generation_service.SpecificationTemplatesGenerator",
        return_value=mock_generator,
    )
    result = runner.invoke(
        app,
        [
            "generate",
            "specification-templates",
            "--product",
            "sdtmig",
            "--version",
            "3-3",
            "--domains",
            "DM",
            "--domains",
            "AE",
            "--output-dir",
            str(tmp_path),
        ],
    )
    assert result.exit_code == 0
    mock_generator.generate.assert_called_once()
    assert "Specification templates generated successfully" in result.stdout


def test_tfl_shell_missing_spec():
    result = runner.invoke(
        app, ["generate", "tfl-shell", "--output-file", "test.docx"]
    )
    assert result.exit_code != 0
    assert "Missing option '--spec'" in result.stderr


def test_synthetic_data_missing_standard():
    result = runner.invoke(
        app,
        [
            "generate",
            "synthetic-data",
            "--version",
            "3-3",
            "--domain",
            "DM",
        ],
    )
    assert result.exit_code != 0
    assert "Missing option '--standard'" in result.stderr
