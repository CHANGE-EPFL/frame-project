run-db:
	docker compose up -d --pull=always db

install:
	pip install pre-commit
	pre-commit install -t pre-commit -t commit-msg

lint:
	pre-commit run --all-files
