from .component import Component, ComponentFromFile, ComponentSummary


class PhysicsBasedComponentFromFile(ComponentFromFile):
    """Physics-based component, without assigned id."""


class PhysicsBasedComponentSummary(ComponentSummary):
    """Essential metadata fields for physics-based components."""


class PhysicsBasedComponent(Component, PhysicsBasedComponentFromFile, PhysicsBasedComponentSummary):
    """Physics-based component."""

    id: int
