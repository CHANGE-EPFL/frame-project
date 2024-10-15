env_path=../.env

install:
	poetry install

run:
	poetry run dotenv -f "$(env_path)" run uvicorn api.main:app --reload

lint:
	poetry run pre-commit run --all-files
