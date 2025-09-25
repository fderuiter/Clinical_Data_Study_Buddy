from typing import Optional

from pydantic import BaseModel, Field


class StudyConfig(BaseModel):
    """
    A Pydantic model for study configuration.

    Attributes:
        study_id (str): The ID of the study.
        protocol_id (Optional[str]): The protocol ID of the study.
        protocol_title (Optional[str]): The title of the protocol.
    """

    study_id: str = Field(..., description="The ID of the study.")
    protocol_id: Optional[str] = Field(
        None, description="The protocol ID of the study."
    )
    protocol_title: Optional[str] = Field(
        None, description="The title of the protocol."
    )
