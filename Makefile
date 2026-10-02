.PHONY: up down build test lint migrate logs shell

up:
	docker-compose up -d

down:
	docker-compose down -v

build:
	docker-compose build

test:
	docker-compose run --rm web pytest -q

lint:
	docker-compose run --rm web ruff check app tests
	docker-compose run --rm web mypy app tests

migrate:
	docker-compose run --rm web alembic upgrade head

logs:
	docker-compose logs -f web

shell:
	docker-compose run --rm web /bin/bash
