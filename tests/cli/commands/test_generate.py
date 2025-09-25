import unittest
from unittest.mock import patch

from typer.testing import CliRunner

from clinical_data_study_buddy.cli.commands.generate import generate_app


class TestGenerateCli(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch(
        "clinical_data_study_buddy.cli.commands.generate.generation_service.generate_tfl_shell"
    )
    def test_tfl_shell_success(self, mock_generate_tfl_shell):
        # Arrange
        spec = "my_spec"
        output_file = "my_output.txt"

        # Act
        result = self.runner.invoke(
            generate_app, ["tfl-shell", "--spec", spec, "--output-file", output_file]
        )

        # Assert
        self.assertEqual(result.exit_code, 0)
        self.assertIn(
            f"Successfully generated TFL shell in {output_file}", result.stdout
        )
        mock_generate_tfl_shell.assert_called_once()

    @patch(
        "clinical_data_study_buddy.cli.commands.generate.generation_service.generate_tfl_shell"
    )
    def test_tfl_shell_error(self, mock_generate_tfl_shell):
        # Arrange
        spec = "my_spec"
        output_file = "my_output.txt"
        mock_generate_tfl_shell.side_effect = Exception("Test error")

        # Act
        result = self.runner.invoke(
            generate_app, ["tfl-shell", "--spec", spec, "--output-file", output_file]
        )

        # Assert
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Test error", result.stdout)
        mock_generate_tfl_shell.assert_called_once()

    @patch(
        "clinical_data_study_buddy.cli.commands.generate.generation_service.generate_edc_raw_dataset_package"
    )
    def test_edc_raw_dataset_package_success(self, mock_generate):
        result = self.runner.invoke(
            generate_app,
            [
                "edc-raw-dataset-package",
                "--num-subjects",
                "20",
                "--therapeutic-area",
                "Oncology",
                "--domains",
                "DM",
                "--domains",
                "AE",
                "--output-dir",
                "output",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("EDC Raw Dataset Package generated successfully", result.stdout)
        mock_generate.assert_called_once()

    @patch(
        "clinical_data_study_buddy.cli.commands.generate.generation_service.generate_synthetic_data"
    )
    def test_synthetic_data_success(self, mock_generate):
        result = self.runner.invoke(
            generate_app,
            [
                "synthetic-data",
                "--standard",
                "sdtmig",
                "--version",
                "3-3",
                "--domain",
                "DM",
                "--num-subjects",
                "30",
                "--output-dir",
                "output",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Saved dataset", result.stdout)
        mock_generate.assert_called_once()

    @patch(
        "clinical_data_study_buddy.cli.commands.generate.generation_service.generate_analysis_code"
    )
    def test_analysis_code_success(self, mock_generate):
        result = self.runner.invoke(
            generate_app,
            [
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
                "output.sas",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Successfully generated SAS code", result.stdout)
        mock_generate.assert_called_once()

    @patch(
        "clinical_data_study_buddy.cli.commands.generate.generation_service.generate_cdash_crf"
    )
    def test_cdash_crf_success(self, mock_generate):
        result = self.runner.invoke(
            generate_app,
            [
                "cdash-crf",
                "--ig-version",
                "v2.3",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("CDASH CRF generated successfully", result.stdout)
        mock_generate.assert_called_once()

    @patch(
        "clinical_data_study_buddy.cli.commands.generate.generation_service.generate_study_protocols"
    )
    def test_study_protocols_success(self, mock_generate):
        result = self.runner.invoke(
            generate_app,
            [
                "study-protocols",
                "--therapeutic-area",
                "Immunology",
                "--treatment-arm",
                "Arm A",
                "--treatment-arm",
                "Arm B",
                "--duration-weeks",
                "24",
                "--phase",
                "3",
                "--output-dir",
                "protocol_docs",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Protocol documents generated in", result.stdout)
        mock_generate.assert_called_once()

    @patch(
        "clinical_data_study_buddy.cli.commands.generate.generation_service.generate_specification_templates"
    )
    def test_specification_templates_success(self, mock_generate):
        result = self.runner.invoke(
            generate_app,
            [
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
                "specs",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Specification templates generated successfully", result.stdout)
        mock_generate.assert_called_once()

    def test_validate_num_subjects_too_low(self):
        result = self.runner.invoke(
            generate_app,
            [
                "edc-raw-dataset-package",
                "--num-subjects",
                "5",
                "--therapeutic-area",
                "Oncology",
                "--domains",
                "DM",
                "--output-dir",
                "output",
            ],
        )
        self.assertNotEqual(result.exit_code, 0)
        self.assertIsInstance(result.exception, SystemExit)

    def test_validate_num_subjects_too_high(self):
        result = self.runner.invoke(
            generate_app,
            [
                "edc-raw-dataset-package",
                "--num-subjects",
                "205",
                "--therapeutic-area",
                "Oncology",
                "--domains",
                "DM",
                "--output-dir",
                "output",
            ],
        )
        self.assertNotEqual(result.exit_code, 0)
        self.assertIsInstance(result.exception, SystemExit)


if __name__ == "__main__":
    unittest.main()
