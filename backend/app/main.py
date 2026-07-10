from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.v1.api import api_router

app = FastAPI(
    title="AI Image Management API",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(api_router, prefix="/api/v1")
