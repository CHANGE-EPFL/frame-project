from typing import Literal

from pydantic import BaseModel, Field


class ComputationalEnvironment(BaseModel, extra="forbid"):
    """Description of a computational environment."""

    type: Literal["conda", "python_requirements", "pyproject_toml"] = Field(
        description=(
            "Type of the computational environment that could be automatically setup after downloading the model."
        )
    )
    file_paths: list[str] = Field(
        description="List of file paths that contain the environment description, relative to the repository root."
    )
