import pandas as pd

def calculate_total_revenue(df:pd.DataFrame) ->float:
    """
    Calculate total revenue from transaction data.
    Revenue is calculated as:
        Quantity * UnitPrice
    """
    return float((df["Quantity"] * df["UnitPrice"]).sum())

def calculate_transaction_count(df:pd.DataFrame) ->int:
    """
    Calculate the number of transactions.
    """
    return int(len(df))

def get_top_selling_products(df:pd.DataFrame,limit:int =10)->pd.DataFrame:
    """
    Return the top_selling products by total quantity sold.
    """
    result = (df.groupby(
        ["StockCode","Description"],as_index=False,
    )["Quantity"]
              .sum()
              .sort_values("Quantity",ascending=False)
              .head(limit)
             )
    return result


def get_revenue_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total revenue for each country.
    """
    result = df.copy()

    result["Revenue"] = result["Quantity"] * result["UnitPrice"]

    return (
        result.groupby("Country", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
    )

def get_monthly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total revenue for each month.
    """
    result = df.copy()

    result["Revenue"] = result["Quantity"] * result["UnitPrice"]

    result["Month"] = result["InvoiceDate"].dt.to_period("M")

    return (
        result.groupby("Month", as_index=False)["Revenue"]
        .sum()
        .sort_values("Month")
    )

