import unittest
from unittest.mock import patch, MagicMock
from clinical_data_study_buddy.generators.specification_templates_generator import SpecificationTemplatesGenerator

class TestSpecificationTemplatesGenerator(unittest.TestCase):
    @patch("clinical_data_study_buddy.generators.specification_templates_generator.Workbook")
    @patch("clinical_data_study_buddy.generators.specification_templates_generator.harvest")
    @patch("clinical_data_study_buddy.generators.specification_templates_generator.get_api_key")
    def test_generate_single_domain(self, mock_get_api_key, mock_harvest, mock_workbook):
        # Arrange
        mock_wb_instance = MagicMock()
        mock_workbook.return_value = mock_wb_instance
        mock_get_api_key.return_value = "test_key"

        mock_item = MagicMock()
        mock_item.name = "VAR1"
        mock_item.label = "Variable 1"
        mock_item.data_type = "text"
        mock_item.length = 10
        mock_item.codelist = None

        mock_form = MagicMock()
        mock_form.domain = "DM"
        mock_form.items = [mock_item]
        mock_harvest.return_value = [mock_form]

        generator = SpecificationTemplatesGenerator(
            product="sdtmig",
            version="3-3",
            domains=["DM"],
            output_dir="test_output_spec",
        )

        # Act
        generator.generate()

        # Assert
        mock_harvest.assert_called_once_with("test_key", "sdtmig", "3-3")
        mock_wb_instance.create_sheet.assert_called_once_with(title="DM")
        mock_wb_instance.save.assert_called_once()

    @patch("clinical_data_study_buddy.generators.specification_templates_generator.Workbook")
    @patch("clinical_data_study_buddy.generators.specification_templates_generator.harvest")
    @patch("clinical_data_study_buddy.generators.specification_templates_generator.get_api_key")
    def test_generate_domain_not_found(self, mock_get_api_key, mock_harvest, mock_workbook):
        # Arrange
        mock_wb_instance = MagicMock()
        mock_workbook.return_value = mock_wb_instance
        mock_get_api_key.return_value = "test_key"
        mock_harvest.return_value = []

        generator = SpecificationTemplatesGenerator(
            product="sdtmig",
            version="3-3",
            domains=["XX"],
            output_dir="test_output_spec",
        )

        # Act
        generator.generate()

        # Assert
        mock_wb_instance.create_sheet.assert_not_called()
        mock_wb_instance.save.assert_called_once()

if __name__ == "__main__":
    unittest.main()
