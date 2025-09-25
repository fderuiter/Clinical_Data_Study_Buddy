"""
This module serves as the main entry point for the Clinical Data Study Buddy web
application. It initializes the FastAPI application, mounts static files, sets up
Jinja2 templates, and includes the API routers for different functionalities.
"""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Get the absolute path to the project root
project_root = Path(__file__).resolve().parents[3]

# Mount static files and templates using absolute paths
app.mount(
    "/static",
    StaticFiles(directory=project_root / "src/clinical_data_study_buddy/web/static"),
    name="static",
)
templates = Jinja2Templates(directory=project_root / "templates/ui")


from clinical_data_study_buddy.web.routers import (  # noqa: E402
    analysis,
    data_generation,
)


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
