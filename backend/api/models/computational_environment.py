from typing import Literal

from pydantic import BaseModel


class ComputationalEnvironment(BaseModel, extra="forbid"):
    """Description of a computational environment."""

    type: Literal["conda", "python_requirements", "pyproject_toml"]
    file_paths: list[str]
