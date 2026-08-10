# ADR 002: Prometheus as Primary Time-Series Engine

## Status: Accepted

## Context
We need a robust, standardized way to aggregate and query system metrics.

## Decision
We will expose `/metrics` endpoint using the official Python `prometheus_client`. All metrics will be scraped by a cluster-level Prometheus instance.

## Consequences
- Wide industry support.
- Native integration with Grafana.
