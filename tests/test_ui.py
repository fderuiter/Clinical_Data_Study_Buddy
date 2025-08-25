import pytest
from fastapi.testclient import TestClient
from ui.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>CDISC Data Generator</h1>" in response.text


def test_generate_synthetic_data_endpoint(client, mocker):
    # Mock the function that calls the external API
    mock_generate = mocker.patch(
        "ui.main.generate_and_download_synthetic_data",
        return_value="output/ui_generated_data/DM.csv",
    )

    request_data = {
        "dataset_type": "SDTM",
        "domain": "DM",
        "num_subjects": 10,
        "therapeutic_area": "Oncology",
        "data_format": "csv",
    }

    response = client.post("/api/generate-synthetic-data", json=request_data)

    assert response.status_code == 200
    assert response.json() == {
        "message": "Dataset generated successfully",
        "file_path": "output/ui_generated_data/DM.csv",
    }

    mock_generate.assert_called_once()
    # You could add more specific assertions here about the arguments passed to the mock
    call_args = mock_generate.call_args[1]
    assert call_args["dataset_type"] == "SDTM"
    assert call_args["domain"] == "DM"
    assert call_args["num_subjects"] == 10


def test_generate_raw_dataset_package_endpoint(client, mocker):
    mock_generate = mocker.patch(
        "ui.main.generate_raw_dataset_package",
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

    mock_generate.assert_called_once()
    call_args = mock_generate.call_args[1]
    assert call_args["num_subjects"] == 20
    assert call_args["domains"] == ["DM", "AE", "VS"]
