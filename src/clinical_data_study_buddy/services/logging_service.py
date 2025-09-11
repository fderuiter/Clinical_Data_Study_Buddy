"""
This module provides a centralized logging service for the application.
"""
import logging
import sys

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Gets and configures a logger.

    Args:
        name (str): The name of the logger.
        level (int): The logging level.

    Returns:
        logging.Logger: A configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
