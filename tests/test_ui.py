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


from cdisc_generators.crfgen.schema import Form, FieldDef

def test_generate_synthetic_data_endpoint(client, mocker):
    mock_form = Form(
        title="DM",
        domain="DM",
        fields=[FieldDef(oid="USUBJID", prompt="Subject ID", datatype="text", cdash_var="USUBJID")],
    )
    mock_get_api_key = mocker.patch("ui.main.get_api_key", return_value="test-key")
    mock_harvest = mocker.patch("ui.main.harvest", return_value=[mock_form])

    mock_dataset = [{"USUBJID": "SUBJ-001"}]
    mock_generator_instance = mocker.Mock()
    mock_generator_instance.generate.return_value = mock_dataset
    mock_generator_class = mocker.patch("ui.main.DataGenerator", return_value=mock_generator_instance)

    request_data = {
        "dataset_type": "SDTM",
        "domain": "DM",
        "num_subjects": 1,
        "therapeutic_area": "Oncology",
        "data_format": "csv",
    }

    response = client.post("/api/generate-synthetic-data", json=request_data)

    assert response.status_code == 200
    assert response.json()["message"] == "Dataset generated successfully"

    mock_harvest.assert_called_once()
    mock_generator_class.assert_called_once_with(mock_form)
    mock_generator_instance.generate.assert_called_once_with(1)


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


def test_generate_analysis_code_endpoint(client, mocker):
    mock_generator_instance = mocker.Mock()
    mock_generator_instance.generate_code.return_value = "/* SAS code */"
    mock_generator_class = mocker.patch(
        "ui.main.AnalysisGenerator", return_value=mock_generator_instance
    )

    request_data = {
        "language": "sas",
        "dataset_path": "testing/test_data/DM.csv",
        "output_type": "demographics",
        "treatment_var": "ARM",
    }

    response = client.post("/api/generate-analysis-code", json=request_data)

    assert response.status_code == 200
    assert response.json()["message"] == "Analysis code generated successfully"
    assert response.json()["file_path"] == "output/ui_generated_data/analysis.sas"

    mock_generator_class.assert_called_once_with(
        language="sas",
        dataset="testing/test_data/DM.csv",
        output_type="demographics",
        treatment_var="ARM",
    )
    mock_generator_instance.generate_code.assert_called_once()
