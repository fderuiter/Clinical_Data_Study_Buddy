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
    from ..models.productgroup_data_analysis import ProductgroupDataAnalysis
    from ..models.productgroup_data_collection import ProductgroupDataCollection
    from ..models.productgroup_data_tabulation import ProductgroupDataTabulation
    from ..models.productgroup_qrs import ProductgroupQrs
    from ..models.productgroup_terminology import ProductgroupTerminology
    from ..models.products_ref import ProductsRef


T = TypeVar("T", bound="ProductsLinks")


@_attrs_define
class ProductsLinks:
    """
    Attributes:
        self_ (Union[Unset, ProductsRef]):
        data_collection (Union[Unset, ProductgroupDataCollection]):
        data_tabulation (Union[Unset, ProductgroupDataTabulation]):
        data_analysis (Union[Unset, ProductgroupDataAnalysis]):
        terminology (Union[Unset, ProductgroupTerminology]):
        measure (Union[Unset, ProductgroupQrs]):
    """

    self_: Union[Unset, "ProductsRef"] = UNSET
    data_collection: Union[Unset, "ProductgroupDataCollection"] = UNSET
    data_tabulation: Union[Unset, "ProductgroupDataTabulation"] = UNSET
    data_analysis: Union[Unset, "ProductgroupDataAnalysis"] = UNSET
    terminology: Union[Unset, "ProductgroupTerminology"] = UNSET
    measure: Union[Unset, "ProductgroupQrs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        data_collection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_collection, Unset):
            data_collection = self.data_collection.to_dict()

        data_tabulation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_tabulation, Unset):
            data_tabulation = self.data_tabulation.to_dict()

        data_analysis: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_analysis, Unset):
            data_analysis = self.data_analysis.to_dict()

        terminology: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.terminology, Unset):
            terminology = self.terminology.to_dict()

        measure: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.measure, Unset):
            measure = self.measure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if data_collection is not UNSET:
            field_dict["data-collection"] = data_collection
        if data_tabulation is not UNSET:
            field_dict["data-tabulation"] = data_tabulation
        if data_analysis is not UNSET:
            field_dict["data-analysis"] = data_analysis
        if terminology is not UNSET:
            field_dict["terminology"] = terminology
        if measure is not UNSET:
            field_dict["measure"] = measure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.productgroup_data_analysis import ProductgroupDataAnalysis
        from ..models.productgroup_data_collection import ProductgroupDataCollection
        from ..models.productgroup_data_tabulation import ProductgroupDataTabulation
        from ..models.productgroup_qrs import ProductgroupQrs
        from ..models.productgroup_terminology import ProductgroupTerminology
        from ..models.products_ref import ProductsRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, ProductsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = ProductsRef.from_dict(_self_)

        _data_collection = d.pop("data-collection", UNSET)
        data_collection: Union[Unset, ProductgroupDataCollection]
        if isinstance(_data_collection, Unset):
            data_collection = UNSET
        else:
            data_collection = ProductgroupDataCollection.from_dict(_data_collection)

        _data_tabulation = d.pop("data-tabulation", UNSET)
        data_tabulation: Union[Unset, ProductgroupDataTabulation]
        if isinstance(_data_tabulation, Unset):
            data_tabulation = UNSET
        else:
            data_tabulation = ProductgroupDataTabulation.from_dict(_data_tabulation)

        _data_analysis = d.pop("data-analysis", UNSET)
        data_analysis: Union[Unset, ProductgroupDataAnalysis]
        if isinstance(_data_analysis, Unset):
            data_analysis = UNSET
        else:
            data_analysis = ProductgroupDataAnalysis.from_dict(_data_analysis)

        _terminology = d.pop("terminology", UNSET)
        terminology: Union[Unset, ProductgroupTerminology]
        if isinstance(_terminology, Unset):
            terminology = UNSET
        else:
            terminology = ProductgroupTerminology.from_dict(_terminology)

        _measure = d.pop("measure", UNSET)
        measure: Union[Unset, ProductgroupQrs]
        if isinstance(_measure, Unset):
            measure = UNSET
        else:
            measure = ProductgroupQrs.from_dict(_measure)

        products_links = cls(
            self_=self_,
            data_collection=data_collection,
            data_tabulation=data_tabulation,
            data_analysis=data_analysis,
            terminology=terminology,
            measure=measure,
        )

        products_links.additional_properties = d
        return products_links

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
