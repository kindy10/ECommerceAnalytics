import pandas as pd

from src.database.connection import engine


def load_to_database(df: pd.DataFrame) -> None:
    """
    Load cleaned transaction data into the transactions table.

    Args:
        df: Cleaned transaction DataFrame.
    """
    df_to_load = df.rename(
        columns={
            "InvoiceNo": "invoice_no",
            "StockCode": "stock_code",
            "Description": "description",
            "Quantity": "quantity",
            "InvoiceDate": "invoice_date",
            "UnitPrice": "unit_price",
            "CustomerID": "customer_id",
            "Country": "country",
        }
    )

    df_to_load.to_sql(
        "transactions",
        con=engine,
        if_exists="append",
        index=False,
    )