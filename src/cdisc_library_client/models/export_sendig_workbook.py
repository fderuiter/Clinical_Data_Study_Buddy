from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_sendig_datasets_row import ExportSendigDatasetsRow
    from ..models.export_sendig_variables_row import ExportSendigVariablesRow


T = TypeVar("T", bound="ExportSendigWorkbook")


@_attrs_define
class ExportSendigWorkbook:
    """
    Attributes:
        variables (Union[Unset, list['ExportSendigVariablesRow']]):
        datasets (Union[Unset, list['ExportSendigDatasetsRow']]):
    """

    variables: Union[Unset, list["ExportSendigVariablesRow"]] = UNSET
    datasets: Union[Unset, list["ExportSendigDatasetsRow"]] = UNSET
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
        from ..models.export_sendig_datasets_row import ExportSendigDatasetsRow
        from ..models.export_sendig_variables_row import ExportSendigVariablesRow

        d = dict(src_dict)
        variables = []
        _variables = d.pop("variables", UNSET)
        for variables_item_data in _variables or []:
            variables_item = ExportSendigVariablesRow.from_dict(variables_item_data)

            variables.append(variables_item)

        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
            datasets_item = ExportSendigDatasetsRow.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        export_sendig_workbook = cls(
            variables=variables,
            datasets=datasets,
        )

        export_sendig_workbook.additional_properties = d
        return export_sendig_workbook

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
