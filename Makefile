install:
	pip install pre-commit
	pre-commit install -t pre-commit -t commit-msg

lint:
	pre-commit run --all-files
