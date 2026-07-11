from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.api.health import router as health_router
from app.api.v1.api import api_router

app = FastAPI(
    title="AI Image Management API",
    version="1.0.0",
    description="Backend API for AI Image Management System",
)

app.include_router(health_router)
app.include_router(api_router, prefix="/api/v1")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    openapi_schema["security"] = [
        {
            "BearerAuth": []
        }
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
