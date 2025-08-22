from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdashig_class_ref_element import CdashigClassRefElement
    from ..models.cdashig_product_classes_ref import CdashigProductClassesRef
    from ..models.cdashig_product_ref import CdashigProductRef


T = TypeVar("T", bound="CdashigProductClassesLinks")


@_attrs_define
class CdashigProductClassesLinks:
    """
    Attributes:
        self_ (Union[Unset, CdashigProductClassesRef]):
        parent_product (Union[Unset, CdashigProductRef]):
        classes (Union[Unset, list['CdashigClassRefElement']]):
    """

    self_: Union[Unset, "CdashigProductClassesRef"] = UNSET
    parent_product: Union[Unset, "CdashigProductRef"] = UNSET
    classes: Union[Unset, list["CdashigClassRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        classes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = []
            for classes_item_data in self.classes:
                classes_item = classes_item_data.to_dict()
                classes.append(classes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if classes is not UNSET:
            field_dict["classes"] = classes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdashig_class_ref_element import CdashigClassRefElement
        from ..models.cdashig_product_classes_ref import CdashigProductClassesRef
        from ..models.cdashig_product_ref import CdashigProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CdashigProductClassesRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CdashigProductClassesRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, CdashigProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = CdashigProductRef.from_dict(_parent_product)

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = CdashigClassRefElement.from_dict(classes_item_data)

            classes.append(classes_item)

        cdashig_product_classes_links = cls(
            self_=self_,
            parent_product=parent_product,
            classes=classes,
        )

        cdashig_product_classes_links.additional_properties = d
        return cdashig_product_classes_links

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
