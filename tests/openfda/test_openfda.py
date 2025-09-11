import pytest
from unittest.mock import AsyncMock

from clinical_data_study_buddy.generators.crfgen.openfda.client import OpenFDAClient
from clinical_data_study_buddy.generators.crfgen.openfda.query import term_query, range_query, count_query, paging_query

def test_term_query():
    assert term_query("field", "term") == 'field:"term"'

def test_range_query():
    assert range_query("field", "start", "end") == 'field:[start+TO+end]'

def test_count_query():
    assert count_query("field") == 'field.exact'
    assert count_query("field.exact") == 'field.exact'

def test_paging_query():
    assert paging_query(100, 50) == {"limit": 100, "skip": 50}
    with pytest.raises(ValueError):
        paging_query(limit=1001)
    with pytest.raises(ValueError):
        paging_query(skip=25001)

from clinical_data_study_buddy.generators.crfgen.openfda.devices.udi import UDIAccessor
from clinical_data_study_buddy.generators.crfgen.openfda.devices.event import MAUDEAccessor
from clinical_data_study_buddy.generators.crfgen.openfda.devices.recall import RecallAccessor
from clinical_data_study_buddy.generators.crfgen.openfda.devices.enforcement import EnforcementAccessor
from clinical_data_study_buddy.generators.crfgen.openfda.devices.classification import ClassificationAccessor
from clinical_data_study_buddy.generators.crfgen.openfda.devices.k510 import K510Accessor
from clinical_data_study_buddy.generators.crfgen.openfda.devices.pma import PMAAccessor
from clinical_data_study_buddy.generators.crfgen.openfda.devices.reglist import RegListAccessor

import httpx


@pytest.mark.asyncio
async def test_openfda_client_get():
    client = OpenFDAClient()
    client.client = AsyncMock()
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"results": []}
    client.client.get.return_value = mock_response

    await client.get("/device/udi.json")

    client.client.get.assert_called_once()
    await client.close()


from unittest.mock import patch


@pytest.mark.asyncio
async def test_openfda_client_get_error():
    client = OpenFDAClient()
    client.client = AsyncMock()
    mock_response = AsyncMock()
    mock_response.status_code = 400
    mock_response.request = httpx.Request("GET", "http://test.com")
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Bad Request", request=mock_response.request, response=mock_response
    )
    client.client.get.return_value = mock_response

    with pytest.raises(httpx.HTTPStatusError):
        # Call the wrapped function directly to bypass the retry decorator
        await client.get.__wrapped__(client, "/device/udi.json")

    client.client.get.assert_called_once()
    await client.close()

@pytest.mark.asyncio
async def test_udi_accessor_fetch():
    client = OpenFDAClient()
    client.get = AsyncMock()
    client.get.return_value.json.return_value = {
        "results": [
            {
                "di": "00812345678901",
                "brand_name": "Test Device",
                "company_name": "Test Company"
            }
        ]
    }

    accessor = UDIAccessor(client)
    results = await accessor.fetch(search="test")

    assert len(results) == 1
    assert results[0].di == "00812345678901"
    client.get.assert_called_once_with("/device/udi.json", params={"search": "test"})

@pytest.mark.asyncio
async def test_maude_accessor_fetch():
    client = OpenFDAClient()
    client.get = AsyncMock()
    client.get.return_value.json.return_value = {
        "results": [
            {
                "mdr_report_key": "12345",
                "device": [{"brand_name": "Test Device"}]
            }
        ]
    }

    accessor = MAUDEAccessor(client)
    results = await accessor.fetch(search="test")

    assert len(results) == 1
    assert results[0].mdr_report_key == "12345"
    client.get.assert_called_once_with("/device/event.json", params={"search": "test"})

@pytest.mark.asyncio
async def test_recall_accessor_fetch():
    client = OpenFDAClient()
    client.get = AsyncMock()
    client.get.return_value.json.return_value = {
        "results": [
            {
                "recall_number": "R12345",
                "product_description": "Test Recall"
            }
        ]
    }

    accessor = RecallAccessor(client)
    results = await accessor.fetch(search="test")

    assert len(results) == 1
    assert results[0].recall_number == "R12345"
    client.get.assert_called_once_with("/device/recall.json", params={"search": "test"})

@pytest.mark.asyncio
async def test_enforcement_accessor_fetch():
    client = OpenFDAClient()
    client.get = AsyncMock()
    client.get.return_value.json.return_value = {
        "results": [
            {
                "recall_number": "E12345",
                "product_description": "Test Enforcement"
            }
        ]
    }

    accessor = EnforcementAccessor(client)
    results = await accessor.fetch(search="test")

    assert len(results) == 1
    assert results[0].recall_number == "E12345"
    client.get.assert_called_once_with("/device/enforcement.json", params={"search": "test"})

@pytest.mark.asyncio
async def test_classification_accessor_fetch():
    client = OpenFDAClient()
    client.get = AsyncMock()
    client.get.return_value.json.return_value = {
        "results": [
            {
                "product_code": "ABC",
                "device_name": "Test Classification"
            }
        ]
    }

    accessor = ClassificationAccessor(client)
    results = await accessor.fetch(search="test")

    assert len(results) == 1
    assert results[0].product_code == "ABC"
    client.get.assert_called_once_with("/device/classification.json", params={"search": "test"})

@pytest.mark.asyncio
async def test_k510_accessor_fetch():
    client = OpenFDAClient()
    client.get = AsyncMock()
    client.get.return_value.json.return_value = {
        "results": [
            {
                "k_number": "K123456",
                "applicant": "Test Applicant"
            }
        ]
    }

    accessor = K510Accessor(client)
    results = await accessor.fetch(search="test")

    assert len(results) == 1
    assert results[0].k_number == "K123456"
    client.get.assert_called_once_with("/device/510k.json", params={"search": "test"})

@pytest.mark.asyncio
async def test_pma_accessor_fetch():
    client = OpenFDAClient()
    client.get = AsyncMock()
    client.get.return_value.json.return_value = {
        "results": [
            {
                "pma_number": "P123456",
                "applicant": "Test Applicant"
            }
        ]
    }

    accessor = PMAAccessor(client)
    results = await accessor.fetch(search="test")

    assert len(results) == 1
    assert results[0].pma_number == "P123456"
    client.get.assert_called_once_with("/device/pma.json", params={"search": "test"})

@pytest.mark.asyncio
async def test_reglist_accessor_fetch():
    client = OpenFDAClient()
    client.get = AsyncMock()
    client.get.return_value.json.return_value = {
        "results": [
            {
                "fei_number": "1234567890",
                "owner_operator": "Test Owner"
            }
        ]
    }

    accessor = RegListAccessor(client)
    results = await accessor.fetch(search="test")

    assert len(results) == 1
    assert results[0].fei_number == "1234567890"
    client.get.assert_called_once_with("/device/registrationlisting.json", params={"search": "test"})
