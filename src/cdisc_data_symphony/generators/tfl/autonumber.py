from typing import List, Dict
from .models import TFL, TFLSpec

class AutoNumberer:
    """
    Handles automatic numbering of TFLs, filenames, and bookmarks.
    """

    def __init__(self, spec: TFLSpec):
        self.spec = spec
        self.tfl_map: Dict[str, TFL] = {tfl.shell_id: tfl for tfl in spec.tfls}

    def get_tfl_by_id(self, shell_id: str) -> TFL:
        """
        Retrieves a TFL by its shell ID.
        """
        if shell_id not in self.tfl_map:
            raise ValueError(f"TFL with shell_id '{shell_id}' not found in the spec.")
        return self.tfl_map[shell_id]

    def assign_numbers(self, prefix="T14") -> TFLSpec:
        """
        Assigns sequential numbers to TFLs based on their order in the spec.
        This is a simple implementation of the T14.x.y rule.
        A more complex implementation could handle hierarchical numbering.
        """
        major = 1
        minor = 1
        for tfl in self.spec.tfls:
            # This is a naive implementation. A real one would need to parse the existing numbers
            # or have a more structured way of assigning them.
            # For now, we'll just re-number everything sequentially.
            tfl.shell_id = f"{prefix}.{major}.{minor}"
            minor += 1
        return self.spec

    @staticmethod
    def generate_filename(tfl: TFL, extension: str = "docx") -> str:
        """
        Generates a filename for a TFL based on its shell_id.
        e.g., "T14.1.1" -> "t14-1-1.docx"
        """
        filename_base = tfl.shell_id.lower().replace(".", "-")
        return f"{filename_base}.{extension}"

    @staticmethod
    def generate_bookmark(tfl: TFL) -> str:
        """
        Generates a bookmark for a TFL based on its shell_id.
        e.g., "T14.1.1" -> "T14_1_1"
        """
        return tfl.shell_id.replace(".", "_")
