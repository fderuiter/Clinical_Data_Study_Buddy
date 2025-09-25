"""
This module provides services for generating standardized filenames and bookmarks.
"""

from clinical_data_study_buddy.generators.tfl.models import TFL


def generate_filename(tfl: TFL, extension: str = "docx") -> str:
    """
    Generates a standardized filename for a TFL.

    Example:
        A TFL with shell_id "T14.1.1" will result in the filename "t14-1-1.docx".

    Args:
        tfl (TFL): The TFL object.
        extension (str): The file extension to use. Defaults to "docx".

    Returns:
        str: The generated filename.
    """
    filename_base = tfl.shell_id.lower().replace(".", "-")
    return f"{filename_base}.{extension}"


def generate_bookmark(tfl: TFL) -> str:
    """
    Generates a standardized bookmark string for a TFL.

    Example:
        A TFL with shell_id "T14.1.1" will result in the bookmark "T14_1_1".

    Args:
        tfl (TFL): The TFL object.

    Returns:
        str: The generated bookmark string.
    """
    return tfl.shell_id.replace(".", "_")
