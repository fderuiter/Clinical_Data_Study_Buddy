import pytest
import json
from unittest.mock import Mock, MagicMock
from clinical_data_study_buddy.generators.documents.adrg_generator import ADRGGenerator
from clinical_data_study_buddy.core.models.config import StudyConfig

@pytest.fixture
def study_config_data():
    """
    Fixture for a sample StudyConfig object as a dictionary.
    """
    return {
        "study_id": "TEST_STUDY",
        "protocol_id": "TEST_PROTOCOL",
        "protocol_title": "Test Protocol Title",
        "sponsors": ["Test Sponsor"],
        "version": "1.0"
    }

@pytest.fixture
def adrg_generator(study_config_data, tmp_path):
    """
    Fixture for an ADRGGenerator instance.
    """
    config_path = tmp_path / "study_config.json"
    with open(config_path, "w") as f:
        json.dump(study_config_data, f)

    generator = ADRGGenerator(str(config_path))
    return generator

def test_document_type(adrg_generator):
    """
    Test that the document_type property returns 'ADRG'.
    """
    assert adrg_generator.document_type == "ADRG"

def test_add_title(adrg_generator):
    """
    Test that the _add_title method adds the correct title to the document.
    """
    mock_document = MagicMock()
    adrg_generator._add_title(mock_document)
    mock_document.add_heading.assert_called_once_with('Analysis Data Reviewer\'s Guide', level=0)

def test_add_sections(adrg_generator):
    """
    Test that the _add_sections method adds all the required sections to the document.
    """
    mock_document = MagicMock()
    adrg_generator._add_sections(mock_document)

    # Check that all headings are added
    headings = [call[0][0] for call in mock_document.add_heading.call_args_list]
    expected_headings = [
        '1. Introduction',
        '2. Protocol Description',
        '3. Analysis Datasets',
        '4. Data Conformance',
        '5. Program and Macro Catalog',
        '6. Data Listings',
        '7. Figures and Tables'
    ]
    assert headings == expected_headings

    # Check some of the content
    paragraphs = [call[0][0] for call in mock_document.add_paragraph.call_args_list]
    assert f"This document describes the analysis datasets for {adrg_generator.study_config.study_id}." in paragraphs
    assert f"Protocol: {adrg_generator.study_config.protocol_id or 'N/A'}" in paragraphs
    assert f"Protocol Title: {adrg_generator.study_config.protocol_title or 'N/A'}" in paragraphs
