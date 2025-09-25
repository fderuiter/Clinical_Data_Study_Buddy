import logging

from clinical_data_study_buddy.core.logging_service import get_logger


def test_get_logger_returns_logger_instance():
    """
    Test that get_logger returns a logging.Logger instance.
    """
    logger = get_logger("test_logger")
    assert isinstance(logger, logging.Logger)


def test_get_logger_sets_name():
    """
    Test that get_logger sets the correct name for the logger.
    """
    logger_name = "my_test_logger"
    logger = get_logger(logger_name)
    assert logger.name == logger_name


def test_get_logger_sets_level():
    """
    Test that get_logger sets the correct logging level.
    """
    logger = get_logger("test_level_logger", level=logging.DEBUG)
    assert logger.level == logging.DEBUG


def test_get_logger_adds_handler_if_none_exist():
    """
    Test that get_logger adds a handler if none exist.
    """
    logger_name = "handler_test_logger"
    # Ensure the logger is fresh and has no handlers
    if logger_name in logging.Logger.manager.loggerDict:
        del logging.Logger.manager.loggerDict[logger_name]

    logger = get_logger(logger_name)
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)


def test_get_logger_does_not_add_handler_if_one_exists():
    """
    Test that get_logger does not add a handler if one already exists.
    """
    logger_name = "existing_handler_logger"
    # Ensure the logger is fresh and has no handlers
    if logger_name in logging.Logger.manager.loggerDict:
        del logging.Logger.manager.loggerDict[logger_name]

    logger = logging.getLogger(logger_name)
    dummy_handler = logging.NullHandler()
    logger.addHandler(dummy_handler)

    logger = get_logger(logger_name)
    assert len(logger.handlers) == 1
    assert logger.handlers[0] is dummy_handler
