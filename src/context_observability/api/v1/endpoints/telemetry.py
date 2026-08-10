"""Telemetry endpoints."""
import structlog
from fastapi import APIRouter
from pydantic import BaseModel

from context_observability.models.telemetry import LogPayload, MetricPayload, TracePayload
from context_observability.processor.log_scrubber import LogScrubber

router = APIRouter(tags=["Telemetry"])
logger = structlog.get_logger("telemetry")
scrubber = LogScrubber()

class TelemetryResponse(BaseModel):
    success: bool
    message: str

@router.post("/log", response_model=TelemetryResponse, status_code=202)
async def ingest_log(payload: LogPayload) -> TelemetryResponse:
    clean_msg = scrubber.sanitize(payload.message)
    logger.info("ingested_log", service=payload.service_name, msg=clean_msg)
    return TelemetryResponse(success=True, message="Log accepted")

@router.post("/trace", response_model=TelemetryResponse, status_code=202)
async def ingest_trace(payload: TracePayload) -> TelemetryResponse:
    logger.info("ingested_trace", trace_id=payload.trace_id)
    return TelemetryResponse(success=True, message="Trace accepted")

@router.post("/metric", response_model=TelemetryResponse, status_code=202)
async def ingest_metric(payload: MetricPayload) -> TelemetryResponse:
    logger.info("ingested_metric", metric_name=payload.metric_name, value=payload.value)
    return TelemetryResponse(success=True, message="Metric accepted")
