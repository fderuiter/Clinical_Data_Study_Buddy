from pathlib import Path
from typing import Dict, List, Any
import pandas as pd

from .TFL import TFL
from .tables import Table
from .figures import Figure
from .listings import Listing
from ..exporter.registry import get as get_exporter

class TFLGenerator:
    """
    A class for orchestrating the generation of Tables, Figures, and Listings (TFLs).

    This class reads a configuration file, loads the necessary data, creates
    TFL objects, and then uses registered exporters to generate the final
    documents in various formats.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the TFLGenerator with a configuration dictionary.

        Args:
            config (Dict[str, Any]): A dictionary containing the configuration for
                                     TFL generation. Expected keys include 'tfls',
                                     'output_dir', 'output_formats', 'data_path',
                                     and 'style'.

        Raises:
            ValueError: If the 'tfls' key is missing in the config.
        """
        if "tfls" not in config:
            raise ValueError("Configuration must contain a 'tfls' key.")
        self.tfls_config = config.get("tfls", [])
        self.output_dir = Path(config.get("output_dir", "artefacts/tfls"))
        self.output_formats = config.get("output_formats", ["docx"])
        self.data_path = config.get("data_path")
        self.global_style = config.get("style", {})
        self.tfls: List[TFL] = []
        self.data: Dict[str, pd.DataFrame] = {}

    def _load_data(self) -> None:
        """
        Loads synthetic data from CSV files into a dictionary of pandas DataFrames.

        The data is loaded from the directory specified in the `data_path`
        attribute of the configuration.
        """
        if self.data_path:
            data_dir = Path(self.data_path)
            if data_dir.is_dir():
                for csv_file in data_dir.glob("*.csv"):
                    domain = csv_file.stem
                    self.data[domain] = pd.read_csv(csv_file)
            else:
                print(f"Warning: Data path '{self.data_path}' is not a directory.")

    def _create_tfl_objects(self) -> None:
        """
        Creates TFL objects (Table, Figure, Listing) from the configuration.

        This method iterates through the TFL definitions in the configuration,
        instantiates the appropriate TFL objects, and populates them with
        data and styles.
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

    def generate(self) -> None:
        """
        Generates the TFLs based on the loaded configuration.

        This is the main method that orchestrates the entire TFL generation
        process, from loading data to exporting the final documents.
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
