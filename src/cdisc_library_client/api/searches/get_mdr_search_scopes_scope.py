from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_search_scopes import DefaultSearchScopes
from ...models.scope_values import ScopeValues
from ...types import Response


def _get_kwargs(
    scope: DefaultSearchScopes,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/mdr/search/scopes/{scope}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ScopeValues]:
    if response.status_code == 200:
        response_200 = ScopeValues.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ScopeValues]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scope: DefaultSearchScopes,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ScopeValues]:
    """Get Search Results Limited to Scope

    Args:
        scope (DefaultSearchScopes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScopeValues]
    """

    kwargs = _get_kwargs(
        scope=scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scope: DefaultSearchScopes,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ScopeValues]:
    """Get Search Results Limited to Scope

    Args:
        scope (DefaultSearchScopes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScopeValues
    """

    return sync_detailed(
        scope=scope,
        client=client,
    ).parsed


async def asyncio_detailed(
    scope: DefaultSearchScopes,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ScopeValues]:
    """Get Search Results Limited to Scope

    Args:
        scope (DefaultSearchScopes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScopeValues]
    """

    kwargs = _get_kwargs(
        scope=scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scope: DefaultSearchScopes,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ScopeValues]:
    """Get Search Results Limited to Scope

    Args:
        scope (DefaultSearchScopes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScopeValues
    """

    return (
        await asyncio_detailed(
            scope=scope,
            client=client,
        )
    ).parsed
