from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class TFL(BaseModel):
    """
    A Pydantic model representing a Table, Figure, or Listing (TFL).

    This class serves as a base model for different types of TFLs,
    providing common attributes for identification, description, data,
    and styling.

    Attributes:
        id (str): The unique ID of the TFL.
        title (str): The title of the TFL.
        description (Optional[str]): A description of the TFL.
        data (Optional[List[Dict]]): The data for the TFL.
        style (Optional[Dict]): The style options for the TFL.
        domain (Optional[str]): The domain of the TFL.
    """

    id: str = Field(..., description="The unique ID of the TFL.")
    title: str = Field(..., description="The title of the TFL.")
    description: Optional[str] = Field(None, description="A description of the TFL.")
    data: Optional[List[Dict]] = Field(None, description="The data for the TFL.")
    style: Optional[Dict] = Field(None, description="The style options for the TFL.")
    domain: Optional[str] = Field(None, description="The domain of the TFL.")
