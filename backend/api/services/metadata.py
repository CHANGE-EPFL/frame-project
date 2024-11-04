"""This module contains functions to retrieve metadata about models.

Mock data for testing.
"""

from datetime import date

from fastapi import HTTPException

from ..models.model import Model, ModelSummary

models = [
    Model(
        id=0,
        contributors=["Smith, John"],
        created=date(2024, 1, 1),
        description="A simple model.",
        keywords=["simple", "example"],
        license="GPL-3.0",
        name="Model 1",
        repository_url="https://github.com/example/model1",
        short_name="model1",
        compatible_machine_learning_component_ids=[0, 1],
        compatible_physical_based_component_ids=[0],
    ),
    Model(
        id=1,
        contributors=[],
        created=date(2024, 2, 1),
        description="",
        keywords=[],
        license="",
        name="Model 2",
        repository_url="",
        short_name="model2",
        compatible_machine_learning_component_ids=[],
        compatible_physical_based_component_ids=[],
    ),
    Model(
        id=2,
        contributors=[],
        created=date(2024, 3, 1),
        description="",
        keywords=[],
        license="",
        name="Model 3",
        repository_url="",
        short_name="model3",
        compatible_machine_learning_component_ids=[],
        compatible_physical_based_component_ids=[],
    ),
]


model_summaries = [
    ModelSummary(
        id=model.id,
        created=model.created,
        description=model.description,
        keywords=model.keywords,
        name=model.name,
    )
    for model in models
]


async def get_models() -> list[ModelSummary]:
    return model_summaries


async def get_model(model_id: int) -> Model:
    try:
        return models[model_id]

    except IndexError:
        raise HTTPException(status_code=404, detail="Model not found.")
