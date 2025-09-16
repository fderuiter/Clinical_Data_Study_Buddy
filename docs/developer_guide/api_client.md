# CDISC Library API Client

This project includes a generated Python client for the CDISC Library API, located in the `src/cdisc_library_client` directory. This client is the recommended way to interact with the CDISC Library API.

## Authentication

To use the client, you will need a CDISC Library API key. You can get one from the [CDISC Library website](https://library.cdisc.org/).

The recommended way to configure the API key is to set the `CDISC_PRIMARY_KEY` environment variable. You can do this by creating a `.env` file in the root of the project:

```
CDISC_PRIMARY_KEY="your-api-key-here"
```

The application provides a utility function, `get_client`, which automatically creates an authenticated client with the necessary settings.

```python
from clinical_data_study_buddy.services.cdisc_library_service import get_client

client = get_client()
```

## Making API Calls

The client is organized into different modules based on the tags in the OpenAPI specification. For example, to get a list of CDASHIG versions, you can use the `get_mdr_cdashig_version` function from the `cdash_implementation_guide_cdashig` module:

```python
from cdisc_library_client.api.cdash_implementation_guide_cdashig import get_mdr_cdashig_version
from clinical_data_study_buddy.services.cdisc_library_service import get_client

client = get_client()
response = get_mdr_cdashig_version.sync(client=client, version="v2.3")

# The response is a Pydantic model representing the API response
print(response)
```

Each API endpoint has a corresponding function in the client. The function name is derived from the endpoint's operation ID in the OpenAPI specification.

## High-level Harvesting

For convenience, the project includes a high-level `harvest` module that simplifies the process of fetching and parsing data from the CDISC Library.

The `harvest` function in `src/cdisc_library_client/harvest.py` uses the API client to fetch all the data for a given standard and converts it into a list of `Form` objects.

Here's how you can use it:

```python
from cdisc_library_client.harvest import harvest

# The API key is read from the environment variable
forms = harvest(ig_filter="2.3")
```

This is the recommended way to get CRF data from the CDISC Library, as it handles all the details of pagination and data parsing for you.
