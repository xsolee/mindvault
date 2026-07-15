"""Process health endpoints."""

from fastapi import APIRouter

from app.schemas.health import LivenessResponse, ReadinessResponse

router = APIRouter()


@router.get("/live", response_model=LivenessResponse)
async def liveness() -> LivenessResponse:
    """Report that the API process is running."""
    return LivenessResponse(status="ok")


@router.get("/ready", response_model=ReadinessResponse)
async def readiness() -> ReadinessResponse:
    """Report readiness for the dependency-free application foundation."""
    return ReadinessResponse(status="ready")
