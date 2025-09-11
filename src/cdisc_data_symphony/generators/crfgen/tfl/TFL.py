from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class TFL(BaseModel):
    """A base class for Tables, Figures, and Listings."""
    id: str = Field(..., description="The unique ID of the TFL.")
    title: str = Field(..., description="The title of the TFL.")
    description: Optional[str] = Field(None, description="A description of the TFL.")
    data: Optional[List[Dict]] = Field(None, description="The data for the TFL.")
    style: Optional[Dict] = Field(None, description="The style options for the TFL.")
    domain: Optional[str] = Field(None, description="The domain of the TFL.")
