env_path=../.env
model_modules=hybrid_model machine_learning_component physics_based_component

install:
	uv venv
	uv pip install -e .[dev]

run:
	uv run dotenv -f "$(env_path)" run uvicorn api.main:app --reload

test:
	uv run dotenv -f "$(env_path)" run pytest

lint:
	uv run pre-commit run --all-files

export-ts-models:
	for module in $(model_modules); do \
		pydantic2ts --module api.models.$$module --output ../frontend/src/models/$$module.ts --json2ts-cmd ../frontend/node_modules/.bin/json2ts; \
	done

export-json-schema:
	uv run python -c 'from api.models.metadata_file import export_json_schema; export_json_schema("api/metadata_files/schema.json")'

export-yaml-template:
	uv run python -c 'from api.models.metadata_file import export_yaml_template; export_yaml_template("api/metadata_files/template.yaml")'
