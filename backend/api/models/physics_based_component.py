from datetime import date

from pydantic import BaseModel

from .component import Component, ComponentFromFile, ComponentSummary
from .computational_resources import ComputationalResources


class VerticalDiscretization(BaseModel, extra="forbid"):
    """Vertical discretization of a physics-based component."""

    soil: str | None = None
    vegetation: str | None = None


class PhysicsBasedComponentFromFile(ComponentFromFile):
    """Physics-based component, without assigned id."""

    type: str | None = None
    fixed_parameters_count: int | None = None
    tunable_parameters_count: int | None = None
    state_varialbles_count: int | None = None
    temporal_coverage: str | date | None = None
    spatial_coverage: str | None = None
    spatial_resolution: str | None = None
    temporal_resolution: str | None = None
    vertical_discretization: VerticalDiscretization | None = None
    lateral_flow: bool | None = None
    related_identifiers: list[str] | None = None
    testing_resources: ComputationalResources | None = None


class PhysicsBasedComponentSummary(ComponentSummary):
    """Essential metadata fields for physics-based components."""


class PhysicsBasedComponent(Component, PhysicsBasedComponentFromFile, PhysicsBasedComponentSummary):
    """Physics-based component."""

    id: int
