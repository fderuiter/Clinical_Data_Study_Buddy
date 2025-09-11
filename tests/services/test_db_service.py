from clinical_data_study_buddy.services.db_service import DBService

def test_db_service_init():
    """
    Tests that the DBService is initialized correctly.
    """
    db_service = DBService("test_connection_string")
    assert db_service.connection_string == "test_connection_string"

def test_db_service_connect_disconnect(capsys):
    """
    Tests that the connect and disconnect methods run without error.
    """
    db_service = DBService("test_connection_string")
    db_service.connect()
    captured = capsys.readouterr()
    assert captured.out == "Connecting to database at test_connection_string...\n"
    db_service.disconnect()
    captured = capsys.readouterr()
    assert captured.out == "Disconnecting from database...\n"
