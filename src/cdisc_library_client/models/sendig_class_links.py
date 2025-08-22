from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sdtm_class_ref import SdtmClassRef
    from ..models.sendig_class_ref import SendigClassRef
    from ..models.sendig_class_ref_subclass import SendigClassRefSubclass
    from ..models.sendig_product_ref import SendigProductRef


T = TypeVar("T", bound="SendigClassLinks")


@_attrs_define
class SendigClassLinks:
    """
    Attributes:
        self_ (Union[Unset, SendigClassRef]):
        model_class (Union[Unset, SdtmClassRef]):
        parent_product (Union[Unset, SendigProductRef]):
        parent_class (Union[Unset, SendigClassRef]):
        subclasses (Union[Unset, list['SendigClassRefSubclass']]):
        prior_version (Union[Unset, SendigClassRef]):
    """

    self_: Union[Unset, "SendigClassRef"] = UNSET
    model_class: Union[Unset, "SdtmClassRef"] = UNSET
    parent_product: Union[Unset, "SendigProductRef"] = UNSET
    parent_class: Union[Unset, "SendigClassRef"] = UNSET
    subclasses: Union[Unset, list["SendigClassRefSubclass"]] = UNSET
    prior_version: Union[Unset, "SendigClassRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        model_class: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.model_class, Unset):
            model_class = self.model_class.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_class: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_class, Unset):
            parent_class = self.parent_class.to_dict()

        subclasses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subclasses, Unset):
            subclasses = []
            for subclasses_item_data in self.subclasses:
                subclasses_item = subclasses_item_data.to_dict()
                subclasses.append(subclasses_item)

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if model_class is not UNSET:
            field_dict["modelClass"] = model_class
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if parent_class is not UNSET:
            field_dict["parentClass"] = parent_class
        if subclasses is not UNSET:
            field_dict["subclasses"] = subclasses
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtm_class_ref import SdtmClassRef
        from ..models.sendig_class_ref import SendigClassRef
        from ..models.sendig_class_ref_subclass import SendigClassRefSubclass
        from ..models.sendig_product_ref import SendigProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SendigClassRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SendigClassRef.from_dict(_self_)

        _model_class = d.pop("modelClass", UNSET)
        model_class: Union[Unset, SdtmClassRef]
        if isinstance(_model_class, Unset):
            model_class = UNSET
        else:
            model_class = SdtmClassRef.from_dict(_model_class)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, SendigProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = SendigProductRef.from_dict(_parent_product)

        _parent_class = d.pop("parentClass", UNSET)
        parent_class: Union[Unset, SendigClassRef]
        if isinstance(_parent_class, Unset):
            parent_class = UNSET
        else:
            parent_class = SendigClassRef.from_dict(_parent_class)

        subclasses = []
        _subclasses = d.pop("subclasses", UNSET)
        for subclasses_item_data in _subclasses or []:
            subclasses_item = SendigClassRefSubclass.from_dict(subclasses_item_data)

            subclasses.append(subclasses_item)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, SendigClassRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = SendigClassRef.from_dict(_prior_version)

        sendig_class_links = cls(
            self_=self_,
            model_class=model_class,
            parent_product=parent_product,
            parent_class=parent_class,
            subclasses=subclasses,
            prior_version=prior_version,
        )

        sendig_class_links.additional_properties = d
        return sendig_class_links

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
