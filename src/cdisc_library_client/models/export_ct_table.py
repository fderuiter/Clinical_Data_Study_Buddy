from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_ct_codelist import ExportCtCodelist


T = TypeVar("T", bound="ExportCtTable")


@_attrs_define
class ExportCtTable:
    """
    Attributes:
        ct (Union[Unset, list['ExportCtCodelist']]):
    """

    ct: Union[Unset, list["ExportCtCodelist"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ct: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ct, Unset):
            ct = []
            for ct_item_data in self.ct:
                ct_item = ct_item_data.to_dict()
                ct.append(ct_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ct is not UNSET:
            field_dict["ct"] = ct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_ct_codelist import ExportCtCodelist

        d = dict(src_dict)
        ct = []
        _ct = d.pop("ct", UNSET)
        for ct_item_data in _ct or []:
            ct_item = ExportCtCodelist.from_dict(ct_item_data)

            ct.append(ct_item)

        export_ct_table = cls(
            ct=ct,
        )

        export_ct_table.additional_properties = d
        return export_ct_table

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
