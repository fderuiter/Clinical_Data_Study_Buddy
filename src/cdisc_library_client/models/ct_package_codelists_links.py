from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ct_codelist_ref_element import CtCodelistRefElement
    from ..models.ct_package_codelists_ref import CtPackageCodelistsRef


T = TypeVar("T", bound="CtPackageCodelistsLinks")


@_attrs_define
class CtPackageCodelistsLinks:
    """
    Attributes:
        self_ (Union[Unset, CtPackageCodelistsRef]):
        prior_version (Union[Unset, CtPackageCodelistsRef]):
        codelists (Union[Unset, list['CtCodelistRefElement']]):
    """

    self_: Union[Unset, "CtPackageCodelistsRef"] = UNSET
    prior_version: Union[Unset, "CtPackageCodelistsRef"] = UNSET
    codelists: Union[Unset, list["CtCodelistRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        codelists: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.codelists, Unset):
            codelists = []
            for codelists_item_data in self.codelists:
                codelists_item = codelists_item_data.to_dict()
                codelists.append(codelists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if codelists is not UNSET:
            field_dict["codelists"] = codelists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ct_codelist_ref_element import CtCodelistRefElement
        from ..models.ct_package_codelists_ref import CtPackageCodelistsRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CtPackageCodelistsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CtPackageCodelistsRef.from_dict(_self_)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, CtPackageCodelistsRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = CtPackageCodelistsRef.from_dict(_prior_version)

        codelists = []
        _codelists = d.pop("codelists", UNSET)
        for codelists_item_data in _codelists or []:
            codelists_item = CtCodelistRefElement.from_dict(codelists_item_data)

            codelists.append(codelists_item)

        ct_package_codelists_links = cls(
            self_=self_,
            prior_version=prior_version,
            codelists=codelists,
        )

        ct_package_codelists_links.additional_properties = d
        return ct_package_codelists_links

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
