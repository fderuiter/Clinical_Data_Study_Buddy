"""
This module provides a service layer for handling data generation business logic.
It acts as an intermediary between the API routers and the core generation services.
"""
import pathlib
from typing import List
from clinical_data_study_buddy.core import generation_service


def create_synthetic_data(dataset_type: str, domain: str, num_subjects: int, therapeutic_area: str, data_format: str) -> str:
    """
    Creates a single synthetic dataset by calling the core generation service.

    Note: This function currently uses a hardcoded version "1-0".

    Args:
        dataset_type (str): The type of dataset to generate.
        domain (str): The domain for the dataset.
        num_subjects (int): The number of subjects.
        therapeutic_area (str): The therapeutic area.
        data_format (str): The desired data format.

    Returns:
        str: The path to the generated dataset file.
    """
    output_dir = pathlib.Path("output/ui_generated_data")
    output_dir.mkdir(parents=True, exist_ok=True)
    return generation_service.generate_synthetic_data(
        dataset_type, "1-0", domain, num_subjects, output_dir
    )


def create_raw_dataset_package(num_subjects: int, therapeutic_area: str, domains: List[str], study_story: str, output_format: str) -> str:
    """
    Creates a raw dataset package by calling the core generation service.

    Args:
        num_subjects (int): The number of subjects.
        therapeutic_area (str): The therapeutic area.
        domains (List[str]): A list of domains to include.
        study_story (str): The study story to simulate.
        output_format (str): The desired output format.

    Returns:
        str: The path to the generated zip file.
    """
    output_dir = pathlib.Path("output/ui_generated_data")
    output_dir.mkdir(parents=True, exist_ok=True)
    generation_service.generate_edc_raw_dataset_package(
        num_subjects, therapeutic_area, domains, study_story, output_dir, output_format
    )
    zip_filename = "edc_raw_datasets.zip"
    return str(output_dir / zip_filename)
