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
    from ..models.export_sdtmig_datasets_row import ExportSdtmigDatasetsRow
    from ..models.export_sdtmig_variables_row import ExportSdtmigVariablesRow


T = TypeVar("T", bound="ExportSdtmigWorkbook")


@_attrs_define
class ExportSdtmigWorkbook:
    """
    Attributes:
        variables (Union[Unset, list['ExportSdtmigVariablesRow']]):
        datasets (Union[Unset, list['ExportSdtmigDatasetsRow']]):
    """

    variables: Union[Unset, list["ExportSdtmigVariablesRow"]] = UNSET
    datasets: Union[Unset, list["ExportSdtmigDatasetsRow"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        datasets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.datasets, Unset):
            datasets = []
            for datasets_item_data in self.datasets:
                datasets_item = datasets_item_data.to_dict()
                datasets.append(datasets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variables is not UNSET:
            field_dict["variables"] = variables
        if datasets is not UNSET:
            field_dict["datasets"] = datasets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_sdtmig_datasets_row import ExportSdtmigDatasetsRow
        from ..models.export_sdtmig_variables_row import ExportSdtmigVariablesRow

        d = dict(src_dict)
        variables = []
        _variables = d.pop("variables", UNSET)
        for variables_item_data in _variables or []:
            variables_item = ExportSdtmigVariablesRow.from_dict(variables_item_data)

            variables.append(variables_item)

        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
            datasets_item = ExportSdtmigDatasetsRow.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        export_sdtmig_workbook = cls(
            variables=variables,
            datasets=datasets,
        )

        export_sdtmig_workbook.additional_properties = d
        return export_sdtmig_workbook

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
