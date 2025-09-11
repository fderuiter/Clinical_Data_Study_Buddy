from unittest.mock import patch, MagicMock
from clinical_data_study_buddy.services.cdisc_library_service import get_client

@patch("clinical_data_study_buddy.services.cdisc_library_service.AuthenticatedClient")
@patch("clinical_data_study_buddy.services.cdisc_library_service.httpx.HTTPTransport")
@patch("clinical_data_study_buddy.services.cdisc_library_service.get_api_key")
def test_get_client(mock_get_api_key, mock_http_transport, mock_auth_client):
    """
    Test that the get_client function configures and returns an AuthenticatedClient correctly.
    """
    # Arrange
    mock_api_key = "test-api-key"
    mock_get_api_key.return_value = mock_api_key

    mock_transport_instance = MagicMock()
    mock_http_transport.return_value = mock_transport_instance

    mock_client_instance = MagicMock()
    mock_auth_client.return_value = mock_client_instance

    # Act
    client = get_client()

    # Assert
    mock_get_api_key.assert_called_once()
    mock_http_transport.assert_called_once_with(retries=5)

    expected_headers = {"api-key": mock_api_key, "Accept": "application/json"}
    mock_auth_client.assert_called_once_with(
        base_url="https://library.cdisc.org/api",
        token="dummy",
        headers=expected_headers,
        auth_header_name="api-key",
        prefix="",
        timeout=30.0,
        httpx_args={"transport": mock_transport_instance},
    )

    assert client == mock_client_instance
