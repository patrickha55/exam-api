from functools import lru_cache
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), "..", ".env")


class Settings(BaseSettings):
    app_name: str = "Exam API"
    postgres_url: str = ""
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=DOTENV
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


if __name__ == "__main__":
    config = get_settings()
    print("Configuration Loaded:")
    print(f"{config.app_name}")
    print(f"{config.postgres_url}")
    print(f"{config.log_level}")
    print("Configuration Loaded Successfully.")
