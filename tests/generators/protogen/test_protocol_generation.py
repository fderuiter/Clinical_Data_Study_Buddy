import unittest
from unittest.mock import patch, MagicMock, mock_open
from clinical_data_study_buddy.generators.protogen.protocol import StudyProtocol, generate_protocol_markdown

class TestProtocol(unittest.TestCase):
    @patch("clinical_data_study_buddy.generators.protogen.protocol.generate_gantt_chart")
    @patch("clinical_data_study_buddy.generators.protogen.protocol.Environment")
    def test_generate_protocol_markdown(self, mock_environment, mock_generate_gantt_chart):
        # Arrange
        protocol = StudyProtocol(
            therapeutic_area="Immunology",
            treatment_arms=["Arm C", "Arm D"],
            duration_weeks=24,
            phase=3,
        )
        output_dir = "test_output_protocol"

        mock_template = MagicMock()
        mock_environment.return_value.get_template.return_value = mock_template

        # Act
        with patch("builtins.open", mock_open()) as mock_file:
            generate_protocol_markdown(protocol, output_dir)

        # Assert
        mock_generate_gantt_chart.assert_called_once()
        mock_environment.assert_called_once_with(loader=unittest.mock.ANY)
        mock_template.render.assert_called_once_with(protocol=protocol)
        mock_file.assert_called_once_with(f"{output_dir}/protocol.md", "w")
        mock_file().write.assert_called_once_with(mock_template.render.return_value)

if __name__ == "__main__":
    unittest.main()
