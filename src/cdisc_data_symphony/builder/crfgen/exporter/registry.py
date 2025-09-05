"""
This module provides a registry for exporter functions.

The registry allows different exporter functions to be registered under a
specific format name (e.g., "csv", "docx"), and then retrieved by that name.
This makes it easy to add new export formats without modifying the core logic.
"""
_registry = {}


def register(name: str):
    """
    A decorator to register an exporter function for a given format name.

    Args:
        name (str): The name of the format (e.g., "pdf", "docx").

    Returns:
        A decorator function that registers the decorated function.
    """
    def decorator(fn):
        _registry[name] = fn
        return fn

    return decorator


def get(name: str):
    """
    Gets the exporter function for a given format name.

    Args:
        name (str): The name of the format.

    Returns:
        The exporter function associated with the given name, or None if not found.
    """
    return _registry.get(name)


def formats():
    """
    Returns a list of all registered format names.

    Returns:
        list: A list of strings, where each string is a registered format name.
    """
    return list(_registry.keys())
