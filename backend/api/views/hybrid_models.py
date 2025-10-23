import io

from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse

from ..models.hybrid_model import HybridModel, HybridModelSummary
from ..services import metadata

router = APIRouter()


@router.get("/")
async def get_hybrid_models(query: str | None = Query(None)) -> list[HybridModelSummary]:
    """Get a summarized list of all hybrid models, optionally filtered by a query."""
    if query:
        return metadata.get_filtered_hybrid_models(query)

    return metadata.get_hybrid_models()


@router.get("/{model_id}")
async def get_hybrid_model(model_id: str, model_version: str | None = None) -> HybridModel:
    """Get a detailed view of a specific hybrid model.
    If the version is not provided, return the latest version.
    """
    return metadata.get_hybrid_model(model_id, model_version)


@router.get("/metadata_file/{model_id}")
async def get_hybrid_model_metadata_file(model_id: str, model_version: str | None = None) -> StreamingResponse:
    """Get the metadata file content of a specific hybrid model.
    If the version is not provided, return the latest version.
    """

    filename, content = metadata.get_hybrid_model_raw_metadata(model_id, model_version)

    return StreamingResponse(
        io.BytesIO(content.encode("utf-8")),
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.get("/ids/")
async def get_hybrid_model_ids() -> list[str]:
    """Get a list of hybrid model short names."""
    return metadata.get_hybrid_model_ids()


@router.get("/versions/{model_id}")
async def get_hybrid_model_versions(model_id: str) -> list[str]:
    """Get a list of hybrid model versions."""
    return metadata.get_hybrid_model_versions(model_id)


@router.get("/physics_based/{component_id}")
async def get_physics_based_component_models(
    component_id: str, component_version: str | None = None
) -> list[HybridModelSummary]:
    """Get a summarized list of all hybrid models for a given physics based component.
    If the version is not provided, use the latest component version.
    """
    return metadata.get_physics_based_component_models(component_id, component_version)


@router.get("/machine_learning/{component_id}")
async def get_machine_learning_component_models(
    component_id: str, component_version: str | None = None
) -> list[HybridModelSummary]:
    """Get a summarized list of all hybrid models for a given machine learning component.
    If the version is not provided, use the latest component version.
    """
    return metadata.get_machine_learning_component_models(component_id, component_version)
