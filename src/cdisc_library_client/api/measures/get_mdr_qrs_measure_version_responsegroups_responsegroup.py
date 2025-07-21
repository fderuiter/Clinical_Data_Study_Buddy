from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_error_response import DefaultErrorResponse
from ...models.qrs_responsegroup import QrsResponsegroup
from ...types import Response


def _get_kwargs(
    measure: str,
    version: str,
    responsegroup: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mdr/qrs/{measure}/{version}/responsegroups/{responsegroup}".format(
            measure=measure,
            version=version,
            responsegroup=responsegroup,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DefaultErrorResponse, QrsResponsegroup]]:
    if response.status_code == 200:
        response_200 = QrsResponsegroup.from_dict(response.json())

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
) -> Response[Union[DefaultErrorResponse, QrsResponsegroup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    measure: str,
    version: str,
    responsegroup: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DefaultErrorResponse, QrsResponsegroup]]:
    """Get QRS Response Group

    Args:
        measure (str):  Example: AIMS1.
        version (str):  Example: 1-0.
        responsegroup (str):  Example: AIMS1.11to12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultErrorResponse, QrsResponsegroup]]
    """

    kwargs = _get_kwargs(
        measure=measure,
        version=version,
        responsegroup=responsegroup,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    measure: str,
    version: str,
    responsegroup: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DefaultErrorResponse, QrsResponsegroup]]:
    """Get QRS Response Group

    Args:
        measure (str):  Example: AIMS1.
        version (str):  Example: 1-0.
        responsegroup (str):  Example: AIMS1.11to12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultErrorResponse, QrsResponsegroup]
    """

    return sync_detailed(
        measure=measure,
        version=version,
        responsegroup=responsegroup,
        client=client,
    ).parsed


async def asyncio_detailed(
    measure: str,
    version: str,
    responsegroup: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DefaultErrorResponse, QrsResponsegroup]]:
    """Get QRS Response Group

    Args:
        measure (str):  Example: AIMS1.
        version (str):  Example: 1-0.
        responsegroup (str):  Example: AIMS1.11to12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultErrorResponse, QrsResponsegroup]]
    """

    kwargs = _get_kwargs(
        measure=measure,
        version=version,
        responsegroup=responsegroup,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    measure: str,
    version: str,
    responsegroup: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DefaultErrorResponse, QrsResponsegroup]]:
    """Get QRS Response Group

    Args:
        measure (str):  Example: AIMS1.
        version (str):  Example: 1-0.
        responsegroup (str):  Example: AIMS1.11to12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultErrorResponse, QrsResponsegroup]
    """

    return (
        await asyncio_detailed(
            measure=measure,
            version=version,
            responsegroup=responsegroup,
            client=client,
        )
    ).parsed
