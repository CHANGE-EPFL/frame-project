from .common_metadata import CommonMetadata, CommonMetadataSummary
from .computational_environment import ComputationalEnvironment
from .data import Data, DataIO


class HybridModelFromFile(CommonMetadata):
    """Hybrid model, without assigned id."""

    ml_process: str | None = None
    host_physics: str | None = None
    latent_variables: list[Data] = []
    computational_environment: list[ComputationalEnvironment] | None = None


class HybridModelSummary(CommonMetadataSummary, extra="ignore"):
    """Contains essential metadata fields for hybrid models."""


class HybridModel(HybridModelFromFile, HybridModelSummary):
    """Hybrid model."""

    compatible_machine_learning_component_ids: list[str]
    compatible_physics_based_component_ids: list[str]
    data: DataIO
