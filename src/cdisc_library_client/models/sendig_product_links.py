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
    from ..models.sdtm_product_ref import SdtmProductRef
    from ..models.sendig_product_ref import SendigProductRef


T = TypeVar("T", bound="SendigProductLinks")


@_attrs_define
class SendigProductLinks:
    """
    Attributes:
        self_ (Union[Unset, SendigProductRef]):
        model (Union[Unset, SdtmProductRef]):
        prior_version (Union[Unset, SendigProductRef]):
    """

    self_: Union[Unset, "SendigProductRef"] = UNSET
    model: Union[Unset, "SdtmProductRef"] = UNSET
    prior_version: Union[Unset, "SendigProductRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if model is not UNSET:
            field_dict["model"] = model
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtm_product_ref import SdtmProductRef
        from ..models.sendig_product_ref import SendigProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SendigProductRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SendigProductRef.from_dict(_self_)

        _model = d.pop("model", UNSET)
        model: Union[Unset, SdtmProductRef]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = SdtmProductRef.from_dict(_model)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, SendigProductRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = SendigProductRef.from_dict(_prior_version)

        sendig_product_links = cls(
            self_=self_,
            model=model,
            prior_version=prior_version,
        )

        sendig_product_links.additional_properties = d
        return sendig_product_links

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
