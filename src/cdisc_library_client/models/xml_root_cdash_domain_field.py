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
    from ..models.root_cdash_domain_field import RootCdashDomainField


T = TypeVar("T", bound="XmlRootCdashDomainField")


@_attrs_define
class XmlRootCdashDomainField:
    """
    Attributes:
        self_ (Union[Unset, RootCdashDomainField]):
    """

    self_: Union[Unset, "RootCdashDomainField"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.root_cdash_domain_field import RootCdashDomainField

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, RootCdashDomainField]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = RootCdashDomainField.from_dict(_self_)

        xml_root_cdash_domain_field = cls(
            self_=self_,
        )

        xml_root_cdash_domain_field.additional_properties = d
        return xml_root_cdash_domain_field

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
