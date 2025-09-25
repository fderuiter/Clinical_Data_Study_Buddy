import pytest
import yaml
from click.testing import CliRunner
from pydantic import ValidationError

from clinical_data_study_buddy.core.filename_service import (
    generate_bookmark,
    generate_filename,
)
from clinical_data_study_buddy.generators.tfl.autonumber import AutoNumberer
from clinical_data_study_buddy.generators.tfl.models import TFLSpec

# from src.crfgen.crfgen import app

VALID_SPEC = """
version: 1.0
tfls:
  - shell_id: "T14.1.1"
    title: "Demographic and Baseline Characteristics"
    population: "SAFETY"
    layout:
      orientation: "portrait"
      page_size: "A4"
"""

INVALID_SPEC = """
version: 1.0
tfls:
  - shell_id: "T14.1.1"
    title: "Demographic and Baseline Characteristics"
    population: "SAFETY"
    layout:
      orientation: "portrait"
"""


def test_valid_spec_loading():
    spec_data = yaml.safe_load(VALID_SPEC)
    spec = TFLSpec(**spec_data)
    assert spec.version == 1.0
    assert len(spec.tfls) == 1
    assert spec.tfls[0].shell_id == "T14.1.1"


def test_invalid_spec_loading():
    spec_data = yaml.safe_load(INVALID_SPEC)
    with pytest.raises(ValidationError):
        TFLSpec(**spec_data)


def test_autonumberer():
    spec_data = yaml.safe_load(VALID_SPEC)
    spec = TFLSpec(**spec_data)
    autonumberer = AutoNumberer(spec)

    # Test generate_filename
    filename = generate_filename(spec.tfls[0], extension="pdf")
    assert filename == "t14-1-1.pdf"

    # Test generate_bookmark
    bookmark = generate_bookmark(spec.tfls[0])
    assert bookmark == "T14_1_1"

    # Test assign_numbers
    spec.tfls.append(spec.tfls[0].model_copy(deep=True))  # Add another TFL
    numbered_spec = autonumberer.assign_numbers()
    assert numbered_spec.tfls[0].shell_id == "T14.1.1"
    assert numbered_spec.tfls[1].shell_id == "T14.1.2"


@pytest.mark.skip(reason="CLI has been refactored")
def test_spec_cli_valid(tmp_path):
    spec_file = tmp_path / "spec.yaml"
    spec_file.write_text(VALID_SPEC)

    # runner = CliRunner()
    # result = runner.invoke(app, ["spec", str(spec_file)])

    # assert result.exit_code == 0
    # assert "Spec file is valid" in result.output


@pytest.mark.skip(reason="CLI has been refactored")
def test_spec_cli_invalid(tmp_path):
    spec_file = tmp_path / "spec.yaml"
    spec_file.write_text(INVALID_SPEC)

    # runner = CliRunner()
    # result = runner.invoke(app, ["spec", str(spec_file)])

    # assert result.exit_code != 0
    # assert "Spec file is invalid" in result.output
