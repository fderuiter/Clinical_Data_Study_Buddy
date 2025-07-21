from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_error_response import DefaultErrorResponse
from ...models.root_ct_codelist import RootCtCodelist
from ...types import Response


def _get_kwargs(
    product_group: str,
    codelist: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mdr/root/ct/{product_group}/codelists/{codelist}".format(
            product_group=product_group,
            codelist=codelist,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DefaultErrorResponse, RootCtCodelist]]:
    if response.status_code == 200:
        response_200 = RootCtCodelist.from_dict(response.json())

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
) -> Response[Union[DefaultErrorResponse, RootCtCodelist]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_group: str,
    codelist: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DefaultErrorResponse, RootCtCodelist]]:
    """Get CDISC Library Root CT Codelist

    Args:
        product_group (str):  Example: sdtmct.
        codelist (str):  Example: C67154.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultErrorResponse, RootCtCodelist]]
    """

    kwargs = _get_kwargs(
        product_group=product_group,
        codelist=codelist,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_group: str,
    codelist: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DefaultErrorResponse, RootCtCodelist]]:
    """Get CDISC Library Root CT Codelist

    Args:
        product_group (str):  Example: sdtmct.
        codelist (str):  Example: C67154.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultErrorResponse, RootCtCodelist]
    """

    return sync_detailed(
        product_group=product_group,
        codelist=codelist,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_group: str,
    codelist: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DefaultErrorResponse, RootCtCodelist]]:
    """Get CDISC Library Root CT Codelist

    Args:
        product_group (str):  Example: sdtmct.
        codelist (str):  Example: C67154.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultErrorResponse, RootCtCodelist]]
    """

    kwargs = _get_kwargs(
        product_group=product_group,
        codelist=codelist,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_group: str,
    codelist: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DefaultErrorResponse, RootCtCodelist]]:
    """Get CDISC Library Root CT Codelist

    Args:
        product_group (str):  Example: sdtmct.
        codelist (str):  Example: C67154.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultErrorResponse, RootCtCodelist]
    """

    return (
        await asyncio_detailed(
            product_group=product_group,
            codelist=codelist,
            client=client,
        )
    ).parsed
