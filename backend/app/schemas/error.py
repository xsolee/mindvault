"""Standard API error response schemas."""

from pydantic import BaseModel


class ErrorDetail(BaseModel):
    """Machine-readable code and public error message."""

    code: str
    message: str


class ErrorResponse(BaseModel):
    """Standard envelope for API errors."""

    error: ErrorDetail
