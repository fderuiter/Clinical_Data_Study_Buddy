import pytest
from fastapi.testclient import TestClient
from clinical_data_study_buddy.web.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>CDISC Data Generator</h1>" in response.text


def test_generate_synthetic_data_endpoint(client, mocker):
    mock_create_synthetic_data = mocker.patch(
        "clinical_data_study_buddy.web.services.data_generation_service.create_synthetic_data",
        return_value="output/ui_generated_data/DM.csv",
    )

    request_data = {
        "dataset_type": "SDTM",
        "domain": "DM",
        "num_subjects": 1,
        "therapeutic_area": "Oncology",
        "data_format": "csv",
    }

    response = client.post("/api/generate-synthetic-data", json=request_data)

    assert response.status_code == 200
    assert response.json() == {
        "message": "Dataset generated successfully",
        "file_path": "output/ui_generated_data/DM.csv",
    }

    mock_create_synthetic_data.assert_called_once_with(
        "SDTM", "DM", 1, "Oncology", "csv"
    )


def test_generate_raw_dataset_package_endpoint(client, mocker):
    mock_create_raw_dataset_package = mocker.patch(
        "clinical_data_study_buddy.web.services.data_generation_service.create_raw_dataset_package",
        return_value="output/ui_generated_data/edc_raw_datasets.zip",
    )

    request_data = {
        "num_subjects": 20,
        "therapeutic_area": "Oncology",
        "domains": ["DM", "AE", "VS"],
        "study_story": "none",
        "output_format": "csv",
    }

    response = client.post("/api/generate-raw-dataset-package", json=request_data)

    assert response.status_code == 200
    assert response.json() == {
        "message": "Raw dataset package generated successfully",
        "file_path": "output/ui_generated_data/edc_raw_datasets.zip",
    }

    mock_create_raw_dataset_package.assert_called_once_with(
        20, "Oncology", ["DM", "AE", "VS"], "none", "csv"
    )


def test_generate_analysis_code_endpoint(client, mocker):
    mock_create_analysis_code = mocker.patch(
        "clinical_data_study_buddy.web.services.analysis_service.create_analysis_code",
        return_value="output/ui_generated_data/analysis.sas",
    )

    request_data = {
        "language": "sas",
        "dataset_path": "testing/test_data/DM.csv",
        "output_type": "demographics",
        "treatment_var": "ARM",
    }

    response = client.post("/api/generate-analysis-code", json=request_data)

    assert response.status_code == 200
    assert response.json() == {
        "message": "Analysis code generated successfully",
        "file_path": "output/ui_generated_data/analysis.sas",
    }

    mock_create_analysis_code.assert_called_once_with(
        "sas", "testing/test_data/DM.csv", "demographics", "ARM"
    )
