from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdashig_scenario_field_links import CdashigScenarioFieldLinks


T = TypeVar("T", bound="CdashigScenarioField")


@_attrs_define
class CdashigScenarioField:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 7.
        name (Union[Unset, str]):  Example: [VSTESTCD]_VSDAT.
        label (Union[Unset, str]):  Example: Vital Signs Date.
        definition (Union[Unset, str]):  Example: The date of the vital signs measurement, represented in an unambiguous
            date format (e.g., DD-MON-YYYY)..
        question_text (Union[Unset, str]):  Example: What was the date of the measurement(s)?.
        prompt (Union[Unset, str]):  Example: [VSTEST] Date.
        completion_instructions (Union[Unset, str]):  Example: Record date of measurements using this format (DD-MON-
            YYYY)..
        implementation_notes (Union[Unset, str]):  Example: A single date may be collected for all the vital sign
            measurements when they are performed on the same date. The date of each measurement can also be collected for
            each measurement using a CDASH variable [VSTESTCD]_VSDAT. The date of the measurements may be determined from a
            collected date of visit and in such cases a separate measurement date field is not required..
        simple_datatype (Union[Unset, str]):  Example: Char.
        mapping_instructions (Union[Unset, str]):  Example: This does not map directly to an SDTMIG variable. For the
            SDTM submission dataset, concatenate all collected CDASH DATE and TIME components and populate the SDTMIG
            variable VSDTC in ISO 8601 format..
        core (Union[Unset, str]):  Example: R/C.
        field_links (Union[Unset, CdashigScenarioFieldLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    definition: Union[Unset, str] = UNSET
    question_text: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    completion_instructions: Union[Unset, str] = UNSET
    implementation_notes: Union[Unset, str] = UNSET
    simple_datatype: Union[Unset, str] = UNSET
    mapping_instructions: Union[Unset, str] = UNSET
    core: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CdashigScenarioFieldLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        definition = self.definition

        question_text = self.question_text

        prompt = self.prompt

        completion_instructions = self.completion_instructions

        implementation_notes = self.implementation_notes

        simple_datatype = self.simple_datatype

        mapping_instructions = self.mapping_instructions

        core = self.core

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if definition is not UNSET:
            field_dict["definition"] = definition
        if question_text is not UNSET:
            field_dict["questionText"] = question_text
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if completion_instructions is not UNSET:
            field_dict["completionInstructions"] = completion_instructions
        if implementation_notes is not UNSET:
            field_dict["implementationNotes"] = implementation_notes
        if simple_datatype is not UNSET:
            field_dict["simpleDatatype"] = simple_datatype
        if mapping_instructions is not UNSET:
            field_dict["mappingInstructions"] = mapping_instructions
        if core is not UNSET:
            field_dict["core"] = core
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdashig_scenario_field_links import CdashigScenarioFieldLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        definition = d.pop("definition", UNSET)

        question_text = d.pop("questionText", UNSET)

        prompt = d.pop("prompt", UNSET)

        completion_instructions = d.pop("completionInstructions", UNSET)

        implementation_notes = d.pop("implementationNotes", UNSET)

        simple_datatype = d.pop("simpleDatatype", UNSET)

        mapping_instructions = d.pop("mappingInstructions", UNSET)

        core = d.pop("core", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CdashigScenarioFieldLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CdashigScenarioFieldLinks.from_dict(_field_links)

        cdashig_scenario_field = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            definition=definition,
            question_text=question_text,
            prompt=prompt,
            completion_instructions=completion_instructions,
            implementation_notes=implementation_notes,
            simple_datatype=simple_datatype,
            mapping_instructions=mapping_instructions,
            core=core,
            field_links=field_links,
        )

        cdashig_scenario_field.additional_properties = d
        return cdashig_scenario_field

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
