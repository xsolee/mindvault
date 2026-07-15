"""Environment-based application configuration."""

from enum import StrEnum
from functools import lru_cache
from typing import Literal, Self

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnvironment(StrEnum):
    """Supported application runtime environments."""

    DEVELOPMENT = "development"
    TEST = "test"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=("../.env", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "MindVault API"
    app_version: str = "0.1.0"
    app_env: AppEnvironment = AppEnvironment.DEVELOPMENT
    app_debug: bool = False
    api_v1_prefix: str = "/api/v1"
    app_host: str = "0.0.0.0"
    app_port: int = Field(default=8000, ge=1, le=65535)
    log_level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"] = "INFO"
    cors_origins: str = "http://localhost:5173"

    @field_validator("api_v1_prefix")
    @classmethod
    def validate_api_prefix(cls, value: str) -> str:
        """Ensure the configured API prefix is an absolute path."""
        normalized = value.rstrip("/")
        if not normalized.startswith("/") or normalized == "":
            msg = "API_V1_PREFIX must be an absolute, non-root path"
            raise ValueError(msg)
        return normalized

    @property
    def cors_origin_list(self) -> list[str]:
        """Return normalized origins from the comma-separated setting."""
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    @model_validator(mode="after")
    def reject_unsafe_production_cors(self) -> Self:
        """Disallow wildcard credential origins in production."""
        if self.app_env is AppEnvironment.PRODUCTION and "*" in self.cors_origin_list:
            msg = "CORS_ORIGINS must not contain '*' in production"
            raise ValueError(msg)
        return self


@lru_cache
def get_settings() -> Settings:
    """Return the process-wide settings instance."""
    return Settings()
