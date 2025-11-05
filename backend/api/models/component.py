from pydantic import BaseModel, Field

from .common_metadata import CommonMetadataIncomplete, CommonMetadataSummary


class ComponentFromFile(CommonMetadataIncomplete):
    """Component of hybrid model."""


class ComponentSummary(CommonMetadataSummary, extra="ignore"):
    """Essential metadata fields for hybrid model components."""


class Component(ComponentFromFile, ComponentSummary):
    """Component of hybrid model."""

    latest: bool = Field(False, description="Whether this version is the latest one. Automatically inferred.")
    readme_content: str | None = None


class ComponentReference(BaseModel, extra="forbid"):
    """Reference to an existing component of a hybrid model."""

    id: str = Field(
        description=(
            "ID of a component defined in another metadata file, that is compatible with the hybrid model defined in"
            " this file. Only the ID is required, the other fields should not be set."
        )
    )
