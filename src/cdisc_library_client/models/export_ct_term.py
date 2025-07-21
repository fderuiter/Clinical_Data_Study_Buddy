from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportCtTerm")


@_attrs_define
class ExportCtTerm:
    """
    Attributes:
        bundle_1 (Union[Unset, str]):
        cdisc_synonyms (Union[Unset, list[str]]):
        bundle_2 (Union[Unset, str]):
    """

    bundle_1: Union[Unset, str] = UNSET
    cdisc_synonyms: Union[Unset, list[str]] = UNSET
    bundle_2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundle_1 = self.bundle_1

        cdisc_synonyms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cdisc_synonyms, Unset):
            cdisc_synonyms = self.cdisc_synonyms

        bundle_2 = self.bundle_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bundle_1 is not UNSET:
            field_dict["bundle-1"] = bundle_1
        if cdisc_synonyms is not UNSET:
            field_dict["CDISC Synonym(s)"] = cdisc_synonyms
        if bundle_2 is not UNSET:
            field_dict["bundle-2"] = bundle_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bundle_1 = d.pop("bundle-1", UNSET)

        cdisc_synonyms = cast(list[str], d.pop("CDISC Synonym(s)", UNSET))

        bundle_2 = d.pop("bundle-2", UNSET)

        export_ct_term = cls(
            bundle_1=bundle_1,
            cdisc_synonyms=cdisc_synonyms,
            bundle_2=bundle_2,
        )

        export_ct_term.additional_properties = d
        return export_ct_term

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
