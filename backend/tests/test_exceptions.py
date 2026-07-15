"""Application exception handler tests."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.core.config import Settings
from app.core.exceptions import MindVaultException
from app.main import create_application


def test_known_exception_uses_standard_error_shape(test_settings: Settings) -> None:
    application = create_application(test_settings)

    @application.get("/test-known-error")
    async def known_error() -> None:
        raise MindVaultException(
            code="test_error",
            message="A safe test error.",
            status_code=409,
        )

    with TestClient(application) as client:
        response = client.get("/test-known-error")

    assert response.status_code == 409
    assert response.json() == {"error": {"code": "test_error", "message": "A safe test error."}}


def test_unexpected_exception_returns_safe_response(test_settings: Settings) -> None:
    application: FastAPI = create_application(test_settings)

    @application.get("/test-unexpected-error")
    async def unexpected_error() -> None:
        raise RuntimeError("private implementation detail")

    with TestClient(application, raise_server_exceptions=False) as client:
        response = client.get("/test-unexpected-error")

    assert response.status_code == 500
    assert response.json() == {
        "error": {
            "code": "internal_server_error",
            "message": "An unexpected error occurred.",
        }
    }
    assert "private implementation detail" not in response.text
