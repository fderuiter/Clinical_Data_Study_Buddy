import json
from pathlib import Path
from unittest.mock import MagicMock, patch, mock_open
import pytest
from clinical_data_study_buddy.core.download_service import download_standard

@pytest.fixture
def mock_cdisc_client():
    """Fixture for a mocked AuthenticatedClient."""
    return MagicMock()

def test_download_standard_unsupported_standard():
    """
    Test that download_standard raises a ValueError for an unsupported standard.
    """
    with pytest.raises(ValueError, match="Only sdtmig is supported at this time."):
        download_standard("unsupported", "1.0", Path("output"))

@patch("clinical_data_study_buddy.core.download_service.get_client")
@patch("clinical_data_study_buddy.core.download_service.get_mdr_sdtmig_version.sync")
@patch("clinical_data_study_buddy.core.download_service.get_mdr_sdtmig_version_classes.sync")
@patch("clinical_data_study_buddy.core.download_service.get_mdr_sdtmig_version_datasets.sync")
@patch("pathlib.Path.mkdir")
@patch("builtins.open", new_callable=mock_open)
def test_download_standard_success(
    mock_open_file,
    mock_mkdir,
    mock_get_datasets,
    mock_get_classes,
    mock_get_version,
    mock_get_client,
    mock_cdisc_client,
):
    """
    Test the successful download and processing of a standard.
    """
    # Arrange
    mock_get_client.return_value = mock_cdisc_client
    mock_get_version.return_value = {
        "_links": {
            "classes": [{"title": "class1"}],
            "datasets": [{"title": "dataset1"}],
        }
    }
    mock_get_classes.return_value = {"name": "class1_data"}
    mock_get_datasets.return_value = {"name": "dataset1_data"}
    output_dir = Path("output")
    version = "3.3"
    standard = "sdtmig"

    # Act
    download_standard(standard, version, output_dir)

    # Assert
    mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    mock_get_client.assert_called_once()
    mock_get_version.assert_called_once_with(client=mock_cdisc_client, version=version)
    mock_get_classes.assert_called_once_with(client=mock_cdisc_client, version=version, class_name="class1")
    mock_get_datasets.assert_called_once_with(client=mock_cdisc_client, version=version, dataset_name="dataset1")

    output_file = output_dir / f"{standard}_{version}.json"
    mock_open_file.assert_called_once_with(output_file, "w")

    handle = mock_open_file()
    # json.dump with indent writes multiple lines, so we need to join them
    written_content = "".join(c[0][0] for c in handle.write.call_args_list)
    written_data = json.loads(written_content)

    expected_data = {
        "_links": {
            "classes": [{"title": "class1"}],
            "datasets": [{"title": "dataset1"}],
        },
        "classes": [{"name": "class1_data"}],
        "datasets": [{"name": "dataset1_data"}],
    }
    assert written_data == expected_data
