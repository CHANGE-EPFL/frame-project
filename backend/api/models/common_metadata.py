"""Common metadata fields for hybrid models and components.

Based on Dublin Core Metadata Initiative (DCMI) Metadata Terms.
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
"""

from datetime import date

from pydantic import BaseModel, Extra


class CommonMetadataSummary(BaseModel, extra=Extra.forbid):
    """Essential metadata fields for hybrid models and components."""

    description: str
    created: date
    keywords: list[str]
    name: str


class CommonMetadata(CommonMetadataSummary):
    """Common metadata fields for hybrid models and components."""

    contributors: list[str]
    #: URLs or DOIs
    documentation: list[str] | None = None
    #: DOI
    identifier: str | None = None
    license: str
    #: Repository URL
    url: str
    version: str | int | float | None = None
