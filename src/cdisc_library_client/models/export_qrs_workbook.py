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
    from ..models.export_qrs_general import ExportQrsGeneral
    from ..models.export_qrs_responses import ExportQrsResponses
    from ..models.export_qrs_workbook_items_row import ExportQrsWorkbookItemsRow


T = TypeVar("T", bound="ExportQrsWorkbook")


@_attrs_define
class ExportQrsWorkbook:
    """
    Attributes:
        self_ (Union[Unset, ExportQrsGeneral]):
        items (Union[Unset, list['ExportQrsWorkbookItemsRow']]):
        responses (Union[Unset, list['ExportQrsResponses']]):
    """

    self_: Union[Unset, "ExportQrsGeneral"] = UNSET
    items: Union[Unset, list["ExportQrsWorkbookItemsRow"]] = UNSET
    responses: Union[Unset, list["ExportQrsResponses"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

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
        if items is not UNSET:
            field_dict["items"] = items
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_qrs_general import ExportQrsGeneral
        from ..models.export_qrs_responses import ExportQrsResponses
        from ..models.export_qrs_workbook_items_row import ExportQrsWorkbookItemsRow

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, ExportQrsGeneral]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = ExportQrsGeneral.from_dict(_self_)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = ExportQrsWorkbookItemsRow.from_dict(items_item_data)

            items.append(items_item)

        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = ExportQrsResponses.from_dict(responses_item_data)

            responses.append(responses_item)

        export_qrs_workbook = cls(
            self_=self_,
            items=items,
            responses=responses,
        )

        export_qrs_workbook.additional_properties = d
        return export_qrs_workbook

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
