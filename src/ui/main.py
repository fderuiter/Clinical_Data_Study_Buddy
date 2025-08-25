from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Get the absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Mount static files and templates using absolute paths
app.mount("/static", StaticFiles(directory=os.path.join(project_root, "src/ui/static")), name="static")
templates = Jinja2Templates(directory=os.path.join(project_root, "src/ui/templates"))


from pydantic import BaseModel
from cdisc_generators.synthetic_data import generate_and_download_synthetic_data
from cdisc_generators.raw_dataset_package import generate_raw_dataset_package
import pathlib
from typing import List

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

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/api/generate-synthetic-data")
async def generate_synthetic_data_endpoint(request: SyntheticDataRequest):
    # For now, save the generated data to a fixed directory
    output_dir = pathlib.Path("output/ui_generated_data")
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = generate_and_download_synthetic_data(
        dataset_type=request.dataset_type,
        domain=request.domain,
        num_subjects=request.num_subjects,
        therapeutic_area=request.therapeutic_area,
        data_format=request.data_format,
        output_dir=output_dir,
    )
    return {"message": "Dataset generated successfully", "file_path": file_path}


@app.post("/api/generate-raw-dataset-package")
async def generate_raw_dataset_package_endpoint(request: RawDatasetRequest):
    output_dir = pathlib.Path("output/ui_generated_data")
    output_dir.mkdir(parents=True, exist_ok=True)

    generate_raw_dataset_package(
        num_subjects=request.num_subjects,
        therapeutic_area=request.therapeutic_area,
        domains=request.domains,
        study_story=request.study_story,
        output_dir=output_dir,
        output_format=request.output_format,
    )
    # The package is a zip file, so we need to construct the expected path
    zip_filename = "edc_raw_datasets.zip"
    file_path = output_dir / zip_filename
    return {"message": "Raw dataset package generated successfully", "file_path": str(file_path)}
