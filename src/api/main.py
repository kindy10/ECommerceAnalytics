from fastapi import FastAPI

app = FastAPI(
    title="ECommerce Analytics API",
    description="REST API for e-commerce analytics.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "ECommerce Analytics API",
        "status": "running",
    }