from fastapi import APIRouter, Query

from ..models.hybrid_model import HybridModel, HybridModelSummary
from ..services import metadata

router = APIRouter()


@router.get("/")
async def get_hybrid_models(query: str | None = Query(None)) -> list[HybridModelSummary]:
    """Get a summarized list of all hybrid models, optionally filtered by a query."""
    if query:
        return await metadata.get_filtered_hybrid_models(query)

    return await metadata.get_hybrid_models()


@router.get("/{model_id}")
async def get_hybrid_model(model_id: str) -> HybridModel:
    """Get a detailed view of a specific hybrid model."""
    return await metadata.get_hybrid_model(model_id)


@router.get("/ids/")
async def get_hybrid_model_ids() -> list[str]:
    """Get a list of hybrid model short names."""
    return await metadata.get_hybrid_model_ids()


@router.get("/physics_based/{component_id}")
async def get_physics_based_component_models(component_id: str) -> list[HybridModelSummary]:
    """Get a summarized list of all hybrid models for a given physics based component."""
    return await metadata.get_physics_based_component_models(component_id)


@router.get("/machine_learning/{component_id}")
async def get_machine_learning_component_models(component_id: str) -> list[HybridModelSummary]:
    """Get a summarized list of all hybrid models for a given machine learning component."""
    return await metadata.get_machine_learning_component_models(component_id)
