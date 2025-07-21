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
    from ..models.qrs_items_ref import QrsItemsRef
    from ..models.qrs_product_ref import QrsProductRef
    from ..models.root_ct_term_ref import RootCtTermRef


T = TypeVar("T", bound="QrsProductLinks")


@_attrs_define
class QrsProductLinks:
    """
    Attributes:
        self_ (Union[Unset, QrsProductRef]):
        prior_version (Union[Unset, QrsProductRef]):
        qrs_term_cat (Union[Unset, RootCtTermRef]):
        qrs_items (Union[Unset, QrsItemsRef]):
    """

    self_: Union[Unset, "QrsProductRef"] = UNSET
    prior_version: Union[Unset, "QrsProductRef"] = UNSET
    qrs_term_cat: Union[Unset, "RootCtTermRef"] = UNSET
    qrs_items: Union[Unset, "QrsItemsRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        qrs_term_cat: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_term_cat, Unset):
            qrs_term_cat = self.qrs_term_cat.to_dict()

        qrs_items: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_items, Unset):
            qrs_items = self.qrs_items.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if qrs_term_cat is not UNSET:
            field_dict["qrsTermCAT"] = qrs_term_cat
        if qrs_items is not UNSET:
            field_dict["qrsItems"] = qrs_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qrs_items_ref import QrsItemsRef
        from ..models.qrs_product_ref import QrsProductRef
        from ..models.root_ct_term_ref import RootCtTermRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, QrsProductRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = QrsProductRef.from_dict(_self_)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, QrsProductRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = QrsProductRef.from_dict(_prior_version)

        _qrs_term_cat = d.pop("qrsTermCAT", UNSET)
        qrs_term_cat: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_term_cat, Unset):
            qrs_term_cat = UNSET
        else:
            qrs_term_cat = RootCtTermRef.from_dict(_qrs_term_cat)

        _qrs_items = d.pop("qrsItems", UNSET)
        qrs_items: Union[Unset, QrsItemsRef]
        if isinstance(_qrs_items, Unset):
            qrs_items = UNSET
        else:
            qrs_items = QrsItemsRef.from_dict(_qrs_items)

        qrs_product_links = cls(
            self_=self_,
            prior_version=prior_version,
            qrs_term_cat=qrs_term_cat,
            qrs_items=qrs_items,
        )

        qrs_product_links.additional_properties = d
        return qrs_product_links

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
