"""
This module serves as the main entry point for the Clinical Data Study Buddy web
application. It initializes the FastAPI application, mounts static files, sets up
Jinja2 templates, and includes the API routers for different functionalities.
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Get the absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Mount static files and templates using absolute paths
app.mount("/static", StaticFiles(directory=os.path.join(project_root, "src/clinical_data_study_buddy/web/static")), name="static")
templates = Jinja2Templates(directory=os.path.join(project_root, "templates/ui"))


from clinical_data_study_buddy.web.routers import data_generation, analysis


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main index page of the web application.

    Args:
        request (Request): The incoming request object.

    Returns:
        TemplateResponse: The rendered index.html template.
    """
    return templates.TemplateResponse(request=request, name="index.html")


app.include_router(data_generation.router)
app.include_router(analysis.router)
