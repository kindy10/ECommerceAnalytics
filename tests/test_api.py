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


def test_transaction_count_endpoint():
    response = client.get("/api/analytics/transactions/count")

    assert response.status_code == 200

    data = response.json()

    assert "transaction_count" in data
    assert data["transaction_count"] == 524878


def test_top_products_endpoint():
    response = client.get("/api/analytics/products/top")

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) == 10

    for product in data["products"]:
        assert "stock_code" in product
        assert "description" in product
        assert "quantity_sold" in product
        
def test_top_products_endpoint_with_limit():
    response = client.get("/api/analytics/products/top?limit=5")

    assert response.status_code == 200

    data = response.json()

    assert len(data["products"]) == 5