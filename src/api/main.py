from fastapi import FastAPI
from src.api.analytics import router as analytics_router

app = FastAPI(
    title="ECommerce Analytics API",
    description="REST API for e-commerce analytics.",
    version="1.0.0",
)

app.include_router(analytics_router)

@app.get("/")
def root():
    return {
        "message": "ECommerce Analytics API",
        "status": "running",
    }