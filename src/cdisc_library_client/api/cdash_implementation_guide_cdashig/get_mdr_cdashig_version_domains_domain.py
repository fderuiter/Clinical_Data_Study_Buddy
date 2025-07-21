from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cdashig_domain import CdashigDomain
from ...models.default_error_response import DefaultErrorResponse
from ...types import Response


def _get_kwargs(
    version: str,
    domain: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mdr/cdashig/{version}/domains/{domain}".format(
            version=version,
            domain=domain,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CdashigDomain, DefaultErrorResponse]]:
    if response.status_code == 200:
        response_200 = CdashigDomain.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = DefaultErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = DefaultErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = DefaultErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = DefaultErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = DefaultErrorResponse.from_dict(response.json())

        return response_405
    if response.status_code == 406:
        response_406 = DefaultErrorResponse.from_dict(response.json())

        return response_406
    if response.status_code == 500:
        response_500 = DefaultErrorResponse.from_dict(response.json())

        return response_500
    if response.status_code == 503:
        response_503 = DefaultErrorResponse.from_dict(response.json())

        return response_503
    if response.status_code == 504:
        response_504 = DefaultErrorResponse.from_dict(response.json())

        return response_504
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CdashigDomain, DefaultErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str,
    domain: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CdashigDomain, DefaultErrorResponse]]:
    """Get CDASHIG Domain

    Args:
        version (str):  Example: 2-1.
        domain (str):  Example: VS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CdashigDomain, DefaultErrorResponse]]
    """

    kwargs = _get_kwargs(
        version=version,
        domain=domain,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    domain: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CdashigDomain, DefaultErrorResponse]]:
    """Get CDASHIG Domain

    Args:
        version (str):  Example: 2-1.
        domain (str):  Example: VS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CdashigDomain, DefaultErrorResponse]
    """

    return sync_detailed(
        version=version,
        domain=domain,
        client=client,
    ).parsed


async def asyncio_detailed(
    version: str,
    domain: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CdashigDomain, DefaultErrorResponse]]:
    """Get CDASHIG Domain

    Args:
        version (str):  Example: 2-1.
        domain (str):  Example: VS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CdashigDomain, DefaultErrorResponse]]
    """

    kwargs = _get_kwargs(
        version=version,
        domain=domain,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    domain: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CdashigDomain, DefaultErrorResponse]]:
    """Get CDASHIG Domain

    Args:
        version (str):  Example: 2-1.
        domain (str):  Example: VS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CdashigDomain, DefaultErrorResponse]
    """

    return (
        await asyncio_detailed(
            version=version,
            domain=domain,
            client=client,
        )
    ).parsed
