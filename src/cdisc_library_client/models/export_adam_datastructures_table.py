from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_adam_datastructures_row import ExportAdamDatastructuresRow


T = TypeVar("T", bound="ExportAdamDatastructuresTable")


@_attrs_define
class ExportAdamDatastructuresTable:
    """
    Attributes:
        datastructures (Union[Unset, list['ExportAdamDatastructuresRow']]):
    """

    datastructures: Union[Unset, list["ExportAdamDatastructuresRow"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datastructures: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.datastructures, Unset):
            datastructures = []
            for datastructures_item_data in self.datastructures:
                datastructures_item = datastructures_item_data.to_dict()
                datastructures.append(datastructures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datastructures is not UNSET:
            field_dict["datastructures"] = datastructures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_adam_datastructures_row import ExportAdamDatastructuresRow

        d = dict(src_dict)
        datastructures = []
        _datastructures = d.pop("datastructures", UNSET)
        for datastructures_item_data in _datastructures or []:
            datastructures_item = ExportAdamDatastructuresRow.from_dict(datastructures_item_data)

            datastructures.append(datastructures_item)

        export_adam_datastructures_table = cls(
            datastructures=datastructures,
        )

        export_adam_datastructures_table.additional_properties = d
        return export_adam_datastructures_table

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
