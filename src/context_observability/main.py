"""Main entrypoint for context-observability."""
import structlog
import uvicorn
from fastapi import FastAPI
from prometheus_client import make_asgi_app

from context_observability.api.v1.router import api_v1_router
from context_observability.config.settings import get_settings

settings = get_settings()
logger = structlog.get_logger("context_observability.main")

app = FastAPI(title="Context Observability")

app.include_router(api_v1_router)

# Mount prometheus metrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

if __name__ == "__main__":
    logger.info("starting_observability_service", host=settings.host, port=settings.port)
    uvicorn.run("context_observability.main:app", host=settings.host, port=settings.port, reload=True)
