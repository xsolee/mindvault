"""Application exceptions and their HTTP handlers."""

import logging
from typing import cast

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler

from app.schemas.error import ErrorDetail, ErrorResponse

logger = logging.getLogger(__name__)


class MindVaultException(Exception):
    """Base exception for errors safe to expose through the public API."""

    def __init__(self, *, code: str, message: str, status_code: int) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code


async def mindvault_exception_handler(_request: Request, exc: MindVaultException) -> JSONResponse:
    """Render a known application exception using the standard error shape."""
    response = ErrorResponse(error=ErrorDetail(code=exc.code, message=exc.message))
    return JSONResponse(status_code=exc.status_code, content=response.model_dump())


async def unexpected_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Log an unexpected error and return a safe public response."""
    logger.exception("Unexpected error while handling %s %s", request.method, request.url.path)
    response = ErrorResponse(
        error=ErrorDetail(
            code="internal_server_error",
            message="An unexpected error occurred.",
        )
    )
    return JSONResponse(status_code=500, content=response.model_dump())


def register_exception_handlers(application: FastAPI) -> None:
    """Register application-level exception handlers."""
    application.add_exception_handler(
        MindVaultException,
        cast(ExceptionHandler, mindvault_exception_handler),
    )
    application.add_exception_handler(Exception, unexpected_exception_handler)
