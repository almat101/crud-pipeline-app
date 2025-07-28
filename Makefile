.PHONY: help start-dev start-prod start-both stop-dev stop-prod stop-both build-dev build-prod logs-dev logs-prod prune certs

# Export UID/GID for Docker to use (avoids permission issues)
export UID := $(shell id -u)
export GID := $(shell id -g)

all:
	docker compose up --build -d




