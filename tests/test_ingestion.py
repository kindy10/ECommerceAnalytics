import pandas as pd
import pytest

from src.ingestion.load_data import load_raw_data


@pytest.fixture(scope="session")
#@pytest.mark.skip(reason="Not relevant for now")
def raw_data():
    return load_raw_data()


@pytest.mark.skip(reason="Not relevant for now")
def test_load_raw_data(raw_data):
    assert isinstance(raw_data, pd.DataFrame)
    assert not raw_data.empty


@pytest.mark.skip(reason="Not relevant for now")
def test_raw_data_has_expected_columns(raw_data):
    expected_columns = [
        "InvoiceNo",
        "StockCode",
        "Description",
        "Quantity",
        "InvoiceDate",
        "UnitPrice",
        "CustomerID",
        "Country",
    ]

    assert raw_data.columns.tolist() == expected_columns