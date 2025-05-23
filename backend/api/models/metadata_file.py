import datetime
import inspect
import json
import types
import typing

from pydantic import BaseModel

from .data import DataIO
from .hybrid_model import HybridModelFromFile
from .machine_learning_component import MachineLearningComponentFromFile, MachineLearningComponentReference
from .physics_based_component import PhysicsBasedComponentFromFile, PhysicsBasedComponentReference


class MetadataFromFile(BaseModel, extra="forbid"):
    """Metadata fields for a metadata file."""

    hybrid_model: HybridModelFromFile
    physics_based_components: list[PhysicsBasedComponentReference | PhysicsBasedComponentFromFile] = []
    machine_learning_components: list[MachineLearningComponentReference | MachineLearningComponentFromFile] = []
    data: DataIO = DataIO()


def export_json_schema(output_path: str) -> None:
    """Export JSON schema for MetadataFromFile."""
    json_schema = MetadataFromFile.model_json_schema()

    with open(output_path, "w") as file:
        json.dump(json_schema, file, indent=4)


def export_yaml_template(output_path: str) -> None:
    """Export YAML template for MetadataFromFile."""

    template = (
        "# yaml-language-server: $schema=https://raw.githubusercontent.com/CHANGE-EPFL/frame-project/"
        "refs/heads/dev/backend/api/metadata_files/schema.json"
    )
    template += get_annotation_template(MetadataFromFile)

    with open(output_path, "w") as file:
        file.write(template)


def get_annotation_template(model, current_level: int = 0, optional: bool = False) -> str:
    template = ""
    indent = "  " * current_level

    if isinstance(model, types.UnionType):
        models = list(typing.get_args(model))
        if type(None) in models:
            models.remove(type(None))

        if len(models) == 1:
            model = models[0]
            optional = True
            # no return, follow through to the next type

        else:
            if set(models) == {float, int}:
                template += " 0"
            template += f" # {' | '.join([m.__name__ for m in models])}"
            if optional:
                template += ", optional"
            return template

    if model is str:
        template += ' "" # str'
        if optional:
            template += ", optional"
        return template

    if model is bool:
        template += " false # bool"
        if optional:
            template += ", optional"
        return template

    if model is int:
        template += " 0 # int"
        if optional:
            template += ", optional"
        return template

    if model is float:
        template += " 0.0 # float"
        if optional:
            template += ", optional"
        return template

    if model is datetime.date:
        template += " 2000-01-01 # date"
        if optional:
            template += ", optional"
        return template

    if isinstance(model, types.GenericAlias) or isinstance(model, typing._GenericAlias):
        if typing.get_origin(model) is list:
            model = typing.get_args(model)[0]

            # If this is a list of union types, show each type as an item
            if isinstance(model, types.UnionType):
                models = list(typing.get_args(model))
                if type(None) in models:
                    models.remove(type(None))
            else:
                models = [model]

            template += " # list"
            if len(models) > 1:
                template += " (multiple possible types)"
            if optional:
                template += ", optional"

            for model in models:
                template += f"\n{indent}- "
                template += get_annotation_template(model, current_level + 1).lstrip()

            return template

        if typing.get_origin(model) is typing.Literal:
            values = typing.get_args(model)
            template += f" {values[0]} # " + " | ".join([f'"{str(v)}"' for v in values])
            if optional:
                template += ", optional"
            return template

    elif inspect.isclass(model) and issubclass(model, BaseModel):
        if optional:
            template += " # optional"

        for name, field in model.model_fields.items():
            if current_level == 0:
                template += "\n"

            template += f"\n{indent}{name}:"
            template += get_annotation_template(field.annotation, current_level + 1, optional=not field.is_required())

        return template

    template += f" # {model.__name__}"
    if optional:
        template += ", optional"
    print(f"WARNING: Unsupported type: {model}")
    return template
    # raise TypeError(f"Unsupported type: {model}")
