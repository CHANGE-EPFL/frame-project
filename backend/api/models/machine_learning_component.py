from pydantic import BaseModel, Extra

from .component import Component, ComponentFromFile, ComponentSummary
from .computational_resources import ComputationalResources


class TrainingRequirements(BaseModel, extra=Extra.forbid):
    """Training requirements for a machine learning component."""

    gpu: bool = False
    cpu: bool = False


class NeuralNetwork(BaseModel, extra=Extra.forbid):
    """Neural network metadata."""

    name: str
    type: str | None = None
    layer_count: int | None = None
    node_count: int | None = None
    batch_size: int | None = None
    learning_rate: float | None = None
    predictor_count: int | None = None
    activation_functions: list[str] | None = None
    input_scaling: str | None = None
    initialization: str | None = None
    loss_function: str | None = None
    regularization: str | None = None
    optimization_method: str | None = None
    host_physics_model: str | None = None
    target_variables: list[str] | None = None
    training_requirements: TrainingRequirements | None = None
    training_resources: ComputationalResources | None = None


class MachineLearningComponentFromFile(ComponentFromFile):
    """Machine learning component, without assigned id."""

    ml_process: str | None = None
    neural_networks: list[NeuralNetwork] | None = None


class MachineLearningComponentSummary(ComponentSummary):
    """Essential metadata fields for machine learning components."""


class MachineLearningComponent(Component, MachineLearningComponentFromFile, MachineLearningComponentSummary):
    """Machine learning component."""

    id: int
