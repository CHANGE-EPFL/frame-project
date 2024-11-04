from .common_metadata import CommonMetadata, CommonMetadataSummary


class ModelSummary(CommonMetadataSummary):
    """Contains essential metadata fields for hybrid models."""

    id: int


class Model(CommonMetadata, ModelSummary):
    """Hybrid model."""

    compatible_machine_learning_component_ids: list[int]
    compatible_physical_based_component_ids: list[int]
    short_name: str
