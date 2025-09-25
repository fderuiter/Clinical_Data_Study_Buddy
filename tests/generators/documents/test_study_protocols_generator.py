import unittest
from unittest.mock import patch

from clinical_data_study_buddy.generators.documents.study_protocols_generator import (
    StudyProtocolsGenerator,
)


class TestStudyProtocolsGenerator(unittest.TestCase):
    @patch(
        "clinical_data_study_buddy.generators.documents.study_protocols_generator.os.makedirs"
    )
    @patch(
        "clinical_data_study_buddy.generators.documents.study_protocols_generator.generate_protocol_markdown"
    )
    @patch(
        "clinical_data_study_buddy.generators.documents.study_protocols_generator.StudyProtocol"
    )
    def test_generate(
        self, mock_study_protocol, mock_generate_protocol_markdown, mock_makedirs
    ):
        # Arrange
        therapeutic_area = "Oncology"
        treatment_arms = ["Arm A", "Arm B"]
        duration_weeks = 12
        phase = 2
        output_dir = "test_output"

        generator = StudyProtocolsGenerator(
            therapeutic_area=therapeutic_area,
            treatment_arms=treatment_arms,
            duration_weeks=duration_weeks,
            phase=phase,
            output_dir=output_dir,
        )

        # Act
        generator.generate()

        # Assert
        mock_makedirs.assert_called_once_with(output_dir, exist_ok=True)
        mock_study_protocol.assert_called_once_with(
            therapeutic_area=therapeutic_area,
            treatment_arms=treatment_arms,
            duration_weeks=duration_weeks,
            phase=phase,
        )
        mock_generate_protocol_markdown.assert_called_once_with(
            mock_study_protocol.return_value, output_dir
        )


if __name__ == "__main__":
    unittest.main()
