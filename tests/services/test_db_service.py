import pytest
from clinical_data_study_buddy.services.db_service import DBService


def test_db_service_init():
    """
    Test that the DBService is initialized correctly.
    """
    db_service = DBService("test_connection_string")
    assert db_service.connection_string == "test_connection_string"


def test_db_service_connect(capsys):
    """
    Test that the connect method prints the correct message.
    """
    db_service = DBService("test_connection_string")
    db_service.connect()
    captured = capsys.readouterr()
    assert captured.out == "Connecting to database at test_connection_string...\n"


def test_db_service_disconnect(capsys):
    """
    Test that the disconnect method prints the correct message.
    """
    db_service = DBService("test_connection_string")
    db_service.disconnect()
    captured = capsys.readouterr()
    assert captured.out == "Disconnecting from database...\n"
