from .common_metadata import CommonMetadata, CommonMetadataSummary


class ComponentSummary(CommonMetadataSummary):
    """Essential metadata fields for hybrid model components."""

    id: int


class Component(CommonMetadata, ComponentSummary):
    """Component of hybrid model."""

    short_name: str
