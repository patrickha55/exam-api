config_script := ./config.sh

.PHONY: config build run dev

config:
	@echo "Generating configuration files..."
	${config_script}

build:
	docker compose up

dev:
	fastapi dev app/main.py

clean:
	docker compose down
	rm app/.env
	rm app/db.env

