"""Application metadata and health endpoint tests."""

from fastapi.testclient import TestClient

from app.core.config import Settings
from app.main import create_application


def test_application_creation(test_settings: Settings) -> None:
    application = create_application(test_settings)

    assert application.title == "MindVault API"
    assert application.version == "0.1.0"
    registered_paths = set(application.openapi()["paths"])
    assert "/" in registered_paths
    assert "/api/v1/health/live" in registered_paths
    assert "/api/v1/health/ready" in registered_paths
    documentation_paths = {
        path for route in application.routes if (path := getattr(route, "path", None)) is not None
    }
    assert "/docs" in documentation_paths
    assert "/redoc" in documentation_paths
    assert "/openapi.json" in documentation_paths


def test_root_returns_public_metadata(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "name": "MindVault API",
        "version": "0.1.0",
        "environment": "test",
        "docs_url": "/docs",
    }
    assert "secret" not in response.text.lower()
    assert "password" not in response.text.lower()


def test_liveness(client: TestClient) -> None:
    response = client.get("/api/v1/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness(client: TestClient) -> None:
    response = client.get("/api/v1/health/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready", "checks": {}}
