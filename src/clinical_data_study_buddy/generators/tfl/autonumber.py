from typing import List, Dict
from .models import TFL, TFLSpec

class AutoNumberer:
    """
    A class for handling the automatic numbering of TFLs, filenames, and bookmarks.

    This class takes a TFL specification and provides methods for renumbering
    TFLs according to a specified prefix and grouping logic.
    """

    def __init__(self, spec: TFLSpec):
        """
        Initializes the AutoNumberer.

        Args:
            spec (TFLSpec): The TFL specification object to be processed.
        """
        self.spec = spec
        self.tfl_map: Dict[str, TFL] = {tfl.shell_id: tfl for tfl in spec.tfls}

    def get_tfl_by_id(self, shell_id: str) -> TFL:
        """
        Retrieves a TFL by its shell ID.

        Args:
            shell_id (str): The shell ID of the TFL to retrieve.

        Returns:
            TFL: The TFL object with the specified shell ID.

        Raises:
            ValueError: If no TFL with the given shell ID is found.
        """
        if shell_id not in self.tfl_map:
            raise ValueError(f"TFL with shell_id '{shell_id}' not found in the spec.")
        return self.tfl_map[shell_id]

    def assign_numbers(self, prefix="T14") -> TFLSpec:
        """
        Assigns sequential numbers to all TFLs in the specification.

        This method implements a simple version of the T14.x.y numbering rule,
        grouping TFLs by their major number and renumbering them sequentially
        within each group.

        Args:
            prefix (str): The prefix to use for the numbering (e.g., "T14").

        Returns:
            TFLSpec: The updated TFL specification with re-numbered TFLs.
        """
        tfl_groups = {}
        # Group TFLs by major number
        for tfl in self.spec.tfls:
            major = -1 # Default group for invalid shell_ids
            try:
                parts = tfl.shell_id.split('.')
                if len(parts) == 3:
                    major = int(parts[1])
            except (ValueError, IndexError):
                pass # Keep major = -1

            if major not in tfl_groups:
                tfl_groups[major] = []
            tfl_groups[major].append(tfl)

        # Re-number TFLs within each group
        for major, tfls in sorted(tfl_groups.items()):
            minor = 1
            for tfl in tfls:
                if major == -1:
                    # For now, assign to a default major number, e.g., 99
                    # A better solution might be to raise an error or use a different logic
                    tfl.shell_id = f"{prefix}.99.{minor}"
                else:
                    tfl.shell_id = f"{prefix}.{major}.{minor}"
                minor += 1
        return self.spec
