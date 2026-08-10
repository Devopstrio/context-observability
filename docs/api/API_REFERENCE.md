# API Reference Guide

## Telemetry Endpoints
- `POST /v1/telemetry/log`: Ingest structured JSON audit logs.
- `POST /v1/telemetry/trace`: Ingest OpenTelemetry formatted trace spans.
- `POST /v1/telemetry/metric`: Ingest custom metrics.

## Export Endpoints
- `GET /metrics`: Standard Prometheus scraping endpoint.
