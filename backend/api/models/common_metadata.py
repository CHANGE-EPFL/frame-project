"""Common metadata fields for hybrid models and components.

Based on Dublin Core Metadata Initiative (DCMI) Metadata Terms.
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
"""

from datetime import date

from pydantic import BaseModel


class CommonMetadataSummary(BaseModel):
    """Essential metadata fields for hybrid models and components."""

    description: str
    created: date
    keywords: list[str]
    name: str


class CommonMetadata(CommonMetadataSummary):
    """Common metadata fields for hybrid models and components."""

    contributors: list[str]
    documentation_url: str | None = None
    doi: str | None = None
    license: str
    repository_url: str
    version: str | None = None
