from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from cdisc_generators_api.ui.services import data_generation_service

router = APIRouter()


class SyntheticDataRequest(BaseModel):
    dataset_type: str
    domain: str
    num_subjects: int
    therapeutic_area: str
    data_format: str

class RawDatasetRequest(BaseModel):
    num_subjects: int
    therapeutic_area: str
    domains: List[str]
    study_story: str
    output_format: str


@router.post("/api/generate-synthetic-data")
async def generate_synthetic_data_endpoint(request: SyntheticDataRequest):
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
    try:
        file_path = data_generation_service.create_raw_dataset_package(
            request.num_subjects,
            request.therapeutic_area,
            request.domains,
            request.study_story,
            request.output_format,
        )
        return {"message": "Raw dataset package generated successfully", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating raw dataset package: {e}")
