import pytest
from typer.testing import CliRunner
from clinical_data_study_buddy.cli.main import app
from unittest.mock import MagicMock, patch
from clinical_data_study_buddy.generators.tfl.migration import TFLSpecMigrationError

runner = CliRunner()


@patch("clinical_data_study_buddy.cli.commands.legacy.console")
def test_legacy_generate(mock_console, mocker):
    mock_harvest = mocker.patch("clinical_data_study_buddy.cli.commands.legacy.harvest")
    mock_exporter = MagicMock()
    mock_get_exporter = mocker.patch(
        "clinical_data_study_buddy.cli.commands.legacy.get_exporter",
        return_value=mock_exporter,
    )
    result = runner.invoke(
        app,
        [
            "legacy",
            "generate",
            "output.docx",
            "sdtmig",
            "3-3",
            "DM",
            "--api-key",
            "test_key",
        ],
    )
    assert result.exit_code == 0
    mock_harvest.assert_called_once()
    mock_get_exporter.assert_called_once()
    mock_exporter.export.assert_called_once()
    mock_console.log.assert_any_call("Exported to output.docx")


@patch("clinical_data_study_buddy.cli.commands.legacy.console")
def test_legacy_protocol(mock_console, mocker):
    mock_generate_protocol_markdown = mocker.patch(
        "clinical_data_study_buddy.cli.commands.legacy.generate_protocol_markdown"
    )
    mock_generate_protocol_markdown.return_value = "output/protocol.md"
    result = runner.invoke(
        app,
        [
            "legacy",
            "protocol",
            "--therapeutic-area",
            "Oncology",
            "--treatment-arm",
            "A",
            "--duration-weeks",
            "12",
            "--phase",
            "3",
        ],
    )
    assert result.exit_code == 0
    mock_generate_protocol_markdown.assert_called_once()
    mock_console.log.assert_any_call("Protocol document generated at output/protocol.md")


@patch("clinical_data_study_buddy.cli.commands.legacy.console")
def test_legacy_spec_valid(mock_console, mocker, tmp_path):
    spec_path = tmp_path / "spec.yaml"
    with open(spec_path, "w") as f:
        f.write("key: value")
    mocker.patch(
        "clinical_data_study_buddy.cli.commands.legacy.migrate_spec",
        return_value={"key": "value"},
    )
    mocker.patch("clinical_data_study_buddy.cli.commands.legacy.TFLSpec")
    result = runner.invoke(app, ["legacy", "spec", str(spec_path)])
    assert result.exit_code == 0
    mock_console.log.assert_any_call("[green]Spec file is valid.[/green]")


@patch("clinical_data_study_buddy.cli.commands.legacy.console")
def test_legacy_spec_invalid(mock_console, mocker, tmp_path):
    spec_path = tmp_path / "spec.yaml"
    with open(spec_path, "w") as f:
        f.write("key: value")
    mocker.patch(
        "clinical_data_study_buddy.cli.commands.legacy.migrate_spec",
        side_effect=TFLSpecMigrationError("Invalid spec"),
    )
    result = runner.invoke(app, ["legacy", "spec", str(spec_path)])
    assert result.exit_code != 0
    mock_console.log.assert_any_call("[red]Spec file is invalid:[/red]")
