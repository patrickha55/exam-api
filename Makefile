.PHONY: run dev

build:
	docker compose up

dev:
	fastapi dev app/main.py

clean:
	docker compose down
