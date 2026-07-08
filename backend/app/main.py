from fastapi import FastAPI

app = FastAPI(
    title="AI Image Management API",
    description="Backend API for AI Image Management System",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Image Management System"
    }
