"""API v1 Router."""
from fastapi import APIRouter

from context_observability.api.v1.endpoints import telemetry

api_v1_router = APIRouter(prefix="/v1/telemetry")
api_v1_router.include_router(telemetry.router)
