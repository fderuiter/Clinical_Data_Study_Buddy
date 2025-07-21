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
    from ..models.qrs_item_links import QrsItemLinks


T = TypeVar("T", bound="QrsItem")


@_attrs_define
class QrsItem:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 1.
        label (Union[Unset, str]):  Example: AIMS01-Muscles of Facial Expression.
        question_text (Union[Unset, str]):  Example: Abnormal Involuntary Movement Scale - Facial and Oral Movements,
            Muscles of facial expression, e.g., movements of forehead, eyebrows, periorbital area, cheeks. Include frowning,
            blinking, grimacing of upper face..
        field_links (Union[Unset, QrsItemLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    question_text: Union[Unset, str] = UNSET
    field_links: Union[Unset, "QrsItemLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        label = self.label

        question_text = self.question_text

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if label is not UNSET:
            field_dict["label"] = label
        if question_text is not UNSET:
            field_dict["questionText"] = question_text
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qrs_item_links import QrsItemLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        label = d.pop("label", UNSET)

        question_text = d.pop("questionText", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, QrsItemLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = QrsItemLinks.from_dict(_field_links)

        qrs_item = cls(
            ordinal=ordinal,
            label=label,
            question_text=question_text,
            field_links=field_links,
        )

        qrs_item.additional_properties = d
        return qrs_item

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
