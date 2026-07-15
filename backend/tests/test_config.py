"""Application settings tests."""

import pytest
from pydantic import ValidationError

from app.core.config import AppEnvironment, Settings


@pytest.fixture(autouse=True)
def clear_application_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep settings tests independent of the developer's environment."""
    for variable in (
        "APP_NAME",
        "APP_VERSION",
        "APP_ENV",
        "APP_DEBUG",
        "API_V1_PREFIX",
        "APP_HOST",
        "APP_PORT",
        "LOG_LEVEL",
        "CORS_ORIGINS",
    ):
        monkeypatch.delenv(variable, raising=False)


def test_settings_defaults() -> None:
    settings = Settings(_env_file=None)

    assert settings.app_env is AppEnvironment.DEVELOPMENT
    assert settings.app_debug is False
    assert settings.api_v1_prefix == "/api/v1"


def test_settings_load_environment_variables(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_NAME", "Configured API")
    monkeypatch.setenv("APP_DEBUG", "true")

    settings = Settings(_env_file=None)

    assert settings.app_name == "Configured API"
    assert settings.app_debug is True


@pytest.mark.parametrize("environment", list(AppEnvironment))
def test_supported_environments(environment: AppEnvironment) -> None:
    settings = Settings(app_env=environment.value, _env_file=None)

    assert settings.app_env is environment


def test_cors_origin_parsing() -> None:
    settings = Settings(
        cors_origins="http://localhost:5173, https://mindvault.example ",
        _env_file=None,
    )

    assert settings.cors_origin_list == [
        "http://localhost:5173",
        "https://mindvault.example",
    ]


def test_production_rejects_wildcard_cors() -> None:
    with pytest.raises(ValidationError):
        Settings(app_env="production", cors_origins="*", _env_file=None)
