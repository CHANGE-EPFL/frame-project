env_path=../.env
model_modules=hybrid_model machine_learning_component physics_based_component

install:
	poetry install
	pip install pre-commit
	pre-commit install -t pre-commit -t commit-msg

run:
	poetry run dotenv -f "$(env_path)" run uvicorn api.main:app --reload

test:
	poetry run dotenv -f "$(env_path)" run pytest

lint:
	pre-commit run --all-files

export-ts-models:
	for module in $(model_modules); do \
		pydantic2ts --module api.models.$$module --output ../frontend/src/models/$$module.ts --json2ts-cmd ../frontend/node_modules/.bin/json2ts; \
	done
