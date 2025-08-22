from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdash_class_field_links import CdashClassFieldLinks


T = TypeVar("T", bound="CdashClassField")


@_attrs_define
class CdashClassField:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 8.
        name (Union[Unset, str]):  Example: --DAT.
        label (Union[Unset, str]):  Example: Collection Date.
        definition (Union[Unset, str]):  Example: Collection date of an observation..
        question_text (Union[Unset, str]):  Example: What [is/was] the date the [event or intervention] [is/was]
            collected?; What [is/was] the (start) date (of the [Finding])?.
        prompt (Union[Unset, str]):  Example: [Event/Intervention] Collection Date; [Finding] (Start) Date.
        simple_datatype (Union[Unset, str]):  Example: Char.
        implementation_notes (Union[Unset, str]):  Example: This is a generic DATE field that can be implemented in a
            system that will store partial dates. Use this for: 1. Date of data collection, 2. Visit date, 3. Visit start
            date, 4. Point in time collection (e.g., vital signs measurements, lab sample collection date), 5. Start date
            for interval collection of measurements or tests (e.g., start date of a 24-hour urine collection). Refer to the
            FDA Study Data Technical Conformance Guide v2.2 (June 12, 2015) Section 4.1.4.1 which indicates that when dates
            have the role of a timing variable, the matching Study Day variables (--DY, --STDY, or --ENDY, respectively) are
            included in the SDTM.
        mapping_instructions (Union[Unset, str]):  Example: This field does not map directly to an SDTM variable. For
            the SDTM dataset, concatenate all collected CDASH DATE and TIME components and populate the SDTM variable --DTC
            in ISO 8601 format. Refer to the FDA Study Data Technical Conformance Guide v2.2 (June 12, 2015) Section 4.1.4.1
            which indicates that when dates have the role of a timing variable, the matching Study Day variables (--DY,
            --STDY, or --ENDY, respectively) should be included in the SDTM dataset..
        field_links (Union[Unset, CdashClassFieldLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    definition: Union[Unset, str] = UNSET
    question_text: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    simple_datatype: Union[Unset, str] = UNSET
    implementation_notes: Union[Unset, str] = UNSET
    mapping_instructions: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CdashClassFieldLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        definition = self.definition

        question_text = self.question_text

        prompt = self.prompt

        simple_datatype = self.simple_datatype

        implementation_notes = self.implementation_notes

        mapping_instructions = self.mapping_instructions

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
        if simple_datatype is not UNSET:
            field_dict["simpleDatatype"] = simple_datatype
        if implementation_notes is not UNSET:
            field_dict["implementationNotes"] = implementation_notes
        if mapping_instructions is not UNSET:
            field_dict["mappingInstructions"] = mapping_instructions
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdash_class_field_links import CdashClassFieldLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        definition = d.pop("definition", UNSET)

        question_text = d.pop("questionText", UNSET)

        prompt = d.pop("prompt", UNSET)

        simple_datatype = d.pop("simpleDatatype", UNSET)

        implementation_notes = d.pop("implementationNotes", UNSET)

        mapping_instructions = d.pop("mappingInstructions", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CdashClassFieldLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CdashClassFieldLinks.from_dict(_field_links)

        cdash_class_field = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            definition=definition,
            question_text=question_text,
            prompt=prompt,
            simple_datatype=simple_datatype,
            implementation_notes=implementation_notes,
            mapping_instructions=mapping_instructions,
            field_links=field_links,
        )

        cdash_class_field.additional_properties = d
        return cdash_class_field

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
