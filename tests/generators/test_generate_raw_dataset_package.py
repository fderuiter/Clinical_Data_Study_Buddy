import zipfile
from pathlib import Path
import pandas as pd
import tempfile

from clinical_data_study_buddy.generators.raw_dataset_package import generate_raw_dataset_package

def test_generate_raw_dataset_package():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        data = {"DM": pd.DataFrame({"USUBJID": [1, 2, 3]})}
        generate_raw_dataset_package(data, tmpdir_path)

        zip_path = tmpdir_path / "datasets.zip"
        assert zip_path.exists()

        with zipfile.ZipFile(zip_path, "r") as zf:
            assert "DM.csv" in zf.namelist()
            zf.extractall(tmpdir_path / "unzipped")

        extracted_csv_path = tmpdir_path / "unzipped" / "DM.csv"
        assert extracted_csv_path.exists()

        df = pd.read_csv(extracted_csv_path)
        pd.testing.assert_frame_equal(df, data["DM"])
