"""Shared backend test fixtures."""

from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app.core.config import AppEnvironment, Settings
from app.main import create_application


@pytest.fixture
def test_settings() -> Settings:
    """Return settings isolated from local environment files."""
    return Settings(
        app_name="MindVault API",
        app_version="0.1.0",
        app_env=AppEnvironment.TEST,
        app_debug=False,
        api_v1_prefix="/api/v1",
        app_host="0.0.0.0",
        app_port=8000,
        log_level="INFO",
        cors_origins="http://localhost:5173",
        _env_file=None,
    )


@pytest.fixture
def client(test_settings: Settings) -> Iterator[TestClient]:
    """Return a client for a freshly-created application."""
    with TestClient(create_application(test_settings)) as test_client:
        yield test_client
