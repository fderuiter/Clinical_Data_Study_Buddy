"""
This module provides the API router for analysis-related endpoints.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from clinical_data_study_buddy.web.services import analysis_service

router = APIRouter()


class AnalysisCodeRequest(BaseModel):
    """
    A Pydantic model for the analysis code generation request.

    Attributes:
        language (str): The programming language for the analysis code.
        dataset_path (str): The path to the dataset file.
        output_type (str): The type of analysis output to generate.
        treatment_var (str): The name of the treatment variable.
    """
    language: str
    dataset_path: str
    output_type: str
    treatment_var: str


@router.post("/api/generate-analysis-code")
async def generate_analysis_code_endpoint(request: AnalysisCodeRequest):
    """
    An API endpoint for generating analysis code.

    This endpoint receives a request with analysis parameters, calls the
    analysis service to generate the code, and returns the path to the
    generated file.

    Args:
        request (AnalysisCodeRequest): The request body containing the
                                       analysis parameters.

    Returns:
        dict: A dictionary with a success message and the path to the file.

    Raises:
        HTTPException: If an error occurs during code generation.
    """
    try:
        file_path = analysis_service.create_analysis_code(
            request.language,
            request.dataset_path,
            request.output_type,
            request.treatment_var,
        )
        return {"message": "Analysis code generated successfully", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating analysis code: {e}")
