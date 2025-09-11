"""
This module defines the data structures (schema) for representing Case Report Forms (CRFs)
using Pydantic models. These models are based on the CDISC CDASH standard.
"""
from __future__ import annotations

import json
import pathlib
from typing import Iterable, Literal, Optional

from pydantic import BaseModel, Field, field_validator
from pydantic.config import ConfigDict


class Codelist(BaseModel):
    """
    Represents a reference to an external controlled-terminology codelist.

    Attributes:
        nci_code (str): The NCI code for the codelist.
        href (str): A URL link to the codelist.
    """

    nci_code: str = Field(..., pattern=r"^C\d+$")
    href: str


class DataType(str):
    """
    Represents a CDASH data type.

    This class is a custom string type that is validated against a set of
    allowed CDASH data types.
    """
    # Not using Enum to keep it open; we validate later

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        from pydantic_core import core_schema

        return core_schema.no_info_plain_validator_function(cls)


ALLOWED_DT = {"text", "integer", "float", "date", "datetime", "boolean"}


class FieldDef(BaseModel):
    """
    Represents a definition for a single field in a CRF.

    This class models a single field or question in a Case Report Form,
    based on the CDISC CDASH standard.

    Attributes:
        oid (str): The object identifier for the field.
        prompt (str): The text prompt or question for the field.
        datatype (DataType): The data type of the field.
        cdash_var (str): The CDASH variable name.
        codelist (Optional[Codelist]): A reference to a codelist, if applicable.
        control (Optional[Literal["radio", "checkbox"]]): The type of input control.
        range_check (Optional[dict]): A dictionary defining a range check.
    """
    oid: str
    prompt: str
    datatype: DataType
    cdash_var: str
    length: Optional[int] = None
    codelist: Optional[Codelist] = None
    control: Optional[Literal["radio", "checkbox"]] = None
    range_check: Optional[dict] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Extra validation step
    @field_validator("datatype", mode="before")
    @classmethod
    def validate_datatype(cls, value: str) -> str:
        """
        Validates that the datatype is one of the allowed values.

        Args:
            value (str): The datatype string to validate.

        Returns:
            str: The validated datatype string in lowercase.

        Raises:
            ValueError: If the datatype is not in the allowed set.
        """
        if value.lower() not in ALLOWED_DT:
            raise ValueError(f"Datatype {value} not in {ALLOWED_DT}")
        return value.lower()


class Form(BaseModel):
    """
    Represents a definition for a CRF form.

    This class models a Case Report Form, which is a collection of fields,
    based on the CDISC CDASH standard.

    Attributes:
        title (str): The title of the form.
        domain (str): The two-letter domain code for the form.
        scenario (Optional[str]): The scenario, if applicable.
        fields (list[FieldDef]): A list of field definitions for the form.
    """
    title: str
    domain: str
    scenario: Optional[str] = None
    fields: list[FieldDef]

    def field_oids(self) -> list[str]:
        """
        Returns a list of all field OIDs in the form.

        Returns:
            list[str]: A list of the object identifiers (OIDs) for all fields.
        """
        return [f.oid for f in self.fields]


def dump_forms(forms: Iterable[Form], path: str | pathlib.Path):
    """
    Dumps a collection of Form objects to a JSON file.

    Args:
        forms (Iterable[Form]): An iterable of Form objects to be dumped.
        path (str | pathlib.Path): The path to the output JSON file.
    """
    data = [f.model_dump() for f in forms]
    pathlib.Path(path).write_text(json.dumps(data, indent=2))


def load_forms(path: str | pathlib.Path) -> list[Form]:
    """
    Loads a list of Form objects from a JSON file.

    Args:
        path (str | pathlib.Path): The path to the input JSON file.

    Returns:
        list[Form]: A list of Form objects loaded from the file.
    """
    raw = json.loads(pathlib.Path(path).read_text())
    return [Form(**d) for d in raw]
