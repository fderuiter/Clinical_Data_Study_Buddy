from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from cdisc_data_symphony.web.services import analysis_service

router = APIRouter()


class AnalysisCodeRequest(BaseModel):
    language: str
    dataset_path: str
    output_type: str
    treatment_var: str


@router.post("/api/generate-analysis-code")
async def generate_analysis_code_endpoint(request: AnalysisCodeRequest):
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
