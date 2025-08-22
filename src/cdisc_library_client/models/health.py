from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Health")


@_attrs_define
class Health:
    """
    Attributes:
        healthy (Union[Unset, bool]):
        ldap_authentication_healthy (Union[Unset, bool]):
        ldap_authorization_healthy (Union[Unset, bool]):
        database_healthy (Union[Unset, bool]):
        es_healthy (Union[Unset, bool]):
    """

    healthy: Union[Unset, bool] = UNSET
    ldap_authentication_healthy: Union[Unset, bool] = UNSET
    ldap_authorization_healthy: Union[Unset, bool] = UNSET
    database_healthy: Union[Unset, bool] = UNSET
    es_healthy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        healthy = self.healthy

        ldap_authentication_healthy = self.ldap_authentication_healthy

        ldap_authorization_healthy = self.ldap_authorization_healthy

        database_healthy = self.database_healthy

        es_healthy = self.es_healthy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if healthy is not UNSET:
            field_dict["healthy"] = healthy
        if ldap_authentication_healthy is not UNSET:
            field_dict["ldapAuthenticationHealthy"] = ldap_authentication_healthy
        if ldap_authorization_healthy is not UNSET:
            field_dict["ldapAuthorizationHealthy"] = ldap_authorization_healthy
        if database_healthy is not UNSET:
            field_dict["databaseHealthy"] = database_healthy
        if es_healthy is not UNSET:
            field_dict["esHealthy"] = es_healthy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        healthy = d.pop("healthy", UNSET)

        ldap_authentication_healthy = d.pop("ldapAuthenticationHealthy", UNSET)

        ldap_authorization_healthy = d.pop("ldapAuthorizationHealthy", UNSET)

        database_healthy = d.pop("databaseHealthy", UNSET)

        es_healthy = d.pop("esHealthy", UNSET)

        health = cls(
            healthy=healthy,
            ldap_authentication_healthy=ldap_authentication_healthy,
            ldap_authorization_healthy=ldap_authorization_healthy,
            database_healthy=database_healthy,
            es_healthy=es_healthy,
        )

        health.additional_properties = d
        return health

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
