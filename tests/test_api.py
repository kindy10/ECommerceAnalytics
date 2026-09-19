from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "ECommerce Analytics API"
    assert data["status"] == "running"


def test_revenue_endpoint():
    response = client.get("/api/analytics/revenue")

    assert response.status_code == 200

    data = response.json()

    assert "total_revenue" in data
    assert isinstance(data["total_revenue"], float)
    assert data["total_revenue"] > 0