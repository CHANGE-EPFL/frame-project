from fastapi import APIRouter

from ..models.machine_learning_component import MachineLearningComponent, MachineLearningComponentSummary
from ..models.physics_based_component import PhysicsBasedComponent, PhysicsBasedComponentSummary
from ..services import metadata

router = APIRouter()


@router.get("/model_physics_based/{model_id}")
async def get_model_physics_based_components(
    model_id: str, model_version: str | None = None
) -> list[PhysicsBasedComponentSummary]:
    """Get a summarized list of all physics-based components for a given model.
    If the version is not provided, use the latest model version.
    """
    return await metadata.get_model_physics_based_components(model_id, model_version)


@router.get("/physics_based/{component_id}")
async def get_physics_based_component(component_id: str, component_version: str | None = None) -> PhysicsBasedComponent:
    """Get a detailed view of a specific physics-based component.
    If the version is not provided, return the latest version.
    """
    return await metadata.get_physics_based_component(component_id, component_version)


@router.get("/model_machine_learning/{model_id}")
async def get_model_machine_learning_components(
    model_id: str, model_version: str | None = None
) -> list[MachineLearningComponentSummary]:
    """Get a summarized list of all machine learning components for a given model.
    If the version is not provided, use the latest model version.
    """
    return await metadata.get_model_machine_learning_components(model_id, model_version)


@router.get("/machine_learning/{component_id}")
async def get_machine_learning_component(
    component_id: str, component_version: str | None = None
) -> MachineLearningComponent:
    """Get a detailed view of a specific machine learning component.
    If the version is not provided, return the latest version.
    """
    return await metadata.get_machine_learning_component(component_id, component_version)


@router.get("/ids/")
async def get_component_ids() -> list[str]:
    """Get a list of component short names."""
    return await metadata.get_component_ids()


@router.get("/physics_based_ids/")
async def get_physics_based_component_ids() -> list[str]:
    """Get a list of physics-based component short names."""
    return await metadata.get_physics_based_component_ids()


@router.get("/machine_learning_ids/")
async def get_machine_learning_component_ids() -> list[str]:
    """Get a list of machine learning component short names."""
    return await metadata.get_machine_learning_component_ids()


@router.get("/physics_based_versions/{component_id}")
async def get_physics_based_component_versions(component_id: str) -> list[str]:
    """Get a list of physics-based component versions."""
    return await metadata.get_physics_based_component_versions(component_id)


@router.get("/machine_learning_versions/{component_id}")
async def get_machine_learning_component_versions(component_id: str) -> list[str]:
    """Get a list of machine learning component versions."""
    return await metadata.get_machine_learning_component_versions(component_id)
