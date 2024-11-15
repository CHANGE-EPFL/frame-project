env_path=../.env

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
