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
    from ..models.export_sdtm_class_variables_row import ExportSdtmClassVariablesRow
    from ..models.export_sdtm_dataset_variables_row import ExportSdtmDatasetVariablesRow
    from ..models.export_sdtm_datasets_row import ExportSdtmDatasetsRow


T = TypeVar("T", bound="ExportSdtmWorkbook")


@_attrs_define
class ExportSdtmWorkbook:
    """
    Attributes:
        class_variables (Union[Unset, list['ExportSdtmClassVariablesRow']]):
        dataset_variables (Union[Unset, list['ExportSdtmDatasetVariablesRow']]):
        datasets (Union[Unset, list['ExportSdtmDatasetsRow']]):
    """

    class_variables: Union[Unset, list["ExportSdtmClassVariablesRow"]] = UNSET
    dataset_variables: Union[Unset, list["ExportSdtmDatasetVariablesRow"]] = UNSET
    datasets: Union[Unset, list["ExportSdtmDatasetsRow"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.class_variables, Unset):
            class_variables = []
            for class_variables_item_data in self.class_variables:
                class_variables_item = class_variables_item_data.to_dict()
                class_variables.append(class_variables_item)

        dataset_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dataset_variables, Unset):
            dataset_variables = []
            for dataset_variables_item_data in self.dataset_variables:
                dataset_variables_item = dataset_variables_item_data.to_dict()
                dataset_variables.append(dataset_variables_item)

        datasets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.datasets, Unset):
            datasets = []
            for datasets_item_data in self.datasets:
                datasets_item = datasets_item_data.to_dict()
                datasets.append(datasets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_variables is not UNSET:
            field_dict["class-variables"] = class_variables
        if dataset_variables is not UNSET:
            field_dict["dataset-variables"] = dataset_variables
        if datasets is not UNSET:
            field_dict["datasets"] = datasets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_sdtm_class_variables_row import ExportSdtmClassVariablesRow
        from ..models.export_sdtm_dataset_variables_row import (
            ExportSdtmDatasetVariablesRow,
        )
        from ..models.export_sdtm_datasets_row import ExportSdtmDatasetsRow

        d = dict(src_dict)
        class_variables = []
        _class_variables = d.pop("class-variables", UNSET)
        for class_variables_item_data in _class_variables or []:
            class_variables_item = ExportSdtmClassVariablesRow.from_dict(
                class_variables_item_data
            )

            class_variables.append(class_variables_item)

        dataset_variables = []
        _dataset_variables = d.pop("dataset-variables", UNSET)
        for dataset_variables_item_data in _dataset_variables or []:
            dataset_variables_item = ExportSdtmDatasetVariablesRow.from_dict(
                dataset_variables_item_data
            )

            dataset_variables.append(dataset_variables_item)

        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
            datasets_item = ExportSdtmDatasetsRow.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        export_sdtm_workbook = cls(
            class_variables=class_variables,
            dataset_variables=dataset_variables,
            datasets=datasets,
        )

        export_sdtm_workbook.additional_properties = d
        return export_sdtm_workbook

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
