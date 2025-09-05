from pydantic import BaseModel, Field
from typing import Optional

class StudyConfig(BaseModel):
    study_id: str = Field(..., description="The ID of the study.")
    protocol_id: Optional[str] = Field(None, description="The protocol ID of the study.")
    protocol_title: Optional[str] = Field(None, description="The title of the protocol.")
