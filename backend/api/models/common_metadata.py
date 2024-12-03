"""Common metadata fields for hybrid models and components.

Based on Dublin Core Metadata Initiative (DCMI) Metadata Terms.
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
"""

from datetime import date
from typing import TYPE_CHECKING

from pydantic import BaseModel, Extra, conlist

if TYPE_CHECKING:  # Static type checker may not accept conlist
    NonEmptyList = list[str]
else:
    NonEmptyList = conlist(str, min_length=1)


class CommonMetadataSummary(BaseModel, extra=Extra.forbid):
    """Essential metadata fields for hybrid models."""

    description: str
    created: date | None = None
    keywords: NonEmptyList
    name: str


class CommonMetadataSummaryIncomplete(BaseModel, extra=Extra.forbid):
    """Essential metadata fields for components that allows for missing fields."""

    description: str
    created: date | None = None
    keywords: list[str] = []
    name: str


class CommonMetadata(CommonMetadataSummary):
    """Common metadata fields for hybrid models."""

    contributors: NonEmptyList
    #: URLs or DOIs
    documentation: list[str] | None = None
    #: DOI
    identifier: str | None = None
    license: str | None = None
    #: Repository URL
    url: str | None = None
    version: str | int | float | None = None


class CommonMetadataIncomplete(CommonMetadataSummaryIncomplete):
    """Common metadata fields for components that allows for missing fields."""

    contributors: list[str] = []
    #: URLs or DOIs
    documentation: list[str] | None = None
    #: DOI
    identifier: str | None = None
    license: str | None = None
    #: Repository URL
    url: str | None = None
    version: str | int | float | None = None
