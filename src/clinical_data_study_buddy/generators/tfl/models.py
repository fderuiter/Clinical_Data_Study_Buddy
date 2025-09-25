"""
This module defines the Pydantic models used to represent the structure and
metadata of TFL (Tables, Figures, and Listings) specifications.
"""

from typing import List

from pydantic import BaseModel, Field


class Layout(BaseModel):
    """
    A Pydantic model representing the layout properties of a TFL.

    Attributes:
        orientation (str): The page orientation (e.g., "portrait", "landscape").
        page_size (str): The page size (e.g., "A4", "Letter").
    """

    orientation: str
    page_size: str


class TFL(BaseModel):
    """
    A Pydantic model representing a single Table, Figure, or Listing (TFL).

    Attributes:
        shell_id (str): The unique identifier for the TFL shell.
        title (str): The title of the TFL.
        population (str): The analysis population for the TFL.
        derivations (List[str]): A list of derivations used in the TFL.
        footnotes (List[str]): A list of footnotes for the TFL.
        layout (Layout): The layout properties for the TFL.
    """

    shell_id: str
    title: str
    population: str
    derivations: List[str] = Field(default_factory=list)
    footnotes: List[str] = Field(default_factory=list)
    layout: Layout


class TFLSpec(BaseModel):
    """
    A Pydantic model representing a complete TFL specification.

    Attributes:
        version (float): The version number of the specification.
        tfls (List[TFL]): A list of all TFLs included in the specification.
    """

    version: float
    tfls: List[TFL]
