from fastapi import APIRouter

from ..models.hybrid_model import HybridModel, HybridModelSummary
from ..services import metadata

router = APIRouter()


@router.get("/")
async def get_hybrid_models() -> list[HybridModelSummary]:
    """Get a summarized list of all hybrid models."""
    return await metadata.get_hybrid_models()


@router.get("/{model_id}")
async def get_hybrid_model(model_id: int) -> HybridModel:
    """Get a detailed view of a specific hybrid model."""
    return await metadata.get_hybrid_model(model_id)


@router.get("/short_names/")
async def get_hybrid_model_short_names() -> list[str]:
    """Get a list of hybrid model short names."""
    return await metadata.get_hybrid_model_short_names()
