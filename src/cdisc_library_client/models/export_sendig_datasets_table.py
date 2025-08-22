from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_sendig_datasets_row import ExportSendigDatasetsRow


T = TypeVar("T", bound="ExportSendigDatasetsTable")


@_attrs_define
class ExportSendigDatasetsTable:
    """
    Attributes:
        datasets (Union[Unset, list['ExportSendigDatasetsRow']]):
    """

    datasets: Union[Unset, list["ExportSendigDatasetsRow"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.datasets, Unset):
            datasets = []
            for datasets_item_data in self.datasets:
                datasets_item = datasets_item_data.to_dict()
                datasets.append(datasets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datasets is not UNSET:
            field_dict["datasets"] = datasets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_sendig_datasets_row import ExportSendigDatasetsRow

        d = dict(src_dict)
        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
            datasets_item = ExportSendigDatasetsRow.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        export_sendig_datasets_table = cls(
            datasets=datasets,
        )

        export_sendig_datasets_table.additional_properties = d
        return export_sendig_datasets_table

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
