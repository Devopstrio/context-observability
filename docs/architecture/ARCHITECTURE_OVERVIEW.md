# Architecture Overview

Context Observability is designed as a standalone FastAPI edge service rather than a pure OpenTelemetry Collector instance. This allows us to embed custom Python-based ML alerting models, strict JWT authentication on the ingestion endpoints, and proprietary enterprise data scrubbing routines before telemetry hits the storage layer.
