import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from clinical_data_study_buddy.core.models.schema import FieldDef, Form
from clinical_data_study_buddy.generators.crfgen.exporter.docx import export_docx


class TestDocxExporter(unittest.TestCase):
    @patch("clinical_data_study_buddy.generators.crfgen.exporter.docx.docx.Document")
    def test_export_docx_with_data(self, mock_document):
        # Arrange
        mock_doc_instance = MagicMock()
        mock_table = MagicMock()
        mock_doc_instance.add_table.return_value = mock_table
        mock_document.return_value = mock_doc_instance

        mock_form = MagicMock(spec=Form)
        mock_form.id = "F1"
        mock_form.title = "Form 1"
        mock_form.data = [{"col1": "val1", "col2": "val2"}]
        mock_form.fields = []

        forms = [mock_form]
        outdir = Path("test_output")

        # Act
        export_docx(forms, outdir)

        # Assert
        mock_document.assert_called_once()
        mock_doc_instance.add_heading.assert_called_once_with("Form 1", level=1)
        mock_doc_instance.add_table.assert_called_once()
        mock_doc_instance.save.assert_called_once_with(outdir / "F1.docx")

    @patch("clinical_data_study_buddy.generators.crfgen.exporter.docx.docx.Document")
    def test_export_docx_with_fields(self, mock_document):
        # Arrange
        mock_doc_instance = MagicMock()
        mock_document.return_value = mock_doc_instance

        mock_field = MagicMock(spec=FieldDef)
        mock_field.oid = "F2.1"
        mock_field.prompt = "Field 1"

        mock_form = MagicMock(spec=Form)
        mock_form.id = "F2"
        mock_form.title = "Form 2"
        mock_form.data = []
        mock_form.fields = [mock_field]

        forms = [mock_form]
        outdir = Path("test_output")

        # Act
        export_docx(forms, outdir)

        # Assert
        mock_document.assert_called_once()
        mock_doc_instance.add_heading.assert_called_once_with("Form 2", level=1)
        mock_doc_instance.add_paragraph.assert_called_once_with("Field 1 (F2.1)")
        mock_doc_instance.save.assert_called_once_with(outdir / "F2.docx")

    @patch("clinical_data_study_buddy.generators.crfgen.exporter.docx.apply_styles")
    @patch("clinical_data_study_buddy.generators.crfgen.exporter.docx.docx.Document")
    def test_export_docx_with_style(self, mock_document, mock_apply_styles):
        # Arrange
        mock_doc_instance = MagicMock()
        mock_document.return_value = mock_doc_instance

        mock_form = MagicMock(spec=Form)
        mock_form.id = "F3"
        mock_form.title = "Form 3"
        mock_form.data = []
        mock_form.fields = []

        forms = [mock_form]
        outdir = Path("test_output")
        style = {"some": "style"}

        # Act
        export_docx(forms, outdir, style=style)

        # Assert
        mock_apply_styles.assert_called_once_with(mock_doc_instance, style)

    @patch("clinical_data_study_buddy.generators.crfgen.exporter.docx.docx.Document")
    def test_export_docx_with_output_filename(self, mock_document):
        # Arrange
        mock_doc_instance = MagicMock()
        mock_document.return_value = mock_doc_instance

        mock_form = MagicMock(spec=Form)
        mock_form.id = "F4"
        mock_form.title = "Form 4"
        mock_form.data = []
        mock_form.fields = []

        forms = [mock_form]
        outdir = Path("test_output")
        output_filename = "custom.docx"

        # Act
        export_docx(forms, outdir, output_filename=output_filename)

        # Assert
        mock_doc_instance.save.assert_called_once_with(outdir / output_filename)


if __name__ == "__main__":
    unittest.main()
