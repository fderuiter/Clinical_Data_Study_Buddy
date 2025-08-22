from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ct_codelist_links import CtCodelistLinks
    from ..models.ct_package_term import CtPackageTerm


T = TypeVar("T", bound="CtCodelist")


@_attrs_define
class CtCodelist:
    """
    Attributes:
        concept_id (Union[Unset, str]):  Example: C67154.
        extensible (Union[Unset, str]):  Example: true.
        name (Union[Unset, str]):  Example: Laboratory Test Name.
        submission_value (Union[Unset, str]):  Example: LBTEST.
        definition (Union[Unset, str]):  Example: Terminology used for laboratory test names of the CDISC Study Data
            Tabulation Model..
        preferred_term (Union[Unset, str]):  Example: CDISC SDTM Laboratory Test Name Terminology.
        synonyms (Union[Unset, list[str]]):  Example: ['Laboratory Test Name'].
        field_links (Union[Unset, CtCodelistLinks]):
        terms (Union[Unset, list['CtPackageTerm']]):
    """

    concept_id: Union[Unset, str] = UNSET
    extensible: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    submission_value: Union[Unset, str] = UNSET
    definition: Union[Unset, str] = UNSET
    preferred_term: Union[Unset, str] = UNSET
    synonyms: Union[Unset, list[str]] = UNSET
    field_links: Union[Unset, "CtCodelistLinks"] = UNSET
    terms: Union[Unset, list["CtPackageTerm"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concept_id = self.concept_id

        extensible = self.extensible

        name = self.name

        submission_value = self.submission_value

        definition = self.definition

        preferred_term = self.preferred_term

        synonyms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.synonyms, Unset):
            synonyms = self.synonyms

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        terms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.terms, Unset):
            terms = []
            for terms_item_data in self.terms:
                terms_item = terms_item_data.to_dict()
                terms.append(terms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concept_id is not UNSET:
            field_dict["conceptId"] = concept_id
        if extensible is not UNSET:
            field_dict["extensible"] = extensible
        if name is not UNSET:
            field_dict["name"] = name
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
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ct_codelist_links import CtCodelistLinks
        from ..models.ct_package_term import CtPackageTerm

        d = dict(src_dict)
        concept_id = d.pop("conceptId", UNSET)

        extensible = d.pop("extensible", UNSET)

        name = d.pop("name", UNSET)

        submission_value = d.pop("submissionValue", UNSET)

        definition = d.pop("definition", UNSET)

        preferred_term = d.pop("preferredTerm", UNSET)

        synonyms = cast(list[str], d.pop("synonyms", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CtCodelistLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CtCodelistLinks.from_dict(_field_links)

        terms = []
        _terms = d.pop("terms", UNSET)
        for terms_item_data in _terms or []:
            terms_item = CtPackageTerm.from_dict(terms_item_data)

            terms.append(terms_item)

        ct_codelist = cls(
            concept_id=concept_id,
            extensible=extensible,
            name=name,
            submission_value=submission_value,
            definition=definition,
            preferred_term=preferred_term,
            synonyms=synonyms,
            field_links=field_links,
            terms=terms,
        )

        ct_codelist.additional_properties = d
        return ct_codelist

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
