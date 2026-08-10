"""API Tests."""
from fastapi.testclient import TestClient

from context_observability.main import app

client = TestClient(app)

def test_ingest_log() -> None:
    response = client.post("/v1/telemetry/log", json={
        "service_name": "test-service",
        "level": "INFO",
        "message": "User 123-45-6789 logged in",
        "correlation_id": "uuid-123"
    })
    assert response.status_code == 202
    assert response.json()["success"] is True

def test_metrics_endpoint() -> None:
    response = client.get("/metrics")
    assert response.status_code == 200
