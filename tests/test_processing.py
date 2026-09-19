import pandas as pd
import pytest

from src.processing.clean_data import clean_data


@pytest.mark.skip(reason="Not relevant for now")
def test_clean_data_removes_duplicates():
    df = pd.DataFrame({
        "InvoiceNo": ["10001", "10001"],
        "StockCode": ["A", "A"],
        "Description": ["Product A", "Product A"],
        "Quantity": [2, 2],
        "InvoiceDate": pd.to_datetime(["2025-01-01", "2025-01-01"]),
        "UnitPrice": [10.0, 10.0],
        "CustomerID": [12345, 12345],
        "Country": ["United Kingdom", "United Kingdom"],
    })

    result = clean_data(df)

    assert len(result) == 1


@pytest.mark.skip(reason="Not relevant for now")
def test_clean_data_removes_cancelled_invoices():
    df = pd.DataFrame({
        "InvoiceNo": ["10001", "C10002"],
        "StockCode": ["A", "B"],
        "Description": ["Product A", "Product B"],
        "Quantity": [2, -1],
        "InvoiceDate": pd.to_datetime(["2025-01-01", "2025-01-01"]),
        "UnitPrice": [10.0, 10.0],
        "CustomerID": [12345, 12345],
        "Country": ["United Kingdom", "United Kingdom"],
    })

    result = clean_data(df)

    assert len(result) == 1
    assert result.iloc[0]["InvoiceNo"] == "10001"


@pytest.mark.skip(reason="Not relevant for now")
def test_clean_data_removes_invalid_quantity_and_price():
    df = pd.DataFrame({
        "InvoiceNo": ["10001", "10002", "10003"],
        "StockCode": ["A", "B", "C"],
        "Description": ["A", "B", "C"],
        "Quantity": [2, 0, -1],
        "InvoiceDate": pd.to_datetime([
            "2025-01-01",
            "2025-01-01",
            "2025-01-01",
        ]),
        "UnitPrice": [10.0, 10.0, 10.0],
        "CustomerID": [12345, 12345, 12345],
        "Country": ["United Kingdom"] * 3,
    })

    result = clean_data(df)

    assert len(result) == 1


@pytest.mark.skip(reason="Not relevant for now")
def test_clean_data_removes_missing_description():
    df = pd.DataFrame({
        "InvoiceNo": ["10001", "10002"],
        "StockCode": ["A", "B"],
        "Description": ["Product A", None],
        "Quantity": [2, 2],
        "InvoiceDate": pd.to_datetime([
            "2025-01-01",
            "2025-01-01",
        ]),
        "UnitPrice": [10.0, 10.0],
        "CustomerID": [12345, 12345],
        "Country": ["United Kingdom", "United Kingdom"],
    })

    result = clean_data(df)

    assert len(result) == 1
    assert result.iloc[0]["Description"] == "Product A"