from pydantic import BaseModel, Field
from typing import List, Optional

class Layout(BaseModel):
    orientation: str
    page_size: str

class TFL(BaseModel):
    shell_id: str
    title: str
    population: str
    derivations: List[str] = Field(default_factory=list)
    footnotes: List[str] = Field(default_factory=list)
    layout: Layout

class TFLSpec(BaseModel):
    version: float
    tfls: List[TFL]
