# Security Threat Model

| Threat | Mitigation |
|---|---|
| Unauthorized ingestion | JWT authentication on `/v1/telemetry/` endpoints |
| PII Data Leak in Logs | Automatic regex redaction in `LogScrub` processor |
