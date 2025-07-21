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


T = TypeVar("T", bound="ExportSdtmVariablesTable")


@_attrs_define
class ExportSdtmVariablesTable:
    """
    Attributes:
        class_variables (Union[Unset, list['ExportSdtmClassVariablesRow']]):
        dataset_variables (Union[Unset, list['ExportSdtmDatasetVariablesRow']]):
    """

    class_variables: Union[Unset, list["ExportSdtmClassVariablesRow"]] = UNSET
    dataset_variables: Union[Unset, list["ExportSdtmDatasetVariablesRow"]] = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_variables is not UNSET:
            field_dict["class-variables"] = class_variables
        if dataset_variables is not UNSET:
            field_dict["dataset-variables"] = dataset_variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_sdtm_class_variables_row import ExportSdtmClassVariablesRow
        from ..models.export_sdtm_dataset_variables_row import (
            ExportSdtmDatasetVariablesRow,
        )

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

        export_sdtm_variables_table = cls(
            class_variables=class_variables,
            dataset_variables=dataset_variables,
        )

        export_sdtm_variables_table.additional_properties = d
        return export_sdtm_variables_table

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
