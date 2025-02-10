from fastapi import APIRouter

from ..models.machine_learning_component import MachineLearningComponent, MachineLearningComponentSummary
from ..models.physics_based_component import PhysicsBasedComponent, PhysicsBasedComponentSummary
from ..services import metadata

router = APIRouter()


@router.get("/model_physics_based/{model_id}")
async def get_model_physics_based_components(model_id: str) -> list[PhysicsBasedComponentSummary]:
    """Get a summarized list of all physics-based components for a given model."""
    return await metadata.get_model_physics_based_components(model_id)


@router.get("/physics_based/{component_id}")
async def get_physics_based_component(component_id: str) -> PhysicsBasedComponent:
    """Get a detailed view of a specific physics-based component."""
    return await metadata.get_physics_based_component(component_id)


@router.get("/model_machine_learning/{model_id}")
async def get_model_machine_learning_components(model_id: str) -> list[MachineLearningComponentSummary]:
    """Get a summarized list of all machine learning components for a given model."""
    return await metadata.get_model_machine_learning_components(model_id)


@router.get("/machine_learning/{component_id}")
async def get_machine_learning_component(component_id: str) -> MachineLearningComponent:
    """Get a detailed view of a specific machine learning component."""
    return await metadata.get_machine_learning_component(component_id)


@router.get("/ids/")
async def get_component_ids() -> list[str]:
    """Get a list of component short names."""
    return await metadata.get_component_ids()
