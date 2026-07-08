from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="AI Image Management API",
    description="Backend API for AI Image Management System",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Image Management System"
    }
