from .component import Component, ComponentFromFile, ComponentSummary


class MachineLearningComponentFromFile(ComponentFromFile):
    """Machine learning component, without assigned id."""


class MachineLearningComponentSummary(ComponentSummary):
    """Essential metadata fields for machine learning components."""


class MachineLearningComponent(Component, MachineLearningComponentFromFile, MachineLearningComponentSummary):
    """Machine learning component."""

    id: int
