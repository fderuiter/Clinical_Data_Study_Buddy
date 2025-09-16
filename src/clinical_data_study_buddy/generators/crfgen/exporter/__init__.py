"""
This package contains modules for exporting CRF (Case Report Form) data into
various output formats. It uses a registry pattern to allow for easy extension
with new exporters.
"""

from .registry import formats, get, register

__all__ = ["register", "get", "formats"]
