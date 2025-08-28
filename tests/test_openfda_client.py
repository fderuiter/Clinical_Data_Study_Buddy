import unittest
from unittest.mock import patch, MagicMock
from cdisc_generators_api.openfda_client import client
from cdisc_generators_api.cdisc_generators.crfgen.populators import populate_ae_from_fda, populate_label_from_fda

class TestOpenFDAClient(unittest.TestCase):

    @patch('requests.get')
    def test_get_adverse_events_single_page(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": [{"patient": {"reaction": [{"reactionmeddrapt": "Headache"}]}}]}
        mock_get.return_value = mock_response

        events = client.get_adverse_events("Aspirin", max_results=5)
        self.assertEqual(len(events), 1)
        mock_get.assert_called_with(
            "https://api.fda.gov/drug/event.json",
            params={"search": 'patient.drug.medicinalproduct:"Aspirin"', "limit": 5, "skip": 0},
            timeout=(10, 30)
        )

    @patch('requests.get')
    def test_get_adverse_events_with_date_filter(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": []}
        mock_get.return_value = mock_response

        client.get_adverse_events("Aspirin", max_results=10, start_date="20200101", end_date="20210101")
        expected_query = 'patient.drug.medicinalproduct:"Aspirin"+AND+receivedate:[20200101+TO+20210101]'
        mock_get.assert_called_with(
            "https://api.fda.gov/drug/event.json",
            params={"search": expected_query, "limit": 10, "skip": 0},
            timeout=(10, 30)
        )

    @patch('requests.get')
    def test_get_adverse_events_pagination(self, mock_get):
        # Mock two pages of results
        mock_response_page1 = MagicMock()
        mock_response_page1.json.return_value = {
            "meta": {"results": {"total": 150, "limit": 100, "skip": 0}},
            "results": [{"id": f"page1_{i}"} for i in range(100)]
        }
        mock_response_page2 = MagicMock()
        mock_response_page2.json.return_value = {
            "meta": {"results": {"total": 150, "limit": 50, "skip": 100}},
            "results": [{"id": f"page2_{i}"} for i in range(50)]
        }
        mock_get.side_effect = [mock_response_page1, mock_response_page2]

        events = client.get_adverse_events("Aspirin", max_results=150)
        self.assertEqual(len(events), 150)
        self.assertEqual(mock_get.call_count, 2)

        # Check call args for the second call
        args, kwargs = mock_get.call_args_list[1]
        self.assertEqual(kwargs['params']['skip'], 100)
        self.assertEqual(kwargs['params']['limit'], 50)


    @patch('requests.get')
    def test_get_drug_label(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": [{"id": "123", "openfda": {"brand_name": ["Aspirin"]}}]}
        mock_get.return_value = mock_response

        label = client.get_drug_label("Aspirin")
        self.assertEqual(label["id"], "123")


class TestPopulators(unittest.TestCase):

    @patch('cdisc_generators_api.openfda_client.client.get_adverse_events')
    def test_populate_ae_from_fda(self, mock_get_adverse_events):
        mock_get_adverse_events.return_value = [
            {"patient": {"reaction": [{"reactionmeddrapt": "Nausea"}]}},
        ]

        results = populate_ae_from_fda("TestDrug", max_results=5, start_date="20210101", end_date="20211231")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["reaction_term"], "Nausea")

        mock_get_adverse_events.assert_called_with(
            "TestDrug", max_results=5, start_date="20210101", end_date="20211231"
        )

    @patch('cdisc_generators_api.openfda_client.client.get_adverse_events')
    def test_populate_ae_from_fda_no_results(self, mock_get_adverse_events):
        mock_get_adverse_events.return_value = []
        results = populate_ae_from_fda("TestDrug")
        self.assertEqual(results, [])

    @patch('cdisc_generators_api.openfda_client.client.get_drug_label')
    def test_populate_label_from_fda(self, mock_get_drug_label):
        mock_get_drug_label.return_value = {
            "openfda": {
                "brand_name": ["Aspirin"],
                "generic_name": ["Aspirin"]
            },
            "indications_and_usage": ["For the relief of pain"],
            "adverse_reactions": ["Stomach bleeding"]
        }

        result = populate_label_from_fda("Aspirin")

        self.assertEqual(result["brand_name"], ["Aspirin"])
        self.assertEqual(result["indications_and_usage"], ["For the relief of pain"])
        mock_get_drug_label.assert_called_with("Aspirin")


if __name__ == '__main__':
    unittest.main()
