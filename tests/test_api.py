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

def test_revenue_by_country_endpoint():
    response = client.get("/api/analytics/revenue/by-country")

    assert response.status_code == 200

    data = response.json()

    assert "countries" in data
    assert isinstance(data["countries"], list)
    assert len(data["countries"]) > 0

    for country in data["countries"]:
        assert "country" in country
        assert "revenue" in country

def test_revenue_by_country_is_sorted():
    response = client.get("/api/analytics/revenue/by-country")

    data = response.json()["countries"]

    revenues = [country["revenue"] for country in data]

    assert revenues == sorted(revenues, reverse=True)


def test_monthly_revenue_endpoint():
    response = client.get("/api/analytics/revenue/monthly")

    assert response.status_code == 200

    data = response.json()

    assert "monthly_revenue" in data
    assert isinstance(data["monthly_revenue"], list)
    assert len(data["monthly_revenue"]) > 0

    for month in data["monthly_revenue"]:
        assert "month" in month
        assert "revenue" in month

def test_monthly_revenue_is_sorted():
    response = client.get("/api/analytics/revenue/monthly")

    data = response.json()["monthly_revenue"]

    months = [item["month"] for item in data]

    assert months == sorted(months)