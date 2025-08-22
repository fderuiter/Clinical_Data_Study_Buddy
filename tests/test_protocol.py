import os
from unittest.mock import MagicMock
import pytest
from protogen.gantt import generate_gantt_chart
from protogen.protocol import StudyProtocol, generate_protocol_markdown
from protogen.clinicaltrials import search_studies

@pytest.fixture
def mock_requests_get(mocker):
    """Fixture to mock requests.get"""
    mock = mocker.patch("requests.get")
    mock.return_value = MagicMock()
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {"studies": [{"protocolSection": {"identificationModule": {"nctId": "NCT12345678"}}}]}
    return mock

def test_generate_gantt_chart(tmpdir):
    tasks = [
        {'name': 'Test Task', 'start': '2024-01-01', 'end': '2024-01-31'},
    ]
    output_path = os.path.join(tmpdir, "gantt.png")
    generate_gantt_chart(tasks, output_path)
    assert os.path.exists(output_path)

def test_search_studies(mock_requests_get):
    studies = search_studies("test query")
    assert studies["studies"][0]["protocolSection"]["identificationModule"]["nctId"] == "NCT12345678"
    mock_requests_get.assert_called_once()

def test_generate_protocol_markdown(tmpdir):
    protocol_data = {
        "therapeutic_area": "Testing",
        "treatment_arms": ["Test Arm 1", "Test Arm 2"],
        "duration_weeks": 4,
        "phase": 1,
    }
    protocol = StudyProtocol(**protocol_data)
    output_dir = str(tmpdir)

    markdown_path = generate_protocol_markdown(protocol, output_dir)

    assert os.path.exists(markdown_path)
    assert os.path.exists(os.path.join(output_dir, "gantt_chart.png"))

    with open(markdown_path, "r") as f:
        content = f.read()
        assert "Testing" in content
        assert "Test Arm 1" in content
