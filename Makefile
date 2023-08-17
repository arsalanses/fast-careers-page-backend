COMPOSE_FILE := docker-compose.yml
DOCKER_COMPOSE := docker compose -f $(COMPOSE_FILE)
SERVICE_NAME := careers

PROJECT_NAME := app
VENV_NAME := venv
VENV_ACTIVATE := . $(VENV_NAME)/bin/activate
PYTHON := $(VENV_NAME)/bin/python

.PHONY: up down build start stop restart logs ps run prune

up: build start

down: stop

build:
	$(DOCKER_COMPOSE) build

start:
	$(DOCKER_COMPOSE) up --scale careers=3 -d --force-recreate

stop:
	$(DOCKER_COMPOSE) stop

restart:
	$(DOCKER_COMPOSE) restart

logs:
	$(DOCKER_COMPOSE) logs -n 100 -f $(SERVICE_NAME)

ps:
	$(DOCKER_COMPOSE) ps

run:
	@echo "Starting development server..."
	$(VENV_ACTIVATE) && uvicorn app.main:app --reload

prune:
	@echo "Cleaning up Docker system resources..."
	docker system prune --all --volumes --force
