from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qrs_responsegroup_ref import QrsResponsegroupRef
    from ..models.qrs_responses import QrsResponses


T = TypeVar("T", bound="QrsResponsegroupLinks")


@_attrs_define
class QrsResponsegroupLinks:
    """
    Attributes:
        self_ (Union[Unset, QrsResponsegroupRef]):
        responses (Union[Unset, list['QrsResponses']]):
    """

    self_: Union[Unset, "QrsResponsegroupRef"] = UNSET
    responses: Union[Unset, list["QrsResponses"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        responses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()
                responses.append(responses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qrs_responsegroup_ref import QrsResponsegroupRef
        from ..models.qrs_responses import QrsResponses

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, QrsResponsegroupRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = QrsResponsegroupRef.from_dict(_self_)

        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = QrsResponses.from_dict(responses_item_data)

            responses.append(responses_item)

        qrs_responsegroup_links = cls(
            self_=self_,
            responses=responses,
        )

        qrs_responsegroup_links.additional_properties = d
        return qrs_responsegroup_links

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
