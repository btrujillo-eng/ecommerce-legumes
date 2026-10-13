from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    stripe_api_key: SecretStr = Field(default=...)
    resend_api_key: SecretStr = Field(default=...)
    db_url: SecretStr = Field(default=...)
    debug: bool = Field(default=False)
    migrator_db_url: SecretStr = Field(default=...)
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    
@lru_cache
def get_settings()-> Settings:
    return Settings()
