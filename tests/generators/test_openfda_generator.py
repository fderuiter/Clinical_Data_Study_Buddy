import io
import csv
import json
from unittest.mock import patch
from clinical_data_study_buddy.generators.openfda import output_csv, populate_crf

def test_output_csv():
    """
    Tests that output_csv writes data correctly.
    """
    output = io.StringIO()
    writer = csv.writer(output)
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    output_csv(data, writer)
    output.seek(0)
    reader = csv.reader(output)
    assert next(reader) == ["a", "b"]
    assert next(reader) == ["1", "2"]
    assert next(reader) == ["3", "4"]

def test_output_csv_empty():
    """
    Tests that output_csv does nothing for empty data.
    """
    output = io.StringIO()
    writer = csv.writer(output)
    output_csv([], writer)
    output.seek(0)
    assert output.read() == ""

@patch("clinical_data_study_buddy.generators.openfda.populate_ae_from_fda")
def test_populate_crf_ae_json(mock_populate, capsys):
    """
    Tests populate_crf for AE domain and JSON output.
    """
    mock_populate.return_value = [{"reactiontext": "headache"}]
    populate_crf("test_drug", "AE", 1, "2020-01-01", "2020-01-31", "json")
    captured = capsys.readouterr()
    assert json.loads(captured.out) == [{"reactiontext": "headache"}]

@patch("clinical_data_study_buddy.generators.openfda.populate_label_from_fda")
def test_populate_crf_label_csv(mock_populate, capsys):
    """
    Tests populate_crf for LABEL domain and CSV output.
    """
    mock_populate.return_value = {"description": ["Test description"]}
    populate_crf("test_drug", "LABEL", 1, "2020-01-01", "2020-01-31", "csv")
    captured = capsys.readouterr()
    reader = csv.reader(io.StringIO(captured.out))
    assert next(reader) == ["Field", "Value"]
    assert next(reader) == ["description", "Test description"]
