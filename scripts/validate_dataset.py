import argparse
from pathlib import Path
import pandas as pd
import openpyxl


def validate_dataset(spec_path: str, dataset_path: str):
    """
    Validates a dataset against a specification file.
    """
    spec_path = Path(spec_path)
    dataset_path = Path(dataset_path)

    # Extract domain from dataset filename, assuming format like sdtm_dm_...
    try:
        _, domain, _ = dataset_path.stem.split("_", 2)
        domain = domain.upper()
    except ValueError:
        print(
            f"Invalid dataset filename format: {dataset_path.name}. Expected '<product>_<domain>_<timestamp>.csv'."
        )
        return

    print(f"Validating dataset {dataset_path.name} against spec {spec_path.name}")

    # Load the spec for the given domain
    try:
        spec_df = pd.read_excel(spec_path, sheet_name=domain)
    except ValueError:
        print(f"Sheet '{domain}' not found in the specification file.")
        return

    # Load the dataset, keeping all columns as strings to avoid type inference issues
    dataset_df = pd.read_csv(dataset_path, dtype=str)

    # --- Validation Checks ---
    validation_warnings = []
    validation_errors = []

    # 1. Check for missing columns (as a warning)
    spec_columns = spec_df["Variable Name"].tolist()
    dataset_columns = dataset_df.columns.tolist()
    missing_columns = set(spec_columns) - set(dataset_columns)
    if missing_columns:
        validation_warnings.append(f"Missing columns in dataset that are in the spec: {', '.join(missing_columns)}")

    # 2. Check for extra columns
    extra_columns = set(dataset_columns) - set(spec_columns)
    if extra_columns:
        validation_errors.append(f"Extra columns in dataset that are not in the spec: {', '.join(extra_columns)}")

    # 3. Check data types
    for _, row in spec_df.iterrows():
        col_name = row["Variable Name"]
        spec_type = row["Data Type"]
        if col_name in dataset_df.columns:
            # Since we read everything as string, we can try to cast to the spec type
            if spec_type == "Num":
                try:
                    pd.to_numeric(dataset_df[col_name].dropna())
                except (ValueError, TypeError):
                    validation_errors.append(f"Data type error in column '{col_name}': Expected a numeric type.")
            # For Char, as long as it can be represented as a string, it's fine.
            # Since we loaded with dtype=str, this check is implicitly passed.

    # --- Report Results ---
    if validation_errors:
        print("\nValidation Failed:")
        for error in validation_errors:
            print(f"- {error}")
    else:
        print("\nValidation Successful: Dataset conforms to the specification.")

    if validation_warnings:
        print("\nValidation Warnings:")
        for warning in validation_warnings:
            print(f"- {warning}")



def main():
    parser = argparse.ArgumentParser(
        description="Validate a dataset against an Excel specification file."
    )
    parser.add_argument(
        "--spec-file",
        required=True,
        help="Path to the Excel specification file.",
    )
    parser.add_argument(
        "--dataset-file",
        required=True,
        help="Path to the dataset file (e.g., a CSV).",
    )
    args = parser.parse_args()
    validate_dataset(args.spec_file, args.dataset_file)


if __name__ == "__main__":
    main()
