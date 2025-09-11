import pytest
import pathlib
from clinical_data_study_buddy.core.generation_service import generate_analysis_code, generate_tfl_shell

def test_generate_analysis_code_creates_output_dir(tmp_path):
    """
    Test that generate_analysis_code creates the output directory if it does not exist.
    """
    output_dir = tmp_path / "non_existent_dir"
    output_file = output_dir / "test.sas"

    # This should not raise FileNotFoundError after the fix
    try:
        generate_analysis_code(
            language="sas",
            dataset="ADSL",
            output_type="Demographics",
            treatment_var="TRT01A",
            output_file=output_file,
        )
    except FileNotFoundError:
        pytest.fail("generate_analysis_code raised FileNotFoundError unexpectedly.")

    assert output_file.exists()

def test_generate_tfl_shell_creates_output_dir(tmp_path):
    """
    Test that generate_tfl_shell creates the output directory if it does not exist.
    """
    output_dir = tmp_path / "non_existent_dir"
    output_file = output_dir / "test.txt"

    try:
        generate_tfl_shell(
            spec="My TFL Spec",
            output_file=output_file,
        )
    except FileNotFoundError:
        pytest.fail("generate_tfl_shell raised FileNotFoundError unexpectedly.")

    assert output_file.exists()
