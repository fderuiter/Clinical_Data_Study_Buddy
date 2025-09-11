import logging
from clinical_data_study_buddy.services.logging_service import get_logger

def test_get_logger():
    """
    Tests that get_logger returns a logger with the correct name and level.
    """
    logger = get_logger("test_logger", logging.DEBUG)
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger"
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 1

def test_get_logger_singleton():
    """
    Tests that get_logger returns the same logger instance for the same name
    and does not add duplicate handlers.
    """
    logger1 = get_logger("singleton_logger")
    assert len(logger1.handlers) == 1
    logger2 = get_logger("singleton_logger")
    assert logger1 is logger2
    assert len(logger2.handlers) == 1
