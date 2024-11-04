from fastapi import APIRouter

from ..models.model import Model, ModelSummary
from ..services import metadata

router = APIRouter()


@router.get("/")
async def get_models() -> list[ModelSummary]:
    """Get a summarized list of all hybrid models."""
    return await metadata.get_models()


@router.get("/{model_id}")
async def get_model(model_id: int) -> Model:
    """Get a detailed view of a specific hybrid model."""
    return await metadata.get_model(model_id)
