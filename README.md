<div align="center">
  <img src="https://raw.githubusercontent.com/Devopstrio/.github/main/assets/Browser_logo.png" alt="Devopstrio Logo" width="300">
</div>

# Context Observability 📊

**Central telemetry and monitoring backbone for the Enterprise Context Engineering platform.**

[![CI](https://github.com/Devopstrio/context-observability/actions/workflows/ci.yml/badge.svg)](https://github.com/Devopstrio/context-observability/actions/workflows/ci.yml)
[![Lint](https://github.com/Devopstrio/context-observability/actions/workflows/lint.yml/badge.svg)](https://github.com/Devopstrio/context-observability/actions/workflows/lint.yml)
[![Security Scan](https://github.com/Devopstrio/context-observability/actions/workflows/security-scan.yml/badge.svg)](https://github.com/Devopstrio/context-observability/actions/workflows/security-scan.yml)

## 📌 Overview

The **Context Observability** service is the centralized intelligence hub that ingests, aggregates, and visualizes telemetry data (logs, metrics, and traces) from all microservices within the Devopstrio Enterprise Context Engineering platform.

It is designed for scale and high cardinality, natively integrating with OpenTelemetry (OTLP) and Prometheus.

## ✨ Features

- 📈 **Metrics Aggregation**: Scrapes and aggregates PromQL-compatible metrics across the entire platform.
- 🔍 **Distributed Tracing**: OTLP endpoint ingestion and correlation ID processing for end-to-end request tracing.
- 📋 **Structured Audit Logging**: Centralized Structlog ingestion with automatic PII redaction rules.
- 🚨 **Alerting Engine**: Configurable thresholds and anomaly detection for system health and security events.

## 🚀 Quick Start

Ensure you have Python 3.12+ and Docker installed.

```bash
# Clone the repository
git clone https://github.com/Devopstrio/context-observability.git
cd context-observability

# Set up the environment
make install-dev
cp .env.example .env

# Start the observability stack (Prometheus, Grafana, API)
make docker-up
```

## 📚 Documentation

For full architectural blueprints, API specifications, and operational manuals, please explore the [Documentation Directory](./docs/README.md).

- [Architecture High-Level Design](./docs/architecture/HLD.md)
- [API Reference Guide](./docs/api/API_REFERENCE.md)
- [Prometheus Monitoring Guide](./docs/guides/MONITORING.md)
- [Security Threat Model](./docs/security/THREAT_MODEL.md)

---
<div align="center">
  <p>© 2026 Devopstrio — Engineering the Autonomous Enterprise.</p>
</div>
