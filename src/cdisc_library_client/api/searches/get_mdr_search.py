from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_error_response import DefaultErrorResponse
from ...models.default_search_response import DefaultSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    highlight: Union[Unset, str] = UNSET,
    start: Union[Unset, float] = 0.0,
    page_size: Union[Unset, float] = 100.0,
    class_: Union[Unset, str] = UNSET,
    codelist: Union[Unset, str] = UNSET,
    concept_id: Union[Unset, str] = UNSET,
    core: Union[Unset, str] = UNSET,
    data_structure: Union[Unset, str] = UNSET,
    dataset_structure: Union[Unset, str] = UNSET,
    definition: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    effective_date: Union[Unset, str] = UNSET,
    extensible: Union[Unset, str] = UNSET,
    href: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    measure_type: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    preferred_term: Union[Unset, str] = UNSET,
    product: Union[Unset, str] = UNSET,
    product_group: Union[Unset, str] = UNSET,
    registration_status: Union[Unset, str] = UNSET,
    role_description: Union[Unset, str] = UNSET,
    sdtm_target: Union[Unset, str] = UNSET,
    simple_datatype: Union[Unset, str] = UNSET,
    submission_value: Union[Unset, str] = UNSET,
    synonyms: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    ui_href: Union[Unset, str] = UNSET,
    value_domain: Union[Unset, str] = UNSET,
    variable_set: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["highlight"] = highlight

    params["start"] = start

    params["pageSize"] = page_size

    params["class"] = class_

    params["codelist"] = codelist

    params["conceptId"] = concept_id

    params["core"] = core

    params["dataStructure"] = data_structure

    params["datasetStructure"] = dataset_structure

    params["definition"] = definition

    params["description"] = description

    params["domain"] = domain

    params["effectiveDate"] = effective_date

    params["extensible"] = extensible

    params["href"] = href

    params["label"] = label

    params["measureType"] = measure_type

    params["name"] = name

    params["preferredTerm"] = preferred_term

    params["product"] = product

    params["productGroup"] = product_group

    params["registrationStatus"] = registration_status

    params["roleDescription"] = role_description

    params["sdtmTarget"] = sdtm_target

    params["simpleDatatype"] = simple_datatype

    params["submissionValue"] = submission_value

    params["synonyms"] = synonyms

    params["type"] = type_

    params["uiHref"] = ui_href

    params["valueDomain"] = value_domain

    params["variableSet"] = variable_set

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mdr/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DefaultErrorResponse, DefaultSearchResponse]]:
    if response.status_code == 200:
        response_200 = DefaultSearchResponse.from_dict(response.json())

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
) -> Response[Union[DefaultErrorResponse, DefaultSearchResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    highlight: Union[Unset, str] = UNSET,
    start: Union[Unset, float] = 0.0,
    page_size: Union[Unset, float] = 100.0,
    class_: Union[Unset, str] = UNSET,
    codelist: Union[Unset, str] = UNSET,
    concept_id: Union[Unset, str] = UNSET,
    core: Union[Unset, str] = UNSET,
    data_structure: Union[Unset, str] = UNSET,
    dataset_structure: Union[Unset, str] = UNSET,
    definition: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    effective_date: Union[Unset, str] = UNSET,
    extensible: Union[Unset, str] = UNSET,
    href: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    measure_type: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    preferred_term: Union[Unset, str] = UNSET,
    product: Union[Unset, str] = UNSET,
    product_group: Union[Unset, str] = UNSET,
    registration_status: Union[Unset, str] = UNSET,
    role_description: Union[Unset, str] = UNSET,
    sdtm_target: Union[Unset, str] = UNSET,
    simple_datatype: Union[Unset, str] = UNSET,
    submission_value: Union[Unset, str] = UNSET,
    synonyms: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    ui_href: Union[Unset, str] = UNSET,
    value_domain: Union[Unset, str] = UNSET,
    variable_set: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[Union[DefaultErrorResponse, DefaultSearchResponse]]:
    """Get Search Results Across CDISC Library

    Args:
        q (str):
        highlight (Union[Unset, str]):
        start (Union[Unset, float]):  Default: 0.0.
        page_size (Union[Unset, float]):  Default: 100.0.
        class_ (Union[Unset, str]):
        codelist (Union[Unset, str]):
        concept_id (Union[Unset, str]):
        core (Union[Unset, str]):
        data_structure (Union[Unset, str]):
        dataset_structure (Union[Unset, str]):
        definition (Union[Unset, str]):
        description (Union[Unset, str]):
        domain (Union[Unset, str]):
        effective_date (Union[Unset, str]):
        extensible (Union[Unset, str]):
        href (Union[Unset, str]):
        label (Union[Unset, str]):
        measure_type (Union[Unset, str]):
        name (Union[Unset, str]):
        preferred_term (Union[Unset, str]):
        product (Union[Unset, str]):
        product_group (Union[Unset, str]):
        registration_status (Union[Unset, str]):
        role_description (Union[Unset, str]):
        sdtm_target (Union[Unset, str]):
        simple_datatype (Union[Unset, str]):
        submission_value (Union[Unset, str]):
        synonyms (Union[Unset, str]):
        type_ (Union[Unset, str]):
        ui_href (Union[Unset, str]):
        value_domain (Union[Unset, str]):
        variable_set (Union[Unset, str]):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultErrorResponse, DefaultSearchResponse]]
    """

    kwargs = _get_kwargs(
        q=q,
        highlight=highlight,
        start=start,
        page_size=page_size,
        class_=class_,
        codelist=codelist,
        concept_id=concept_id,
        core=core,
        data_structure=data_structure,
        dataset_structure=dataset_structure,
        definition=definition,
        description=description,
        domain=domain,
        effective_date=effective_date,
        extensible=extensible,
        href=href,
        label=label,
        measure_type=measure_type,
        name=name,
        preferred_term=preferred_term,
        product=product,
        product_group=product_group,
        registration_status=registration_status,
        role_description=role_description,
        sdtm_target=sdtm_target,
        simple_datatype=simple_datatype,
        submission_value=submission_value,
        synonyms=synonyms,
        type_=type_,
        ui_href=ui_href,
        value_domain=value_domain,
        variable_set=variable_set,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    highlight: Union[Unset, str] = UNSET,
    start: Union[Unset, float] = 0.0,
    page_size: Union[Unset, float] = 100.0,
    class_: Union[Unset, str] = UNSET,
    codelist: Union[Unset, str] = UNSET,
    concept_id: Union[Unset, str] = UNSET,
    core: Union[Unset, str] = UNSET,
    data_structure: Union[Unset, str] = UNSET,
    dataset_structure: Union[Unset, str] = UNSET,
    definition: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    effective_date: Union[Unset, str] = UNSET,
    extensible: Union[Unset, str] = UNSET,
    href: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    measure_type: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    preferred_term: Union[Unset, str] = UNSET,
    product: Union[Unset, str] = UNSET,
    product_group: Union[Unset, str] = UNSET,
    registration_status: Union[Unset, str] = UNSET,
    role_description: Union[Unset, str] = UNSET,
    sdtm_target: Union[Unset, str] = UNSET,
    simple_datatype: Union[Unset, str] = UNSET,
    submission_value: Union[Unset, str] = UNSET,
    synonyms: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    ui_href: Union[Unset, str] = UNSET,
    value_domain: Union[Unset, str] = UNSET,
    variable_set: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[Union[DefaultErrorResponse, DefaultSearchResponse]]:
    """Get Search Results Across CDISC Library

    Args:
        q (str):
        highlight (Union[Unset, str]):
        start (Union[Unset, float]):  Default: 0.0.
        page_size (Union[Unset, float]):  Default: 100.0.
        class_ (Union[Unset, str]):
        codelist (Union[Unset, str]):
        concept_id (Union[Unset, str]):
        core (Union[Unset, str]):
        data_structure (Union[Unset, str]):
        dataset_structure (Union[Unset, str]):
        definition (Union[Unset, str]):
        description (Union[Unset, str]):
        domain (Union[Unset, str]):
        effective_date (Union[Unset, str]):
        extensible (Union[Unset, str]):
        href (Union[Unset, str]):
        label (Union[Unset, str]):
        measure_type (Union[Unset, str]):
        name (Union[Unset, str]):
        preferred_term (Union[Unset, str]):
        product (Union[Unset, str]):
        product_group (Union[Unset, str]):
        registration_status (Union[Unset, str]):
        role_description (Union[Unset, str]):
        sdtm_target (Union[Unset, str]):
        simple_datatype (Union[Unset, str]):
        submission_value (Union[Unset, str]):
        synonyms (Union[Unset, str]):
        type_ (Union[Unset, str]):
        ui_href (Union[Unset, str]):
        value_domain (Union[Unset, str]):
        variable_set (Union[Unset, str]):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultErrorResponse, DefaultSearchResponse]
    """

    return sync_detailed(
        client=client,
        q=q,
        highlight=highlight,
        start=start,
        page_size=page_size,
        class_=class_,
        codelist=codelist,
        concept_id=concept_id,
        core=core,
        data_structure=data_structure,
        dataset_structure=dataset_structure,
        definition=definition,
        description=description,
        domain=domain,
        effective_date=effective_date,
        extensible=extensible,
        href=href,
        label=label,
        measure_type=measure_type,
        name=name,
        preferred_term=preferred_term,
        product=product,
        product_group=product_group,
        registration_status=registration_status,
        role_description=role_description,
        sdtm_target=sdtm_target,
        simple_datatype=simple_datatype,
        submission_value=submission_value,
        synonyms=synonyms,
        type_=type_,
        ui_href=ui_href,
        value_domain=value_domain,
        variable_set=variable_set,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    highlight: Union[Unset, str] = UNSET,
    start: Union[Unset, float] = 0.0,
    page_size: Union[Unset, float] = 100.0,
    class_: Union[Unset, str] = UNSET,
    codelist: Union[Unset, str] = UNSET,
    concept_id: Union[Unset, str] = UNSET,
    core: Union[Unset, str] = UNSET,
    data_structure: Union[Unset, str] = UNSET,
    dataset_structure: Union[Unset, str] = UNSET,
    definition: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    effective_date: Union[Unset, str] = UNSET,
    extensible: Union[Unset, str] = UNSET,
    href: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    measure_type: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    preferred_term: Union[Unset, str] = UNSET,
    product: Union[Unset, str] = UNSET,
    product_group: Union[Unset, str] = UNSET,
    registration_status: Union[Unset, str] = UNSET,
    role_description: Union[Unset, str] = UNSET,
    sdtm_target: Union[Unset, str] = UNSET,
    simple_datatype: Union[Unset, str] = UNSET,
    submission_value: Union[Unset, str] = UNSET,
    synonyms: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    ui_href: Union[Unset, str] = UNSET,
    value_domain: Union[Unset, str] = UNSET,
    variable_set: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[Union[DefaultErrorResponse, DefaultSearchResponse]]:
    """Get Search Results Across CDISC Library

    Args:
        q (str):
        highlight (Union[Unset, str]):
        start (Union[Unset, float]):  Default: 0.0.
        page_size (Union[Unset, float]):  Default: 100.0.
        class_ (Union[Unset, str]):
        codelist (Union[Unset, str]):
        concept_id (Union[Unset, str]):
        core (Union[Unset, str]):
        data_structure (Union[Unset, str]):
        dataset_structure (Union[Unset, str]):
        definition (Union[Unset, str]):
        description (Union[Unset, str]):
        domain (Union[Unset, str]):
        effective_date (Union[Unset, str]):
        extensible (Union[Unset, str]):
        href (Union[Unset, str]):
        label (Union[Unset, str]):
        measure_type (Union[Unset, str]):
        name (Union[Unset, str]):
        preferred_term (Union[Unset, str]):
        product (Union[Unset, str]):
        product_group (Union[Unset, str]):
        registration_status (Union[Unset, str]):
        role_description (Union[Unset, str]):
        sdtm_target (Union[Unset, str]):
        simple_datatype (Union[Unset, str]):
        submission_value (Union[Unset, str]):
        synonyms (Union[Unset, str]):
        type_ (Union[Unset, str]):
        ui_href (Union[Unset, str]):
        value_domain (Union[Unset, str]):
        variable_set (Union[Unset, str]):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultErrorResponse, DefaultSearchResponse]]
    """

    kwargs = _get_kwargs(
        q=q,
        highlight=highlight,
        start=start,
        page_size=page_size,
        class_=class_,
        codelist=codelist,
        concept_id=concept_id,
        core=core,
        data_structure=data_structure,
        dataset_structure=dataset_structure,
        definition=definition,
        description=description,
        domain=domain,
        effective_date=effective_date,
        extensible=extensible,
        href=href,
        label=label,
        measure_type=measure_type,
        name=name,
        preferred_term=preferred_term,
        product=product,
        product_group=product_group,
        registration_status=registration_status,
        role_description=role_description,
        sdtm_target=sdtm_target,
        simple_datatype=simple_datatype,
        submission_value=submission_value,
        synonyms=synonyms,
        type_=type_,
        ui_href=ui_href,
        value_domain=value_domain,
        variable_set=variable_set,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    highlight: Union[Unset, str] = UNSET,
    start: Union[Unset, float] = 0.0,
    page_size: Union[Unset, float] = 100.0,
    class_: Union[Unset, str] = UNSET,
    codelist: Union[Unset, str] = UNSET,
    concept_id: Union[Unset, str] = UNSET,
    core: Union[Unset, str] = UNSET,
    data_structure: Union[Unset, str] = UNSET,
    dataset_structure: Union[Unset, str] = UNSET,
    definition: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    effective_date: Union[Unset, str] = UNSET,
    extensible: Union[Unset, str] = UNSET,
    href: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    measure_type: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    preferred_term: Union[Unset, str] = UNSET,
    product: Union[Unset, str] = UNSET,
    product_group: Union[Unset, str] = UNSET,
    registration_status: Union[Unset, str] = UNSET,
    role_description: Union[Unset, str] = UNSET,
    sdtm_target: Union[Unset, str] = UNSET,
    simple_datatype: Union[Unset, str] = UNSET,
    submission_value: Union[Unset, str] = UNSET,
    synonyms: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    ui_href: Union[Unset, str] = UNSET,
    value_domain: Union[Unset, str] = UNSET,
    variable_set: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[Union[DefaultErrorResponse, DefaultSearchResponse]]:
    """Get Search Results Across CDISC Library

    Args:
        q (str):
        highlight (Union[Unset, str]):
        start (Union[Unset, float]):  Default: 0.0.
        page_size (Union[Unset, float]):  Default: 100.0.
        class_ (Union[Unset, str]):
        codelist (Union[Unset, str]):
        concept_id (Union[Unset, str]):
        core (Union[Unset, str]):
        data_structure (Union[Unset, str]):
        dataset_structure (Union[Unset, str]):
        definition (Union[Unset, str]):
        description (Union[Unset, str]):
        domain (Union[Unset, str]):
        effective_date (Union[Unset, str]):
        extensible (Union[Unset, str]):
        href (Union[Unset, str]):
        label (Union[Unset, str]):
        measure_type (Union[Unset, str]):
        name (Union[Unset, str]):
        preferred_term (Union[Unset, str]):
        product (Union[Unset, str]):
        product_group (Union[Unset, str]):
        registration_status (Union[Unset, str]):
        role_description (Union[Unset, str]):
        sdtm_target (Union[Unset, str]):
        simple_datatype (Union[Unset, str]):
        submission_value (Union[Unset, str]):
        synonyms (Union[Unset, str]):
        type_ (Union[Unset, str]):
        ui_href (Union[Unset, str]):
        value_domain (Union[Unset, str]):
        variable_set (Union[Unset, str]):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultErrorResponse, DefaultSearchResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            highlight=highlight,
            start=start,
            page_size=page_size,
            class_=class_,
            codelist=codelist,
            concept_id=concept_id,
            core=core,
            data_structure=data_structure,
            dataset_structure=dataset_structure,
            definition=definition,
            description=description,
            domain=domain,
            effective_date=effective_date,
            extensible=extensible,
            href=href,
            label=label,
            measure_type=measure_type,
            name=name,
            preferred_term=preferred_term,
            product=product,
            product_group=product_group,
            registration_status=registration_status,
            role_description=role_description,
            sdtm_target=sdtm_target,
            simple_datatype=simple_datatype,
            submission_value=submission_value,
            synonyms=synonyms,
            type_=type_,
            ui_href=ui_href,
            value_domain=value_domain,
            variable_set=variable_set,
            version=version,
        )
    ).parsed
