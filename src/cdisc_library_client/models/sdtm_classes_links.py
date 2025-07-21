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
    from ..models.sdtm_class_ref_element import SdtmClassRefElement
    from ..models.sdtm_classes_ref import SdtmClassesRef


T = TypeVar("T", bound="SdtmClassesLinks")


@_attrs_define
class SdtmClassesLinks:
    """
    Attributes:
        self_ (Union[Unset, SdtmClassesRef]):
        prior_version (Union[Unset, SdtmClassesRef]):
        classes (Union[Unset, list['SdtmClassRefElement']]):
    """

    self_: Union[Unset, "SdtmClassesRef"] = UNSET
    prior_version: Union[Unset, "SdtmClassesRef"] = UNSET
    classes: Union[Unset, list["SdtmClassRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

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
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if classes is not UNSET:
            field_dict["classes"] = classes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtm_class_ref_element import SdtmClassRefElement
        from ..models.sdtm_classes_ref import SdtmClassesRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SdtmClassesRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SdtmClassesRef.from_dict(_self_)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, SdtmClassesRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = SdtmClassesRef.from_dict(_prior_version)

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = SdtmClassRefElement.from_dict(classes_item_data)

            classes.append(classes_item)

        sdtm_classes_links = cls(
            self_=self_,
            prior_version=prior_version,
            classes=classes,
        )

        sdtm_classes_links.additional_properties = d
        return sdtm_classes_links

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
