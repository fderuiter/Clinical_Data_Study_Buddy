import unittest
from clinical_data_study_buddy.services.db_service import DBService

# The tests for this service are basic because the implementation
# is a placeholder. More meaningful tests will be added when the
# database service is implemented.

class TestDBService(unittest.TestCase):
    def test_init(self):
        # Arrange
        connection_string = "test_connection_string"

        # Act
        db_service = DBService(connection_string)

        # Assert
        self.assertEqual(db_service.connection_string, connection_string)

    def test_connect_disconnect(self):
        # Arrange
        connection_string = "test_connection_string"
        db_service = DBService(connection_string)

        # Act & Assert
        # We are just checking that these methods can be called without error
        try:
            db_service.connect()
            db_service.disconnect()
        except Exception as e:
            self.fail(f"DBService connect/disconnect raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
