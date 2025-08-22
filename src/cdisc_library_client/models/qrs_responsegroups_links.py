from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qrs_responsegroup_ref_element import QrsResponsegroupRefElement
    from ..models.qrs_responsegroups_ref import QrsResponsegroupsRef


T = TypeVar("T", bound="QrsResponsegroupsLinks")


@_attrs_define
class QrsResponsegroupsLinks:
    """
    Attributes:
        self_ (Union[Unset, QrsResponsegroupsRef]):
        responsegroups (Union[Unset, list['QrsResponsegroupRefElement']]):
    """

    self_: Union[Unset, "QrsResponsegroupsRef"] = UNSET
    responsegroups: Union[Unset, list["QrsResponsegroupRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        responsegroups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.responsegroups, Unset):
            responsegroups = []
            for responsegroups_item_data in self.responsegroups:
                responsegroups_item = responsegroups_item_data.to_dict()
                responsegroups.append(responsegroups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if responsegroups is not UNSET:
            field_dict["responsegroups"] = responsegroups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qrs_responsegroup_ref_element import QrsResponsegroupRefElement
        from ..models.qrs_responsegroups_ref import QrsResponsegroupsRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, QrsResponsegroupsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = QrsResponsegroupsRef.from_dict(_self_)

        responsegroups = []
        _responsegroups = d.pop("responsegroups", UNSET)
        for responsegroups_item_data in _responsegroups or []:
            responsegroups_item = QrsResponsegroupRefElement.from_dict(responsegroups_item_data)

            responsegroups.append(responsegroups_item)

        qrs_responsegroups_links = cls(
            self_=self_,
            responsegroups=responsegroups,
        )

        qrs_responsegroups_links.additional_properties = d
        return qrs_responsegroups_links

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
