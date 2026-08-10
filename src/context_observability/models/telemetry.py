"""Telemetry models."""
from typing import Any

from pydantic import BaseModel, Field


class LogPayload(BaseModel):
    service_name: str
    level: str
    message: str
    correlation_id: str
    metadata: dict[str, Any] = Field(default_factory=dict)

class TracePayload(BaseModel):
    trace_id: str
    span_id: str
    parent_span_id: str | None = None
    operation_name: str

class MetricPayload(BaseModel):
    metric_name: str
    value: float
    labels: dict[str, str] = Field(default_factory=dict)
