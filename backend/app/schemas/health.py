"""Application metadata and health response schemas."""

from typing import Literal

from pydantic import BaseModel, Field

from app.core.config import AppEnvironment


class ApplicationMetadata(BaseModel):
    """Public metadata returned by the API root."""

    name: str
    version: str
    environment: AppEnvironment
    docs_url: str


class LivenessResponse(BaseModel):
    """Liveness probe response."""

    status: Literal["ok"]


class ReadinessResponse(BaseModel):
    """Readiness probe response with future dependency check space."""

    status: Literal["ready"]
    checks: dict[str, str] = Field(default_factory=dict)
