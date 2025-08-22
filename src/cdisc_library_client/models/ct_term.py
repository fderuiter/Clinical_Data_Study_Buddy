from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ct_term_links import CtTermLinks


T = TypeVar("T", bound="CtTerm")


@_attrs_define
class CtTerm:
    """
    Attributes:
        concept_id (Union[Unset, str]):  Example: C64796.
        submission_value (Union[Unset, str]):  Example: Hematocrit.
        definition (Union[Unset, str]):  Example: The percentage of a whole blood specimen that is composed of red blood
            cells (erythrocytes)..
        preferred_term (Union[Unset, str]):  Example: Hematocrit Measurement.
        synonyms (Union[Unset, list[str]]):  Example: ['EVF', 'Erythrocyte Volume Fraction', 'Hematocrit', 'PCV',
            'Packed Cell Volume'].
        field_links (Union[Unset, CtTermLinks]):
    """

    concept_id: Union[Unset, str] = UNSET
    submission_value: Union[Unset, str] = UNSET
    definition: Union[Unset, str] = UNSET
    preferred_term: Union[Unset, str] = UNSET
    synonyms: Union[Unset, list[str]] = UNSET
    field_links: Union[Unset, "CtTermLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concept_id = self.concept_id

        submission_value = self.submission_value

        definition = self.definition

        preferred_term = self.preferred_term

        synonyms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.synonyms, Unset):
            synonyms = self.synonyms

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concept_id is not UNSET:
            field_dict["conceptId"] = concept_id
        if submission_value is not UNSET:
            field_dict["submissionValue"] = submission_value
        if definition is not UNSET:
            field_dict["definition"] = definition
        if preferred_term is not UNSET:
            field_dict["preferredTerm"] = preferred_term
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ct_term_links import CtTermLinks

        d = dict(src_dict)
        concept_id = d.pop("conceptId", UNSET)

        submission_value = d.pop("submissionValue", UNSET)

        definition = d.pop("definition", UNSET)

        preferred_term = d.pop("preferredTerm", UNSET)

        synonyms = cast(list[str], d.pop("synonyms", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CtTermLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CtTermLinks.from_dict(_field_links)

        ct_term = cls(
            concept_id=concept_id,
            submission_value=submission_value,
            definition=definition,
            preferred_term=preferred_term,
            synonyms=synonyms,
            field_links=field_links,
        )

        ct_term.additional_properties = d
        return ct_term

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
