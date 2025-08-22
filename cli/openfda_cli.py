import asyncio
import json
from typing import Optional

import typer
from src.crfgen.openfda.client import OpenFDAClient
from src.crfgen.openfda.devices.udi import UDIAccessor
from src.crfgen.openfda.ingest import download_and_extract

app = typer.Typer()
device_app = typer.Typer()
app.add_typer(device_app, name="device")
ingest_app = typer.Typer()
app.add_typer(ingest_app, name="ingest")

from src.crfgen.openfda.devices.event import MAUDEAccessor
from src.crfgen.openfda.devices.recall import RecallAccessor
from src.crfgen.openfda.devices.enforcement import EnforcementAccessor
from src.crfgen.openfda.devices.classification import ClassificationAccessor
from src.crfgen.openfda.devices.k510 import K510Accessor
from src.crfgen.openfda.devices.pma import PMAAccessor
from src.crfgen.openfda.devices.reglist import RegListAccessor

@device_app.command("udi")
def udi(
    search: Optional[str] = typer.Option(None, "--search", "-s"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    skip: Optional[int] = typer.Option(None, "--skip"),
    out: Optional[typer.FileTextWrite] = typer.Option(None, "--out", "-o"),
):
    """
    Fetch UDI data from openFDA.
    """
    async def main():
        client = OpenFDAClient()
        accessor = UDIAccessor(client)
        results = await accessor.fetch(search=search, limit=limit, skip=skip)
        if out:
            for item in results:
                out.write(item.json() + "\n")
        else:
            for item in results:
                print(item.json())
        await client.close()

    asyncio.run(main())

@device_app.command("recall")
def recall(
    search: Optional[str] = typer.Option(None, "--search", "-s"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    skip: Optional[int] = typer.Option(None, "--skip"),
    out: Optional[typer.FileTextWrite] = typer.Option(None, "--out", "-o"),
):
    """
    Fetch device recall data from openFDA.
    """
    async def main():
        client = OpenFDAClient()
        accessor = RecallAccessor(client)
        results = await accessor.fetch(search=search, limit=limit, skip=skip)
        if out:
            for item in results:
                out.write(item.json() + "\n")
        else:
            for item in results:
                print(item.json())
        await client.close()

    asyncio.run(main())

@device_app.command("enforcement")
def enforcement(
    search: Optional[str] = typer.Option(None, "--search", "-s"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    skip: Optional[int] = typer.Option(None, "--skip"),
    count: Optional[str] = typer.Option(None, "--count"),
    out: Optional[typer.FileTextWrite] = typer.Option(None, "--out", "-o"),
):
    """
    Fetch enforcement report data from openFDA.
    """
    async def main():
        client = OpenFDAClient()
        accessor = EnforcementAccessor(client)
        if count:
            results = await accessor.count(count)
            if out:
                out.write(json.dumps(results, indent=2))
            else:
                print(json.dumps(results, indent=2))
        else:
            results = await accessor.fetch(search=search, limit=limit, skip=skip)
            if out:
                for item in results:
                    out.write(item.json() + "\n")
            else:
                for item in results:
                    print(item.json())
        await client.close()

    asyncio.run(main())

@device_app.command("classification")
def classification(
    search: Optional[str] = typer.Option(None, "--search", "-s"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    skip: Optional[int] = typer.Option(None, "--skip"),
    out: Optional[typer.FileTextWrite] = typer.Option(None, "--out", "-o"),
):
    """
    Fetch device classification data from openFDA.
    """
    async def main():
        client = OpenFDAClient()
        accessor = ClassificationAccessor(client)
        results = await accessor.fetch(search=search, limit=limit, skip=skip)
        if out:
            for item in results:
                out.write(item.json() + "\n")
        else:
            for item in results:
                print(item.json())
        await client.close()

    asyncio.run(main())

@device_app.command("k510")
def k510(
    search: Optional[str] = typer.Option(None, "--search", "-s"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    skip: Optional[int] = typer.Option(None, "--skip"),
    out: Optional[typer.FileTextWrite] = typer.Option(None, "--out", "-o"),
):
    """
    Fetch 510(k) data from openFDA.
    """
    async def main():
        client = OpenFDAClient()
        accessor = K510Accessor(client)
        results = await accessor.fetch(search=search, limit=limit, skip=skip)
        if out:
            for item in results:
                out.write(item.json() + "\n")
        else:
            for item in results:
                print(item.json())
        await client.close()

    asyncio.run(main())

@device_app.command("pma")
def pma(
    search: Optional[str] = typer.Option(None, "--search", "-s"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    skip: Optional[int] = typer.Option(None, "--skip"),
    out: Optional[typer.FileTextWrite] = typer.Option(None, "--out", "-o"),
):
    """
    Fetch PMA data from openFDA.
    """
    async def main():
        client = OpenFDAClient()
        accessor = PMAAccessor(client)
        results = await accessor.fetch(search=search, limit=limit, skip=skip)
        if out:
            for item in results:
                out.write(item.json() + "\n")
        else:
            for item in results:
                print(item.json())
        await client.close()

    asyncio.run(main())

@device_app.command("reglist")
def reglist(
    search: Optional[str] = typer.Option(None, "--search", "-s"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    skip: Optional[int] = typer.Option(None, "--skip"),
    out: Optional[typer.FileTextWrite] = typer.Option(None, "--out", "-o"),
):
    """
    Fetch registration and listing data from openFDA.
    """
    async def main():
        client = OpenFDAClient()
        accessor = RegListAccessor(client)
        results = await accessor.fetch(search=search, limit=limit, skip=skip)
        if out:
            for item in results:
                out.write(item.json() + "\n")
        else:
            for item in results:
                print(item.json())
        await client.close()

    asyncio.run(main())

@device_app.command("event")
def event(
    search: Optional[str] = typer.Option(None, "--search", "-s"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    skip: Optional[int] = typer.Option(None, "--skip"),
    count: Optional[str] = typer.Option(None, "--count"),
    out: Optional[typer.FileTextWrite] = typer.Option(None, "--out", "-o"),
):
    """
    Fetch MAUDE event data from openFDA.
    """
    async def main():
        client = OpenFDAClient()
        accessor = MAUDEAccessor(client)
        if count:
            results = await accessor.count(count)
            if out:
                out.write(json.dumps(results, indent=2))
            else:
                print(json.dumps(results, indent=2))
        else:
            results = await accessor.fetch(search=search, limit=limit, skip=skip)
            if out:
                for item in results:
                    out.write(item.json() + "\n")
            else:
                for item in results:
                    print(item.json())
        await client.close()

    asyncio.run(main())


@ingest_app.command("download")
def download(
    endpoint: str = typer.Argument(..., help="Endpoint to download, e.g., device/udi"),
    output_dir: str = typer.Option("data/openfda", "--out", "-o"),
):
    """
    Download and extract bulk data from openFDA.
    """
    asyncio.run(download_and_extract(endpoint, output_dir))

if __name__ == "__main__":
    app()
