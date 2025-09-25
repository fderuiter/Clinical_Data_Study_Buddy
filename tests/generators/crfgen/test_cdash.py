from unittest.mock import MagicMock, patch

import pytest

from clinical_data_study_buddy.generators.crfgen.cdash import (
    get_cdashig_variables_from_api,
)


@pytest.fixture
def mock_cdisc_library_client():
    """Mocks the CDISC library client and its API calls."""
    with patch("cdisc_library_client.client.AuthenticatedClient") as mock_client:
        yield mock_client


def test_get_cdashig_variables_from_api_with_pagination(
    mock_cdisc_library_client, monkeypatch
):
    """
    Tests that get_cdashig_variables_from_api correctly handles pagination
    and fetches all variables across multiple pages.
    """
    monkeypatch.setenv("CDISC_PRIMARY_KEY", "test_key")

    # Mock the domains response
    mock_domains_response = MagicMock()
    mock_domains_response.field_links.domains = [
        MagicMock(href="/mdr/cdashig/v2.3/domains/AE")
    ]

    # Mock the fields response for two pages
    mock_fields_response_page1 = MagicMock()
    mock_fields_response_page1.field_links.fields = [
        MagicMock(href=f"/mdr/cdashig/v2.3/domains/AE/fields/field_{i}")
        for i in range(10)
    ]

    mock_fields_response_page2 = MagicMock()
    mock_fields_response_page2.field_links.fields = [
        MagicMock(href=f"/mdr/cdashig/v2.3/domains/AE/fields/field_{i}")
        for i in range(10, 15)
    ]

    # Mock the field details response
    def mock_get_field_details(client, version, domain, field, **kwargs):
        field_details = MagicMock()
        field_details.name = field
        field_details.ordinal = 1
        field_details.prompt = "Test Prompt"
        field_details.label = "Test Label"
        field_details.completion_instructions = "Test Instructions"
        field_details.simple_datatype = "Text"
        field_details.implementation_notes = "Test Notes"
        field_details.additional_properties = {}
        return field_details

    with patch(
        "cdisc_library_client.api.cdash_implementation_guide_cdashig.get_mdr_cdashig_version_domains.sync"
    ) as mock_get_domains, patch(
        "cdisc_library_client.api.cdash_implementation_guide_cdashig.get_mdr_cdashig_version_domains_domain_fields.sync"
    ) as mock_get_fields, patch(
        "cdisc_library_client.api.cdash_implementation_guide_cdashig.get_mdr_cdashig_version_domains_domain_fields_field.sync"
    ) as mock_get_field_details_sync:

        mock_get_domains.return_value = mock_domains_response
        mock_get_fields.side_effect = [
            mock_fields_response_page1,
            mock_fields_response_page2,
            MagicMock(field_links=MagicMock(fields=[])),
        ]
        mock_get_field_details_sync.side_effect = mock_get_field_details

        df = get_cdashig_variables_from_api("v2.3")

        assert len(df) == 15
        assert df["Variable"].tolist() == [f"field_{i}" for i in range(15)]
