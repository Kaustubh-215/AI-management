from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.v1.api import api_router

app = FastAPI(
    title="AI Images Management API",
    version="1.0.0",
    description="Backend API for AI Image Management System",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://34.212.58.132:5173",
        "https://34.212.58.132.nip.io",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(api_router, prefix="/api/v1")
