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
    from ..models.root_ct_term_ref import RootCtTermRef


T = TypeVar("T", bound="QrsResponseLinks")


@_attrs_define
class QrsResponseLinks:
    """
    Attributes:
        qrs_response_orres (Union[Unset, RootCtTermRef]):
        qrs_response_orresu (Union[Unset, RootCtTermRef]):
        qrs_response_stresc (Union[Unset, RootCtTermRef]):
        qrs_response_strescu (Union[Unset, RootCtTermRef]):
    """

    qrs_response_orres: Union[Unset, "RootCtTermRef"] = UNSET
    qrs_response_orresu: Union[Unset, "RootCtTermRef"] = UNSET
    qrs_response_stresc: Union[Unset, "RootCtTermRef"] = UNSET
    qrs_response_strescu: Union[Unset, "RootCtTermRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qrs_response_orres: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_response_orres, Unset):
            qrs_response_orres = self.qrs_response_orres.to_dict()

        qrs_response_orresu: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_response_orresu, Unset):
            qrs_response_orresu = self.qrs_response_orresu.to_dict()

        qrs_response_stresc: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_response_stresc, Unset):
            qrs_response_stresc = self.qrs_response_stresc.to_dict()

        qrs_response_strescu: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_response_strescu, Unset):
            qrs_response_strescu = self.qrs_response_strescu.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qrs_response_orres is not UNSET:
            field_dict["qrsResponseORRES"] = qrs_response_orres
        if qrs_response_orresu is not UNSET:
            field_dict["qrsResponseORRESU"] = qrs_response_orresu
        if qrs_response_stresc is not UNSET:
            field_dict["qrsResponseSTRESC"] = qrs_response_stresc
        if qrs_response_strescu is not UNSET:
            field_dict["qrsResponseSTRESCU"] = qrs_response_strescu

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.root_ct_term_ref import RootCtTermRef

        d = dict(src_dict)
        _qrs_response_orres = d.pop("qrsResponseORRES", UNSET)
        qrs_response_orres: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_response_orres, Unset):
            qrs_response_orres = UNSET
        else:
            qrs_response_orres = RootCtTermRef.from_dict(_qrs_response_orres)

        _qrs_response_orresu = d.pop("qrsResponseORRESU", UNSET)
        qrs_response_orresu: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_response_orresu, Unset):
            qrs_response_orresu = UNSET
        else:
            qrs_response_orresu = RootCtTermRef.from_dict(_qrs_response_orresu)

        _qrs_response_stresc = d.pop("qrsResponseSTRESC", UNSET)
        qrs_response_stresc: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_response_stresc, Unset):
            qrs_response_stresc = UNSET
        else:
            qrs_response_stresc = RootCtTermRef.from_dict(_qrs_response_stresc)

        _qrs_response_strescu = d.pop("qrsResponseSTRESCU", UNSET)
        qrs_response_strescu: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_response_strescu, Unset):
            qrs_response_strescu = UNSET
        else:
            qrs_response_strescu = RootCtTermRef.from_dict(_qrs_response_strescu)

        qrs_response_links = cls(
            qrs_response_orres=qrs_response_orres,
            qrs_response_orresu=qrs_response_orresu,
            qrs_response_stresc=qrs_response_stresc,
            qrs_response_strescu=qrs_response_strescu,
        )

        qrs_response_links.additional_properties = d
        return qrs_response_links

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
