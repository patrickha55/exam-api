from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Exam API"
    postgres_url: str
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=(".env", ".env.prod"))
