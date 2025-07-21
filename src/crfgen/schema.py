from __future__ import annotations

from typing import Optional, Literal

from pydantic import BaseModel, Field, field_validator
from pydantic.config import ConfigDict


class Codelist(BaseModel):
    """Reference to an external controlled-terminology list."""

    nci_code: str = Field(..., pattern=r"^C\d+$")
    href: str


class DataType(str):
    """CDASH datatype subset we care about."""

    # Not using Enum to keep it open; we validate later

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        from pydantic_core import core_schema

        return core_schema.no_info_plain_validator_function(cls)


ALLOWED_DT = {"text", "integer", "float", "date", "datetime", "boolean"}


class FieldDef(BaseModel):
    oid: str
    prompt: str
    datatype: DataType
    cdash_var: str
    codelist: Optional[Codelist] = None
    control: Optional[Literal["radio", "checkbox"]] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Extra validation step
    @field_validator("datatype", mode="before")
    @classmethod
    def validate_datatype(cls, value: str) -> str:
        if value.lower() not in ALLOWED_DT:
            raise ValueError(f"Datatype {value} not in {ALLOWED_DT}")
        return value.lower()


class Form(BaseModel):
    title: str
    domain: str
    scenario: Optional[str] = None
    fields: list[FieldDef]

    def field_oids(self) -> list[str]:
        return [f.oid for f in self.fields]
