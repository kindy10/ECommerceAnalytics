import pandas as pd

from src.analytics.sales import *

def test_calculate_total_revenue():
    df = pd.DataFrame({
        "Quantity":[2,3,5],
        "UnitPrice":[10.0, 20.0, 5.0],
    })
    result = calculate_total_revenue(df)
    assert result == 105.0

def test_calculate_transaction_count():
    df = pd.DataFrame({
        "Quantity":[2,3,5],
        "UnitPrice":[10.0, 20.0, 5.0]
    })
    result = calculate_transaction_count(df)

    assert result == 3

def test_get_top_selling_products():
    df = pd.DataFrame({
        "StockCode": ["A", "A", "B", "C"],
        "Description": [
            "Product A",
            "Product A",
            "Product B",
            "Product C",
        ],
        "Quantity": [5, 10, 8, 3],
        "UnitPrice": [2.0, 2.0, 5.0, 10.0],
    })

    result = get_top_selling_products(df, limit=2)

    assert len(result) == 2
    assert result.iloc[0]["StockCode"] == "A"
    assert result.iloc[0]["Quantity"] == 15

def test_get_revenue_by_country():
    df = pd.DataFrame({
        "Country": [
            "United Kingdom",
            "United Kingdom",
            "Germany",
        ],
        "Quantity": [2, 3, 4],
        "UnitPrice": [10.0, 20.0, 5.0],
    })

    result = get_revenue_by_country(df)

    assert len(result) == 2

    uk_revenue = result.loc[
        result["Country"] == "United Kingdom",
        "Revenue",
    ].iloc[0]

    germany_revenue = result.loc[
        result["Country"] == "Germany",
        "Revenue",
    ].iloc[0]

    assert uk_revenue == 80.0
    assert germany_revenue == 20.0

def test_get_monthly_revenue():
    df = pd.DataFrame({
        "InvoiceDate": pd.to_datetime([
            "2010-12-01",
            "2010-12-15",
            "2011-01-05",
        ]),
        "Quantity": [2, 3, 4],
        "UnitPrice": [10.0, 20.0, 5.0],
    })

    result = get_monthly_revenue(df)

    assert len(result) == 2

    december_revenue = result.loc[
        result["Month"].astype(str) == "2010-12",
        "Revenue",
    ].iloc[0]

    january_revenue = result.loc[
        result["Month"].astype(str) == "2011-01",
        "Revenue",
    ].iloc[0]

    assert december_revenue == 80.0
    assert january_revenue == 20.0