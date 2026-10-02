from fastapi import FastAPI
from app.api.routes import health

app = FastAPI(
    title="EVE Healthcare API",
    version="0.1.0",
    description="Backend service for diagnostic test bookings and simulated payments",
    openapi_tags=[
        {"name": "health", "description": "Healthcheck endpoint"}
    ]
)

app.include_router(health.router, tags=["health"])
