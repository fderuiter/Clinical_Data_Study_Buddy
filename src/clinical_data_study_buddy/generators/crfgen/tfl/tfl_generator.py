from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from ..exporter.registry import get as get_exporter
from .figures import Figure
from .listings import Listing
from .tables import Table
from .TFL import TFL


class TFLGenerator:
    """
    Orchestrates the generation of Tables, Figures, and Listings (TFLs).
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the TFLGenerator with a configuration dictionary.

        Args:
            config: A dictionary containing the configuration for TFL generation.
                    Expected keys:
                    - 'tfls': A list of TFL definitions.
                    - 'output_dir': The directory to save the generated files.
                    - 'output_formats': A list of output formats (e.g., 'docx', 'pdf').
                    - 'data_path': The path to the directory containing synthetic data.
                    - 'style': Global style options.
        """
        self.tfls_config = config.get("tfls", [])
        self.output_dir = Path(config.get("output_dir", "artefacts/tfls"))
        self.output_formats = config.get("output_formats", ["docx"])
        self.data_path = config.get("data_path")
        self.global_style = config.get("style", {})
        self.tfls: List[TFL] = []
        self.data: Dict[str, pd.DataFrame] = {}

    def _load_data(self):
        """
        Loads synthetic data from CSV files.
        """
        if self.data_path:
            data_dir = Path(self.data_path)
            if data_dir.is_dir():
                for csv_file in data_dir.glob("*.csv"):
                    domain = csv_file.stem
                    self.data[domain] = pd.read_csv(csv_file)
            else:
                print(f"Warning: Data path '{self.data_path}' is not a directory.")

    def _create_tfl_objects(self):
        """
        Creates TFL objects from the configuration.
        """
        for tfl_config in self.tfls_config:
            tfl_type = tfl_config.get("type")
            domain = tfl_config.get("domain")
            data = self.data.get(domain) if domain else None
            if data is not None:
                tfl_config["data"] = data.to_dict(orient="records")

            # Combine global and tfl-specific styles
            tfl_style = self.global_style.copy()
            tfl_style.update(tfl_config.get("style", {}))
            tfl_config["style"] = tfl_style

            if tfl_type == "table":
                self.tfls.append(Table(**tfl_config))
            elif tfl_type == "figure":
                self.tfls.append(Figure(**tfl_config))
            elif tfl_type == "listing":
                self.tfls.append(Listing(**tfl_config))
            else:
                print(f"Warning: Unknown TFL type '{tfl_type}'. Skipping.")

    def generate(self):
        """
        Generates the TFLs based on the configuration.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._load_data()
        self._create_tfl_objects()

        for tfl in self.tfls:
            print(f"Generating TFL: {tfl.id} - {tfl.title}")
            for fmt in self.output_formats:
                print(f"  - Exporting to {fmt}...")
                exporter = get_exporter(fmt)
                if exporter:
                    # The exporter expects a sequence of forms, so we wrap the tfl in a list
                    exporter([tfl], self.output_dir, style=tfl.style)
                else:
                    print(f"Warning: Exporter for format '{fmt}' not found.")

        print("TFL generation complete.")
