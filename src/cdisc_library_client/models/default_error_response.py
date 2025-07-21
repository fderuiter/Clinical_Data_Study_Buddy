from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultErrorResponse")


@_attrs_define
class DefaultErrorResponse:
    """
    Attributes:
        status_code (Union[Unset, str]): HTTP Status Code
        reason_phrase (Union[Unset, str]): HTTP Reason Phrase
        user_message (Union[Unset, str]): User Error Message
        admin_message (Union[Unset, str]): Admin Error Message
    """

    status_code: Union[Unset, str] = UNSET
    reason_phrase: Union[Unset, str] = UNSET
    user_message: Union[Unset, str] = UNSET
    admin_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        reason_phrase = self.reason_phrase

        user_message = self.user_message

        admin_message = self.admin_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if reason_phrase is not UNSET:
            field_dict["reasonPhrase"] = reason_phrase
        if user_message is not UNSET:
            field_dict["userMessage"] = user_message
        if admin_message is not UNSET:
            field_dict["adminMessage"] = admin_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_code = d.pop("statusCode", UNSET)

        reason_phrase = d.pop("reasonPhrase", UNSET)

        user_message = d.pop("userMessage", UNSET)

        admin_message = d.pop("adminMessage", UNSET)

        default_error_response = cls(
            status_code=status_code,
            reason_phrase=reason_phrase,
            user_message=user_message,
            admin_message=admin_message,
        )

        default_error_response.additional_properties = d
        return default_error_response

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
