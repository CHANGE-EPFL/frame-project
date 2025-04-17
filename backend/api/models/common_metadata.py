"""Common metadata fields for hybrid models and components.

Based on Dublin Core Metadata Initiative (DCMI) Metadata Terms.
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
"""

from datetime import date
from typing import TYPE_CHECKING

from pydantic import BaseModel, conlist

if TYPE_CHECKING:  # Static type checker may not accept conlist
    NonEmptyList = list[str]
else:
    NonEmptyList = conlist(str, min_length=1)


class CommonMetadataSummary(BaseModel, extra="forbid"):
    """Essential metadata fields for hybrid models."""

    description: str
    created: date | None = None
    id: str
    keywords: NonEmptyList
    name: str


class CommonMetadataSummaryIncomplete(BaseModel, extra="forbid"):
    """Essential metadata fields for components that allows for missing fields."""

    description: str
    created: date | None = None
    id: str
    keywords: list[str] = []
    name: str


class CommonMetadata(CommonMetadataSummary):
    """Common metadata fields for hybrid models."""

    #: List of contributor names
    contributors: NonEmptyList
    #: URLs or DOIs
    documentation: list[str] | None = None
    #: DOI
    identifier: str | None = None
    license: str | None = None
    #: Markdown readme URL
    readme: str | None = None
    #: Repository URL
    url: str | None = None
    #: Semantic version
    version: str | None = None
    #: Whether version is latest
    latest: bool = False


class CommonMetadataIncomplete(CommonMetadataSummaryIncomplete):
    """Common metadata fields for components that allows for missing fields."""

    #: List of contributor names
    contributors: list[str] = []
    #: URLs or DOIs
    documentation: list[str] | None = None
    #: DOI
    identifier: str | None = None
    license: str | None = None
    #: Markdown readme URL
    readme: str | None = None
    #: Repository URL
    url: str | None = None
    #: Semantic version
    version: str | None = None
    #: Whether version is latest
    latest: bool = False
