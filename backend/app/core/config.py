# /backend/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache
import os

# Get the environment (default to "dev" if not set)
env = os.getenv("APP_ENV", "dev")
env_file_path = f".env.{env}"  # expects .env.dev, .env.test, .env.prod
print("ENV path:", env_file_path)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file_path)

    app_env: str = Field(default="dev", alias="APP_ENV")
    mongo_uri: str = Field(alias="MONGO_URI")
    janusgraph_url: str = Field(alias="JANUSGRAPH_URL")
    secret_key: str = Field(alias="SECRET_KEY")

@lru_cache()
def get_settings() -> Settings:
    return Settings()
