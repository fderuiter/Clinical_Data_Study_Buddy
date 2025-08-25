class TFLShellGenerator:
    def __init__(self, spec):
        self.spec = spec

    def generate(self):
        """
        Generates a simple TFL shell document.
        """
        return f"""\
# TFL Shell Document

This is a shell document for the following TFLs:

{self.spec}
"""
