import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the raw ecommerce transaction data.

    Args:
        df: Raw transaction DataFrame.

    Returns:
        Cleaned transaction DataFrame.
    """
    cleaned_df = df.copy()

    # Remove duplicate rows
    cleaned_df = cleaned_df.drop_duplicates()

    # Remove rows with missing product descriptions
    cleaned_df = cleaned_df.dropna(subset=["Description"])

    # Remove cancelled/returned transactions
    cleaned_df = cleaned_df[
        ~cleaned_df["InvoiceNo"].astype(str).str.startswith("C")
    ]

    # Keep only positive quantities and prices
    cleaned_df = cleaned_df[
        (cleaned_df["Quantity"] > 0)
        & (cleaned_df["UnitPrice"] > 0)
    ]

    return cleaned_df