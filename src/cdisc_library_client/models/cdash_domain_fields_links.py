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
    from ..models.cdash_class_ref import CdashClassRef
    from ..models.cdash_domain_field_ref_element import CdashDomainFieldRefElement
    from ..models.cdash_domain_fields_ref import CdashDomainFieldsRef
    from ..models.cdash_product_ref import CdashProductRef


T = TypeVar("T", bound="CdashDomainFieldsLinks")


@_attrs_define
class CdashDomainFieldsLinks:
    """
    Attributes:
        self_ (Union[Unset, CdashDomainFieldsRef]):
        parent_product (Union[Unset, CdashProductRef]):
        parent_class (Union[Unset, CdashClassRef]):
        fields (Union[Unset, list['CdashDomainFieldRefElement']]):
    """

    self_: Union[Unset, "CdashDomainFieldsRef"] = UNSET
    parent_product: Union[Unset, "CdashProductRef"] = UNSET
    parent_class: Union[Unset, "CdashClassRef"] = UNSET
    fields: Union[Unset, list["CdashDomainFieldRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_class: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_class, Unset):
            parent_class = self.parent_class.to_dict()

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if parent_class is not UNSET:
            field_dict["parentClass"] = parent_class
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdash_class_ref import CdashClassRef
        from ..models.cdash_domain_field_ref_element import CdashDomainFieldRefElement
        from ..models.cdash_domain_fields_ref import CdashDomainFieldsRef
        from ..models.cdash_product_ref import CdashProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CdashDomainFieldsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CdashDomainFieldsRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, CdashProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = CdashProductRef.from_dict(_parent_product)

        _parent_class = d.pop("parentClass", UNSET)
        parent_class: Union[Unset, CdashClassRef]
        if isinstance(_parent_class, Unset):
            parent_class = UNSET
        else:
            parent_class = CdashClassRef.from_dict(_parent_class)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = CdashDomainFieldRefElement.from_dict(fields_item_data)

            fields.append(fields_item)

        cdash_domain_fields_links = cls(
            self_=self_,
            parent_product=parent_product,
            parent_class=parent_class,
            fields=fields,
        )

        cdash_domain_fields_links.additional_properties = d
        return cdash_domain_fields_links

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
