import tempfile
import zipfile
from pathlib import Path

import pandas as pd


def generate_raw_dataset_package(domains: dict[str, pd.DataFrame], output_dir: Path):
    """
    Generates a raw dataset package as a zip file.

    Args:
        domains (dict[str, pd.DataFrame]): A dictionary where keys are domain names
                                           and values are pandas DataFrames.
        output_dir (Path): The directory where the final package will be saved.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        for domain, df in domains.items():
            df.to_csv(tmpdir_path / f"{domain}.csv", index=False)

        zip_path = output_dir / "datasets.zip"
        with zipfile.ZipFile(zip_path, "w") as zf:
            for file in tmpdir_path.iterdir():
                zf.write(file, file.name)
