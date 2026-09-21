import requests

def get_total_revenue(api_url: str) -> float:
    response = requests.get(
        f"{api_url}/api/analytics/revenue",
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    return float(data["total_revenue"])


def get_transaction_count(api_url: str) -> int:
    response = requests.get(
        f"{api_url}/api/analytics/transactions/count",
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    return int(data["transaction_count"])


def get_top_products(
    api_url: str,
    limit: int = 10,
) -> list[dict]:
    response = requests.get(
        f"{api_url}/api/analytics/products/top",
        params={"limit": limit},
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    return data["products"]


def get_revenue_by_country(api_url: str) -> list[dict]:
    response = requests.get(
        f"{api_url}/api/analytics/revenue/by-country",
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    return data["countries"]


def get_monthly_revenue(api_url: str) -> list[dict]:
    response = requests.get(
        f"{api_url}/api/analytics/revenue/monthly",
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    return data["monthly_revenue"]