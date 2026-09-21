from src.dashboard.api_client import (
    get_monthly_revenue,
    get_revenue_by_country,
    get_top_products,
    get_total_revenue,
    get_transaction_count,
)


class MockResponse:
    def __init__(self, data):
        self.data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self.data


def test_get_total_revenue(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(
            {"total_revenue": 1500.50}
        )

    monkeypatch.setattr(
        "src.dashboard.api_client.requests.get",
        mock_get,
    )

    result = get_total_revenue("http://test-api")

    assert result == 1500.50


def test_get_transaction_count(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(
            {"transaction_count": 500}
        )

    monkeypatch.setattr(
        "src.dashboard.api_client.requests.get",
        mock_get,
    )

    result = get_transaction_count("http://test-api")

    assert result == 500


def test_get_top_products(monkeypatch):
    products = [
        {
            "stock_code": "A001",
            "description": "Product A",
            "quantity_sold": 100,
        }
    ]

    def mock_get(*args, **kwargs):
        return MockResponse({"products": products})

    monkeypatch.setattr(
        "src.dashboard.api_client.requests.get",
        mock_get,
    )

    result = get_top_products("http://test-api")

    assert result == products


def test_get_revenue_by_country(monkeypatch):
    countries = [
        {
            "country": "United Kingdom",
            "revenue": 5000.0,
        }
    ]

    def mock_get(*args, **kwargs):
        return MockResponse({"countries": countries})

    monkeypatch.setattr(
        "src.dashboard.api_client.requests.get",
        mock_get,
    )

    result = get_revenue_by_country("http://test-api")

    assert result == countries


def test_get_monthly_revenue(monkeypatch):
    monthly_data = [
        {
            "month": "2010-12",
            "revenue": 1000.0,
        }
    ]

    def mock_get(*args, **kwargs):
        return MockResponse(
            {"monthly_revenue": monthly_data}
        )

    monkeypatch.setattr(
        "src.dashboard.api_client.requests.get",
        mock_get,
    )

    result = get_monthly_revenue("http://test-api")

    assert result == monthly_data