from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ct_package_ref_element import CtPackageRefElement
    from ..models.ct_packages_ref import CtPackagesRef


T = TypeVar("T", bound="CtPackagesLinks")


@_attrs_define
class CtPackagesLinks:
    """
    Attributes:
        self_ (Union[Unset, CtPackagesRef]):
        packages (Union[Unset, list['CtPackageRefElement']]):
    """

    self_: Union[Unset, "CtPackagesRef"] = UNSET
    packages: Union[Unset, list["CtPackageRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ct_package_ref_element import CtPackageRefElement
        from ..models.ct_packages_ref import CtPackagesRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CtPackagesRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CtPackagesRef.from_dict(_self_)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = CtPackageRefElement.from_dict(packages_item_data)

            packages.append(packages_item)

        ct_packages_links = cls(
            self_=self_,
            packages=packages,
        )

        ct_packages_links.additional_properties = d
        return ct_packages_links

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
