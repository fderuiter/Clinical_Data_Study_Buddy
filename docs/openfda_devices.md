# openFDA Device Module

This document provides an overview of the openFDA device module, its components, and how to use them.

## Components

The openFDA device module is organized into the following components:

- **`client.py`**: An asynchronous HTTP client for interacting with the openFDA API. It includes features like rate limiting, caching, and automatic retries.
- **`query.py`**: A set of functions for building query parameters for the openFDA API.
- **`models.py`**: Pydantic models for the various openFDA device endpoints.
- **`devices/`**: A directory containing device-specific accessors for each openFDA endpoint.
- **`mappers.py`**: Functions for joining and enriching data from different openFDA endpoints.
- **`ingest.py`**: Functionality for downloading and processing bulk data from the openFDA download portal.
- **`cli/openfda_cli.py`**: A command-line interface for interacting with the openFDA module.

## Usage

### Client

The `OpenFDAClient` can be used to make requests to the openFDA API.

```python
from crfgen.openfda.client import OpenFDAClient

client = OpenFDAClient()
response = await client.get("/device/udi.json", params={"limit": 1})
print(response.json())
```

### Accessors

The device-specific accessors provide a higher-level interface for fetching data from the openFDA API.

```python
from crfgen.openfda.client import OpenFDAClient
from crfgen.openfda.devices.udi import UDIAccessor

client = OpenFDAClient()
accessor = UDIAccessor(client)
results = await accessor.fetch(search='device_name:"pacemaker"')
```

### CLI

The command-line interface can be used to interact with the openFDA module from the terminal.

```bash
# Fetch UDI data
crfgen openfda device udi --search 'device_name:"pacemaker"' --limit 10

# Download bulk data
crfgen openfda ingest download --endpoint device/udi
```
