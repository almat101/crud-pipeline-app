all:
	docker compose up --build -d

down:
	docker compose down

fclean:
	docker compose down -v

prune:
	docker system prune -af --volumes

.PHONY: all down fclean prune



