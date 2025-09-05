import pathlib
from typing import List
from cdisc_data_symphony.core import generation_service


def create_synthetic_data(dataset_type: str, domain: str, num_subjects: int, therapeutic_area: str, data_format: str):
    output_dir = pathlib.Path("output/ui_generated_data")
    return generation_service.generate_synthetic_data(
        dataset_type, "1-0", domain, num_subjects, output_dir
    )


def create_raw_dataset_package(num_subjects: int, therapeutic_area: str, domains: List[str], study_story: str, output_format: str):
    output_dir = pathlib.Path("output/ui_generated_data")
    generation_service.generate_edc_raw_dataset_package(
        num_subjects, therapeutic_area, domains, study_story, output_dir, output_format
    )
    zip_filename = "edc_raw_datasets.zip"
    return str(output_dir / zip_filename)
