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
from cdisc_generators.data_generator import DataGenerator
from cdisc_library_client.harvest import harvest
from cdisc_generators.crfgen.utils import get_api_key
import pandas as pd
from cdisc_generators.raw_dataset_package import generate_raw_dataset_package
from cdisc_generators.analysisgen.generator import AnalysisGenerator
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


class AnalysisCodeRequest(BaseModel):
    language: str
    dataset_path: str
    output_type: str
    treatment_var: str


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/api/generate-synthetic-data")
async def generate_synthetic_data_endpoint(request: SyntheticDataRequest):
    # For now, save the generated data to a fixed directory
    output_dir = pathlib.Path("output/ui_generated_data")
    output_dir.mkdir(parents=True, exist_ok=True)

    api_key = get_api_key()
    forms = harvest(api_key, ig_filter=request.dataset_type)
    domain_form = next((f for f in forms if f.domain == request.domain), None)
    if not domain_form:
        return {"message": f"Domain {request.domain} not found"}

    generator = DataGenerator(domain_form)
    dataset = generator.generate(request.num_subjects)

    output_file = output_dir / f"{request.domain}.csv"
    df = pd.DataFrame(dataset)
    df.to_csv(output_file, index=False)

    return {"message": "Dataset generated successfully", "file_path": str(output_file)}


@app.post("/api/generate-raw-dataset-package")
async def generate_raw_dataset_package_endpoint(request: RawDatasetRequest):
    output_dir = pathlib.Path("output/ui_generated_data")
    output_dir.mkdir(parents=True, exist_ok=True)

    generate_raw_dataset_package(
        num_subjects=request.num_subjects,
        therapeutic_area=request.therapeutic_area,
        domains=request.domains,
        study_story=request.study_story,
        output_dir=str(output_dir),
        output_format=request.output_format,
    )
    # The package is a zip file, so we need to construct the expected path
    zip_filename = "edc_raw_datasets.zip"
    file_path = output_dir / zip_filename
    return {"message": "Raw dataset package generated successfully", "file_path": str(file_path)}


@app.post("/api/generate-analysis-code")
async def generate_analysis_code_endpoint(request: AnalysisCodeRequest):
    output_dir = pathlib.Path("output/ui_generated_data")
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        generator = AnalysisGenerator(
            language=request.language,
            dataset=request.dataset_path,
            output_type=request.output_type,
            treatment_var=request.treatment_var
        )
        code = generator.generate_code()
        output_filename = f"analysis.{request.language}"
        file_path = output_dir / output_filename
        with open(file_path, "w") as f:
            f.write(code)
        return {"message": "Analysis code generated successfully", "file_path": str(file_path)}
    except Exception as e:
        return {"message": f"Error generating analysis code: {e}"}
