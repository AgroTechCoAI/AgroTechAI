# Help documentation à la https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@echo "AgroTech AI - Available commands:"
	@echo ""
	@cat Makefile | grep -v '\.PHONY' |  grep -v '\help:' | grep -B1 -E '^[a-zA-Z0-9_.-]+:.*' | sed -e "s/:.*//" | sed -e "s/^## //" |  grep -v '\-\-' | sed '1!G;h;$$!d' | awk 'NR%2{printf "\033[36m%-30s\033[0m",$$0;next;}1' | sort

# Install production dependencies
py-install:
	cd server && pip install -e .

# Install development dependencies
py-install-dev:
	cd server && pip install -e ".[dev,test]"

# Install javascript dependencies
js-install:
	cd client && npm install

# Run all Python tests (unit + integration)
py-test:
	cd server && python tests/test_runner.py all

# Run all Python unit tests
py-test-unit:
	cd server && python tests/test_runner.py unit

# Run all Python integration's tests
py-test-integration:
	cd server && python tests/test_runner.py integration

# Run Python tests with coverage report
py-test-coverage:
	cd server && python tests/test_runner.py coverage

# Run all Python integration's tests with ollama feature
py-test-ollama:
	cd server && python tests/test_runner.py ollama

# Run smoke tests (critical path validation)
py-test-smoke:
	cd server && python tests/test_runner.py smoke

# Run acceptance tests (end-to-end)
py-test-acceptance:
	cd server && python tests/test_runner.py acceptance

# Run all JavaScript tests (unit + integration)
js-test:
	cd client && npm test -- --run

# Run JavaScript unit tests only
js-test-unit:
	cd client && npm test tests/unit -- --run

# Run JavaScript integration tests only
js-test-integration:
	cd client && npm test tests/integration -- --run

# Run JavaScript tests with coverage report
js-test-coverage:
	cd client && npm run test:coverage

# Run JavaScript tests in watch mode
js-test-watch:
	cd client && npm run test:watch

# Run pylint checks
py-lint:
	cd server && pylint agrotech_ai/ --output-format=text --fail-under=9 > coverage/pylint-report.txt || true

# Run all python linters
py-lint-all: py-lint
	cd server && python tests/test_runner.py lint

# Format Python code with black and isort
py-format:
	cd server && python tests/test_runner.py format

# Run JavaScript linting checks
js-lint:
	cd client && npm run lint

# Run JavaScript linting with auto-fix
js-lint-fix:
	cd client && npm run lint:fix

# Start Python development server
py-run:
	cd server && uvicorn agrotech_ai.app:app --host 0.0.0.0 --port 8000 --reload

# Start JavaScript development server
js-run:
	cd client && npm run dev

# Start services with Docker Compose (ollama, api, frontend)
docker-run:
	docker compose up --build

# Start services with Docker Compose in detached mode (ollama, api, frontend)
docker-detached-run:
	docker compose up --build -d

# Stop Docker Compose services
docker-stop:
	docker compose down

# View Docker Compose logs
logs:
	docker compose logs -f

# View Docker Compose logs for api-server
logs-server:
	docker compose logs -f api-server

# View Docker Compose logs for ollama
logs-ollama:
	docker compose logs -f ollama

# Rebuild all docker services
docker-rebuild:
	docker compose down
	docker compose build --no-cache
	docker compose up

# Delete all docker services
docker-clean:
	docker compose down -v

# Cleanup in the server project
clean-python:
	# Python cleanup
	find server -type f -name ".coverage" -delete
	find server -type d -name "*.egg-info" -exec rm -rf {} +
	find server -type d -name ".pytest_cache" -exec rm -rf {} +
	find server -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf server/htmlcov/
	rm -rf server/coverage.xml
	rm -rf server/report.html
	rm -rf server/coverage
	rm -rf server/dist/
	rm -rf server/build/

# Cleanup in the client project
clean-js:
	# JavaScript cleanup
	rm -rf client/dist/
	rm -rf client/coverage/
	rm -rf client/node_modules/.cache/

# Cleanup in the project
clean: clean-python clean-js
