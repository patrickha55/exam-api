config_script := ./config.sh
docker_env := app/db.env
docker_compose_file := compose.yaml

.PHONY: config build run dev

config:
	@echo "Generating configuration files..."
	${config_script}

build: config
	@echo "Starting the dev server in detached mode..."
	docker compose --env-file ${docker_env} -f ${docker_compose_file} up -d
	@echo "Waiting for the database to be ready, 5 seconds..."
	sleep 5

dev:
	fastapi dev app/main.py

clean:
	docker compose down
	rm app/.env
	rm app/db.env

