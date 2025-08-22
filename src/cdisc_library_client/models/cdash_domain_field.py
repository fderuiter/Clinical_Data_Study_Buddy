from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdash_domain_field_links import CdashDomainFieldLinks


T = TypeVar("T", bound="CdashDomainField")


@_attrs_define
class CdashDomainField:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 18.
        name (Union[Unset, str]):  Example: AGE.
        label (Union[Unset, str]):  Example: Age.
        definition (Union[Unset, str]):  Example: The age of the subject expressed in AGEU..
        domain_specific (Union[Unset, str]):
        question_text (Union[Unset, str]):  Example: What [is/was] the subject's age?.
        prompt (Union[Unset, str]):  Example: Age.
        simple_datatype (Union[Unset, str]):  Example: Num.
        implementation_notes (Union[Unset, str]):  Example: If Age is collected, it should be collected as a number and,
            to be correctly interpreted, the age value should be associated to a variable for the Age Unit. It may be
            necessary to know when the age was collected as an age may need to be recalculated for analysis, such as
            deriving age at a reference start time (RFSTDTC for SDTM). BRTHDTC may not be available in all cases (due to
            subject privacy concerns). If AGE is collected, then it is recommended that the date of collection also be
            recorded, either separately or by association to the date of the visit..
        mapping_instructions (Union[Unset, str]):  Example: Maps directly to the SDTM variable listed in the column with
            the heading "SDTM Target"..
        field_links (Union[Unset, CdashDomainFieldLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    definition: Union[Unset, str] = UNSET
    domain_specific: Union[Unset, str] = UNSET
    question_text: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    simple_datatype: Union[Unset, str] = UNSET
    implementation_notes: Union[Unset, str] = UNSET
    mapping_instructions: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CdashDomainFieldLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        definition = self.definition

        domain_specific = self.domain_specific

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
        if domain_specific is not UNSET:
            field_dict["domainSpecific"] = domain_specific
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
        from ..models.cdash_domain_field_links import CdashDomainFieldLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        definition = d.pop("definition", UNSET)

        domain_specific = d.pop("domainSpecific", UNSET)

        question_text = d.pop("questionText", UNSET)

        prompt = d.pop("prompt", UNSET)

        simple_datatype = d.pop("simpleDatatype", UNSET)

        implementation_notes = d.pop("implementationNotes", UNSET)

        mapping_instructions = d.pop("mappingInstructions", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CdashDomainFieldLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CdashDomainFieldLinks.from_dict(_field_links)

        cdash_domain_field = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            definition=definition,
            domain_specific=domain_specific,
            question_text=question_text,
            prompt=prompt,
            simple_datatype=simple_datatype,
            implementation_notes=implementation_notes,
            mapping_instructions=mapping_instructions,
            field_links=field_links,
        )

        cdash_domain_field.additional_properties = d
        return cdash_domain_field

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
