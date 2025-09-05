import pathlib
from cdisc_data_symphony.core import generation_service


def create_analysis_code(language: str, dataset_path: str, output_type: str, treatment_var: str):
    output_dir = pathlib.Path("output/ui_generated_data")
    output_file = output_dir / f"analysis.{language}"
    return generation_service.generate_analysis_code(
        language, dataset_path, output_type, treatment_var, output_file
    )
