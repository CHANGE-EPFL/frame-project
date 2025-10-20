from pydantic import BaseModel, Field


type_description = "{} computational environment that can be automatically setup after downloading the model."
file_paths_description = (
    "List of file paths that contain the {} environment description, relative to the repository root. E.g., {}."
)


class ComputationalEnvironment(BaseModel, extra="forbid"):
    """Description of a computational environment."""

    type: str = Field(description=type_description.format("Type of"))
    file_paths: list[str] = Field(
        description=file_paths_description.format("target", "for 'conda', it could be ['environment.yml']")
    )


class CondaComputationalEnvironment(ComputationalEnvironment):
    """Conda computational environment."""

    type: str = Field(pattern="^conda$", description=type_description.format("Conda"))
    file_paths: list[str] = Field(description=file_paths_description.format("conda", "'environment.yml'"))


class PythonComputationalEnvironment(ComputationalEnvironment):
    """Python computational environment."""

    type: str = Field(pattern="^python$", description=type_description.format("Python"))
    file_paths: list[str] = Field(
        description=file_paths_description.format("python", "'requirements.txt', 'pyproject.toml'")
    )


class JuliaComputationalEnvironment(ComputationalEnvironment):
    """Julia computational environment."""

    type: str = Field(pattern="^julia$", description=type_description.format("Julia"))
    file_paths: list[str] = Field(description=file_paths_description.format("julia", "'Project.toml', 'Manifest.toml'"))
