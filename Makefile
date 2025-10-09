install:
	pip install pre-commit
	pre-commit install
	cd backend && make install

lint:
	pre-commit run --all-files

run-backend:
	cd backend && make run

run-frontend:
	cd frontend && npm run dev

test:
	cd backend && make test
