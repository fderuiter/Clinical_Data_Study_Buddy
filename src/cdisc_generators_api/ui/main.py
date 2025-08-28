from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Get the absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Mount static files and templates using absolute paths
app.mount("/static", StaticFiles(directory=os.path.join(project_root, "src/cdisc_generators_api/ui/static")), name="static")
templates = Jinja2Templates(directory=os.path.join(project_root, "templates/ui"))


from cdisc_generators_api.ui.routers import data_generation, analysis

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

app.include_router(data_generation.router)
app.include_router(analysis.router)
