install:
	pip install pre-commit
	pre-commit install -t pre-commit -t commit-msg
	cd backend && make install

lint:
	pre-commit run --all-files

run-backend:
	cd backend && make run

run-frontend:
	cd frontend && npm run dev

test:
	cd backend && make test
