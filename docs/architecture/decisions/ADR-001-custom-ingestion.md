# ADR 001: Custom FastAPI Telemetry Ingestion

## Status: Accepted

## Context
We need to ingest OTLP and custom log formats while enforcing strict JWT security and secondary PII redaction.

## Decision
We will build a custom FastAPI Python microservice to act as the telemetry ingestion proxy instead of exposing a raw OpenTelemetry Collector to the network.

## Consequences
- Better control over authentication and data scrubbing.
- Slight performance overhead compared to raw Go-based OTel collector.
