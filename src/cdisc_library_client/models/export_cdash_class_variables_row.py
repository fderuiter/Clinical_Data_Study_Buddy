from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportCdashClassVariablesRow")


@_attrs_define
class ExportCdashClassVariablesRow:
    """
    Attributes:
        version (Union[Unset, str]):
        class_ (Union[Unset, str]):
        domain (Union[Unset, str]):
        variable_order (Union[Unset, str]):
        cdash_variable (Union[Unset, str]):
        cdash_variable_label (Union[Unset, str]):
        draft_cdash_definition (Union[Unset, str]):
        domain_specific (Union[Unset, str]):
        question_text (Union[Unset, str]):
        prompt (Union[Unset, str]):
        type_ (Union[Unset, str]):
        sdtm_target (Union[Unset, list[str]]):
        mapping_instructions (Union[Unset, str]):
        controlled_terminology_codelist_name (Union[Unset, str]):
        implementation_notes (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    variable_order: Union[Unset, str] = UNSET
    cdash_variable: Union[Unset, str] = UNSET
    cdash_variable_label: Union[Unset, str] = UNSET
    draft_cdash_definition: Union[Unset, str] = UNSET
    domain_specific: Union[Unset, str] = UNSET
    question_text: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    sdtm_target: Union[Unset, list[str]] = UNSET
    mapping_instructions: Union[Unset, str] = UNSET
    controlled_terminology_codelist_name: Union[Unset, str] = UNSET
    implementation_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        class_ = self.class_

        domain = self.domain

        variable_order = self.variable_order

        cdash_variable = self.cdash_variable

        cdash_variable_label = self.cdash_variable_label

        draft_cdash_definition = self.draft_cdash_definition

        domain_specific = self.domain_specific

        question_text = self.question_text

        prompt = self.prompt

        type_ = self.type_

        sdtm_target: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sdtm_target, Unset):
            sdtm_target = self.sdtm_target

        mapping_instructions = self.mapping_instructions

        controlled_terminology_codelist_name = self.controlled_terminology_codelist_name

        implementation_notes = self.implementation_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if class_ is not UNSET:
            field_dict["Class"] = class_
        if domain is not UNSET:
            field_dict["Domain"] = domain
        if variable_order is not UNSET:
            field_dict["Variable Order"] = variable_order
        if cdash_variable is not UNSET:
            field_dict["CDASH Variable"] = cdash_variable
        if cdash_variable_label is not UNSET:
            field_dict["CDASH Variable Label"] = cdash_variable_label
        if draft_cdash_definition is not UNSET:
            field_dict["DRAFT CDASH Definition"] = draft_cdash_definition
        if domain_specific is not UNSET:
            field_dict["Domain Specific"] = domain_specific
        if question_text is not UNSET:
            field_dict["Question Text"] = question_text
        if prompt is not UNSET:
            field_dict["Prompt"] = prompt
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if sdtm_target is not UNSET:
            field_dict["SDTM Target"] = sdtm_target
        if mapping_instructions is not UNSET:
            field_dict["Mapping Instructions"] = mapping_instructions
        if controlled_terminology_codelist_name is not UNSET:
            field_dict["Controlled Terminology Codelist Name"] = controlled_terminology_codelist_name
        if implementation_notes is not UNSET:
            field_dict["Implementation Notes"] = implementation_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("Version", UNSET)

        class_ = d.pop("Class", UNSET)

        domain = d.pop("Domain", UNSET)

        variable_order = d.pop("Variable Order", UNSET)

        cdash_variable = d.pop("CDASH Variable", UNSET)

        cdash_variable_label = d.pop("CDASH Variable Label", UNSET)

        draft_cdash_definition = d.pop("DRAFT CDASH Definition", UNSET)

        domain_specific = d.pop("Domain Specific", UNSET)

        question_text = d.pop("Question Text", UNSET)

        prompt = d.pop("Prompt", UNSET)

        type_ = d.pop("Type", UNSET)

        sdtm_target = cast(list[str], d.pop("SDTM Target", UNSET))

        mapping_instructions = d.pop("Mapping Instructions", UNSET)

        controlled_terminology_codelist_name = d.pop("Controlled Terminology Codelist Name", UNSET)

        implementation_notes = d.pop("Implementation Notes", UNSET)

        export_cdash_class_variables_row = cls(
            version=version,
            class_=class_,
            domain=domain,
            variable_order=variable_order,
            cdash_variable=cdash_variable,
            cdash_variable_label=cdash_variable_label,
            draft_cdash_definition=draft_cdash_definition,
            domain_specific=domain_specific,
            question_text=question_text,
            prompt=prompt,
            type_=type_,
            sdtm_target=sdtm_target,
            mapping_instructions=mapping_instructions,
            controlled_terminology_codelist_name=controlled_terminology_codelist_name,
            implementation_notes=implementation_notes,
        )

        export_cdash_class_variables_row.additional_properties = d
        return export_cdash_class_variables_row

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
