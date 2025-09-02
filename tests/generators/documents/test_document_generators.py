import pytest
import pathlib
from docx import Document
from cdisc_data_symphony.generators.documents.adrg_generator import ADRGGenerator
from cdisc_data_symphony.generators.documents.sdrg_generator import SDRGGenerator

@pytest.fixture
def study_config_path():
    return pathlib.Path("tests/fixtures/study_config.json")

def test_adrg_generator(study_config_path, tmp_path):
    output_path = tmp_path / "adrg.docx"
    generator = ADRGGenerator(study_config_path)
    generator.generate(output_path)

    assert output_path.exists()
    doc = Document(output_path)
    assert doc.paragraphs[0].text == "Analysis Data Reviewer's Guide"

def test_sdrg_generator(study_config_path, tmp_path):
    output_path = tmp_path / "sdrg.docx"
    generator = SDRGGenerator(study_config_path)
    generator.generate(output_path)

    assert output_path.exists()
    doc = Document(output_path)
    assert doc.paragraphs[0].text == "Study Data Reviewer's Guide"
