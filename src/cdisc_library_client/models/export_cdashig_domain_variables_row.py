from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportCdashigDomainVariablesRow")


@_attrs_define
class ExportCdashigDomainVariablesRow:
    """
    Attributes:
        version (Union[Unset, str]):
        class_ (Union[Unset, str]):
        domain (Union[Unset, str]):
        data_collection_scenario (Union[Unset, str]):
        variable_order (Union[Unset, str]):
        cdashig_variable (Union[Unset, str]):
        cdashig_variable_label (Union[Unset, str]):
        draft_cdashig_definition (Union[Unset, str]):
        question_text (Union[Unset, str]):
        prompt (Union[Unset, str]):
        type_ (Union[Unset, str]):
        cdashig_core (Union[Unset, str]):
        case_report_form_completion_instructions (Union[Unset, str]):
        sdtmig_target (Union[Unset, list[str]]):
        mapping_instructions (Union[Unset, str]):
        controlled_terminology_codelist_name (Union[Unset, str]):
        implementation_notes (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    data_collection_scenario: Union[Unset, str] = UNSET
    variable_order: Union[Unset, str] = UNSET
    cdashig_variable: Union[Unset, str] = UNSET
    cdashig_variable_label: Union[Unset, str] = UNSET
    draft_cdashig_definition: Union[Unset, str] = UNSET
    question_text: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    cdashig_core: Union[Unset, str] = UNSET
    case_report_form_completion_instructions: Union[Unset, str] = UNSET
    sdtmig_target: Union[Unset, list[str]] = UNSET
    mapping_instructions: Union[Unset, str] = UNSET
    controlled_terminology_codelist_name: Union[Unset, str] = UNSET
    implementation_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        class_ = self.class_

        domain = self.domain

        data_collection_scenario = self.data_collection_scenario

        variable_order = self.variable_order

        cdashig_variable = self.cdashig_variable

        cdashig_variable_label = self.cdashig_variable_label

        draft_cdashig_definition = self.draft_cdashig_definition

        question_text = self.question_text

        prompt = self.prompt

        type_ = self.type_

        cdashig_core = self.cdashig_core

        case_report_form_completion_instructions = self.case_report_form_completion_instructions

        sdtmig_target: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sdtmig_target, Unset):
            sdtmig_target = self.sdtmig_target

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
        if data_collection_scenario is not UNSET:
            field_dict["Data Collection Scenario"] = data_collection_scenario
        if variable_order is not UNSET:
            field_dict["Variable Order"] = variable_order
        if cdashig_variable is not UNSET:
            field_dict["CDASHIG Variable"] = cdashig_variable
        if cdashig_variable_label is not UNSET:
            field_dict["CDASHIG Variable Label"] = cdashig_variable_label
        if draft_cdashig_definition is not UNSET:
            field_dict["DRAFT CDASHIG Definition"] = draft_cdashig_definition
        if question_text is not UNSET:
            field_dict["Question Text"] = question_text
        if prompt is not UNSET:
            field_dict["Prompt"] = prompt
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if cdashig_core is not UNSET:
            field_dict["CDASHIG Core"] = cdashig_core
        if case_report_form_completion_instructions is not UNSET:
            field_dict["Case Report Form Completion Instructions"] = case_report_form_completion_instructions
        if sdtmig_target is not UNSET:
            field_dict["SDTMIG Target"] = sdtmig_target
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

        data_collection_scenario = d.pop("Data Collection Scenario", UNSET)

        variable_order = d.pop("Variable Order", UNSET)

        cdashig_variable = d.pop("CDASHIG Variable", UNSET)

        cdashig_variable_label = d.pop("CDASHIG Variable Label", UNSET)

        draft_cdashig_definition = d.pop("DRAFT CDASHIG Definition", UNSET)

        question_text = d.pop("Question Text", UNSET)

        prompt = d.pop("Prompt", UNSET)

        type_ = d.pop("Type", UNSET)

        cdashig_core = d.pop("CDASHIG Core", UNSET)

        case_report_form_completion_instructions = d.pop("Case Report Form Completion Instructions", UNSET)

        sdtmig_target = cast(list[str], d.pop("SDTMIG Target", UNSET))

        mapping_instructions = d.pop("Mapping Instructions", UNSET)

        controlled_terminology_codelist_name = d.pop("Controlled Terminology Codelist Name", UNSET)

        implementation_notes = d.pop("Implementation Notes", UNSET)

        export_cdashig_domain_variables_row = cls(
            version=version,
            class_=class_,
            domain=domain,
            data_collection_scenario=data_collection_scenario,
            variable_order=variable_order,
            cdashig_variable=cdashig_variable,
            cdashig_variable_label=cdashig_variable_label,
            draft_cdashig_definition=draft_cdashig_definition,
            question_text=question_text,
            prompt=prompt,
            type_=type_,
            cdashig_core=cdashig_core,
            case_report_form_completion_instructions=case_report_form_completion_instructions,
            sdtmig_target=sdtmig_target,
            mapping_instructions=mapping_instructions,
            controlled_terminology_codelist_name=controlled_terminology_codelist_name,
            implementation_notes=implementation_notes,
        )

        export_cdashig_domain_variables_row.additional_properties = d
        return export_cdashig_domain_variables_row

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
