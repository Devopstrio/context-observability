# ADR 003: Structlog for JSON Audit Logging

## Status: Accepted

## Context
We need structured logging to enable efficient parsing and aggregation in Elasticsearch/Loki.

## Decision
We will use `structlog` to enforce JSON-formatted log lines natively within the Python runtime.

## Consequences
- Requires adapting standard library `logging` output.
- Highly performant JSON serialization.
