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
    from ..models.export_cdash_class_variables_row import ExportCdashClassVariablesRow
    from ..models.export_cdash_domain_variables_row import ExportCdashDomainVariablesRow


T = TypeVar("T", bound="ExportCdashTable")


@_attrs_define
class ExportCdashTable:
    """
    Attributes:
        class_variables (Union[Unset, list['ExportCdashClassVariablesRow']]):
        domain_variables (Union[Unset, list['ExportCdashDomainVariablesRow']]):
    """

    class_variables: Union[Unset, list["ExportCdashClassVariablesRow"]] = UNSET
    domain_variables: Union[Unset, list["ExportCdashDomainVariablesRow"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.class_variables, Unset):
            class_variables = []
            for class_variables_item_data in self.class_variables:
                class_variables_item = class_variables_item_data.to_dict()
                class_variables.append(class_variables_item)

        domain_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.domain_variables, Unset):
            domain_variables = []
            for domain_variables_item_data in self.domain_variables:
                domain_variables_item = domain_variables_item_data.to_dict()
                domain_variables.append(domain_variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_variables is not UNSET:
            field_dict["class-variables"] = class_variables
        if domain_variables is not UNSET:
            field_dict["domain-variables"] = domain_variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_cdash_class_variables_row import (
            ExportCdashClassVariablesRow,
        )
        from ..models.export_cdash_domain_variables_row import (
            ExportCdashDomainVariablesRow,
        )

        d = dict(src_dict)
        class_variables = []
        _class_variables = d.pop("class-variables", UNSET)
        for class_variables_item_data in _class_variables or []:
            class_variables_item = ExportCdashClassVariablesRow.from_dict(
                class_variables_item_data
            )

            class_variables.append(class_variables_item)

        domain_variables = []
        _domain_variables = d.pop("domain-variables", UNSET)
        for domain_variables_item_data in _domain_variables or []:
            domain_variables_item = ExportCdashDomainVariablesRow.from_dict(
                domain_variables_item_data
            )

            domain_variables.append(domain_variables_item)

        export_cdash_table = cls(
            class_variables=class_variables,
            domain_variables=domain_variables,
        )

        export_cdash_table.additional_properties = d
        return export_cdash_table

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
