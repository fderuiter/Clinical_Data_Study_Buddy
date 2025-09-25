import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from clinical_data_study_buddy.core.models.schema import FieldDef, Form
from clinical_data_study_buddy.generators.crfgen.exporter.odm import render_odm


class TestOdmExporter(unittest.TestCase):
    @patch("clinical_data_study_buddy.generators.crfgen.exporter.odm.ODM.ODM")
    def test_render_odm_single_form(self, mock_odm_root):
        # Arrange
        mock_root_instance = MagicMock()
        mock_odm_root.return_value = mock_root_instance

        mock_field = MagicMock(spec=FieldDef)
        mock_field.oid = "F1.1"
        mock_field.prompt = "Field 1"
        mock_field.datatype = "text"
        mock_field.range_check = None

        mock_form = MagicMock(spec=Form)
        mock_form.domain = "DM"
        mock_form.title = "Demographics"
        mock_form.fields = [mock_field]

        forms = [mock_form]
        outdir = Path("test_output_odm")

        # Act
        render_odm(forms, outdir)

        # Assert
        mock_odm_root.assert_called_once()
        mock_root_instance.write_xml.assert_called_once_with(
            str(outdir / "forms.odm.xml")
        )

    @patch("clinical_data_study_buddy.generators.crfgen.exporter.odm.ODM.RangeCheck")
    @patch("clinical_data_study_buddy.generators.crfgen.exporter.odm.ODM.ODM")
    def test_render_odm_with_range_check(self, mock_odm_root, mock_range_check):
        # Arrange
        mock_root_instance = MagicMock()
        mock_odm_root.return_value = mock_root_instance

        mock_field = MagicMock(spec=FieldDef)
        mock_field.oid = "F2.1"
        mock_field.prompt = "Field 2"
        mock_field.datatype = "integer"
        mock_field.range_check = ["1", "2", "3"]

        mock_form = MagicMock(spec=Form)
        mock_form.domain = "VS"
        mock_form.title = "Vital Signs"
        mock_form.fields = [mock_field]

        forms = [mock_form]
        outdir = Path("test_output_odm")

        # Act
        render_odm(forms, outdir)

        # Assert
        mock_range_check.assert_called_once_with(Comparator="EQ", SoftHard="Soft")


if __name__ == "__main__":
    unittest.main()
