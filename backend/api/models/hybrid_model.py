from typing import Union

from . import computational_environment
from .common_metadata import CommonMetadata, CommonMetadataSummary
from .computational_environment import ComputationalEnvironment
from .data import Data, DataIO

computational_environment_types = [
    c
    for c in computational_environment.__dict__.values()
    if isinstance(c, type) and issubclass(c, ComputationalEnvironment) and c is not ComputationalEnvironment
] + [ComputationalEnvironment]


class HybridModelFromFile(CommonMetadata):
    """Hybrid model."""

    ml_process: str | None = None
    host_physics: str | None = None
    latent_variables: list[Data] = []
    computational_environment: list[Union[tuple(computational_environment_types)]] | None = None


class HybridModelSummary(CommonMetadataSummary, extra="ignore"):
    """Contains essential metadata fields for hybrid models."""


class HybridModel(HybridModelFromFile, HybridModelSummary):
    """Hybrid model."""

    compatible_machine_learning_component_ids: list[str]
    compatible_physics_based_component_ids: list[str]
    data: DataIO
    fair_level: int = 0
    #: Whether version is latest
    latest: bool = False
    readme_content: str | None = None
