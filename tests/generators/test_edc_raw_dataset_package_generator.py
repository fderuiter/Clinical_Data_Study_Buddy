from unittest.mock import patch

import pytest

from clinical_data_study_buddy.core.models.schema import FieldDef, Form
from clinical_data_study_buddy.generators.edc_raw_dataset_package_generator import (
    EDCRawDatasetPackageGenerator,
)


@pytest.fixture
def mock_get_api_key():
    with patch(
        "clinical_data_study_buddy.generators.edc_raw_dataset_package_generator.get_api_key"
    ) as mock:
        mock.return_value = "fake_api_key"
        yield mock


@pytest.fixture
def mock_harvest():
    with patch(
        "clinical_data_study_buddy.generators.edc_raw_dataset_package_generator.harvest"
    ) as mock:
        mock.return_value = [
            Form(
                title="DM",
                domain="DM",
                fields=[
                    FieldDef(
                        oid="USUBJID",
                        prompt="Subject ID",
                        datatype="text",
                        cdash_var="USUBJID",
                    )
                ],
            ),
            Form(
                title="AE",
                domain="AE",
                fields=[
                    FieldDef(
                        oid="AETERM",
                        prompt="Adverse Event Term",
                        datatype="text",
                        cdash_var="AETERM",
                    )
                ],
            ),
        ]
        yield mock


@pytest.fixture
def mock_data_generator():
    with patch(
        "clinical_data_study_buddy.generators.edc_raw_dataset_package_generator.DataGenerator"
    ) as mock:
        instance = mock.return_value
        instance.generate.return_value = [{"USUBJID": "1"}, {"USUBJID": "2"}]
        yield mock


@pytest.fixture
def mock_apply_study_story():
    with patch(
        "clinical_data_study_buddy.generators.edc_raw_dataset_package_generator.apply_study_story"
    ) as mock:
        yield mock


@pytest.fixture
def mock_generate_define_xml():
    with patch(
        "clinical_data_study_buddy.generators.edc_raw_dataset_package_generator.generate_define_xml"
    ) as mock:
        yield mock


@pytest.fixture
def mock_package_datasets():
    with patch(
        "clinical_data_study_buddy.generators.edc_raw_dataset_package_generator.package_datasets"
    ) as mock:
        yield mock


def test_edc_raw_dataset_package_generator(
    tmp_path,
    mock_get_api_key,
    mock_harvest,
    mock_data_generator,
    mock_apply_study_story,
    mock_generate_define_xml,
    mock_package_datasets,
):
    output_dir = tmp_path
    generator = EDCRawDatasetPackageGenerator(
        num_subjects=10,
        therapeutic_area="Oncology",
        domains=["DM", "AE"],
        study_story="none",
        output_dir=output_dir,
        output_format="csv",
    )
    generator.generate()

    # Assert that the mocked functions were called
    assert mock_get_api_key.called
    assert mock_harvest.called
    assert mock_data_generator.called
    assert not mock_apply_study_story.called
    assert mock_generate_define_xml.called
    assert mock_package_datasets.called

    # Assert that the temp directory was created
    temp_dir = output_dir / "temp_datasets"
    assert temp_dir.exists()

    # Assert that the datasets were created
    assert (temp_dir / "DM.csv").exists()
    assert (temp_dir / "AE.csv").exists()


def test_edc_raw_dataset_package_generator_with_study_story(
    tmp_path,
    mock_get_api_key,
    mock_harvest,
    mock_data_generator,
    mock_apply_study_story,
    mock_generate_define_xml,
    mock_package_datasets,
):
    output_dir = tmp_path
    generator = EDCRawDatasetPackageGenerator(
        num_subjects=10,
        therapeutic_area="Oncology",
        domains=["DM"],
        study_story="mystory",
        output_dir=output_dir,
        output_format="csv",
    )
    generator.generate()

    assert mock_apply_study_story.called


def test_edc_raw_dataset_package_generator_domain_not_found(
    tmp_path,
    mock_get_api_key,
    mock_harvest,
    mock_data_generator,
    mock_apply_study_story,
    mock_generate_define_xml,
    mock_package_datasets,
    capsys,
):
    output_dir = tmp_path
    generator = EDCRawDatasetPackageGenerator(
        num_subjects=10,
        therapeutic_area="Oncology",
        domains=["VS"],
        study_story="none",
        output_dir=output_dir,
        output_format="csv",
    )
    generator.generate()

    captured = capsys.readouterr()
    assert "Warning: Domain VS not found in CDISC Library. Skipping." in captured.out
    assert not (output_dir / "temp_datasets" / "VS.csv").exists()
