"""
This module provides the TFLShellGenerator class, which is responsible for
generating simple TFL shell documents.
"""


class TFLShellGenerator:
    """
    A class for generating simple TFL shell documents.

    This class takes a TFL specification and generates a basic Markdown
    document that serves as a shell for the TFLs.
    """
    def __init__(self, spec):
        """
        Initializes the TFLShellGenerator.

        Args:
            spec (str): The TFL specification.
        """
        self.spec = spec

    def generate(self):
        """
        Generates a simple TFL shell document as a Markdown string.

        Returns:
            str: The generated TFL shell document.
        """
        return f"""\
# TFL Shell Document

This is a shell document for the following TFLs:

{self.spec}
"""
