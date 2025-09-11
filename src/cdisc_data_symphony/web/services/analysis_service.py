"""
This module provides a service layer for handling analysis-related business logic.
It acts as an intermediary between the API routers and the core generation services.
"""
import pathlib
from cdisc_data_symphony.core import generation_service


def create_analysis_code(language: str, dataset_path: str, output_type: str, treatment_var: str) -> str:
    """
    Creates analysis code by calling the core generation service.

    Args:
        language (str): The programming language for the analysis code.
        dataset_path (str): The path to the dataset file.
        output_type (str): The type of analysis output to generate.
        treatment_var (str): The name of the treatment variable.

    Returns:
        str: The path to the generated analysis code file.
    """
    output_dir = pathlib.Path("output/ui_generated_data")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"analysis.{language}"
    generation_service.generate_analysis_code(
        language, dataset_path, output_type, treatment_var, output_file
    )
    return str(output_file)
