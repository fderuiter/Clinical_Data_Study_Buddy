"""
This module provides the API router for data generation endpoints.
"""
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from clinical_data_study_buddy.web.services import data_generation_service

router = APIRouter()


class SyntheticDataRequest(BaseModel):
    """
    A Pydantic model for the synthetic data generation request.

    Attributes:
        dataset_type (str): The type of dataset to generate.
        domain (str): The domain for the dataset.
        num_subjects (int): The number of subjects.
        therapeutic_area (str): The therapeutic area.
        data_format (str): The desired data format (e.g., "csv").
    """
    dataset_type: str
    domain: str
    num_subjects: int
    therapeutic_area: str
    data_format: str


class RawDatasetRequest(BaseModel):
    """
    A Pydantic model for the raw dataset package generation request.

    Attributes:
        num_subjects (int): The number of subjects.
        therapeutic_area (str): The therapeutic area.
        domains (List[str]): A list of domains to include.
        study_story (str): The study story to simulate.
        output_format (str): The desired output format (e.g., "csv").
    """
    num_subjects: int
    therapeutic_area: str
    domains: List[str]
    study_story: str
    output_format: str


@router.post("/api/generate-synthetic-data")
async def generate_synthetic_data_endpoint(request: SyntheticDataRequest):
    """
    An API endpoint for generating a single synthetic dataset.

    This endpoint receives a request with data generation parameters, calls the
    data generation service, and returns the path to the generated file.

    Args:
        request (SyntheticDataRequest): The request body containing the
                                        data generation parameters.

    Returns:
        dict: A dictionary with a success message and the path to the file.

    Raises:
        HTTPException: If an error occurs during data generation.
    """
    try:
        file_path = data_generation_service.create_synthetic_data(
            request.dataset_type,
            request.domain,
            request.num_subjects,
            request.therapeutic_area,
            request.data_format,
        )
        return {"message": "Dataset generated successfully", "file_path": file_path}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating synthetic data: {e}")


@router.post("/api/generate-raw-dataset-package")
async def generate_raw_dataset_package_endpoint(request: RawDatasetRequest):
    """
    An API endpoint for generating a raw dataset package.

    This endpoint receives a request with parameters for generating a full
    study dataset package, calls the data generation service, and returns
    the path to the generated zip file.

    Args:
        request (RawDatasetRequest): The request body containing the package
                                     generation parameters.

    Returns:
        dict: A dictionary with a success message and the path to the file.

    Raises:
        HTTPException: If an error occurs during package generation.
    """
    try:
        file_path = data_generation_service.create_raw_dataset_package(
            request.num_subjects,
            request.therapeutic_area,
            request.domains,
            request.study_story,
            request.output_format,
        )
        return {"message": "Raw dataset package generated successfully", "file_path": file_path}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating raw dataset package: {e}")
