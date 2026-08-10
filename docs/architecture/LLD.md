# Low-Level Design (LLD)

## 1. Components
### `TelemetryRouter` (FastAPI)
- Routes incoming POST requests to `/v1/logs`, `/v1/traces`, and `/v1/metrics`.

### `LogProcessor`
- Cleans and structures raw JSON logs using Structlog.
- Filters out any leaked PII using secondary regex scanners.

### `TraceProcessor`
- Receives OTLP span data.
- Constructs distributed span graphs using parent-child IDs.

### `AlertEngine`
- Runs asynchronous periodic tasks.
- Evaluates Prometheus gauge and counter metrics.
- Emits webhooks if thresholds are breached (e.g., error rate > 5%).

## 2. Internal Schemas

### LogEvent Schema
```json
{
  "timestamp": "ISO8601",
  "correlation_id": "uuid",
  "service": "string",
  "level": "INFO|WARN|ERROR",
  "message": "string",
  "metadata": {}
}
```

### AlertRule Schema
```json
{
  "rule_id": "string",
  "metric_name": "string",
  "operator": "GREATER_THAN",
  "threshold": "float",
  "duration_seconds": "int"
}
```
