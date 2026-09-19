from fastapi import APIRouter
from sqlalchemy import text

from src.database.connection import engine


router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"],
)


@router.get("/revenue")
def get_total_revenue():
    query = text(
        """
        SELECT SUM(quantity * unit_price)
        FROM transactions
        """
    )

    with engine.connect() as connection:
        result = connection.execute(query).scalar()

    return {
        "total_revenue": float(result or 0)
    }


@router.get("/transactions/count")
def get_transaction_count():
    query = text(
        """
        SELECT COUNT(*)
        FROM transactions
        """
    )

    with engine.connect() as connection:
        result = connection.execute(query).scalar()

    return {
        "transaction_count":int(result or 0)
    }


@router.get("/products/top")
def get_top_products(limit: int = 10):
    query = text(
        """
        SELECT
            stock_code,
            description,
            SUM(quantity) AS quantity_sold
        FROM transactions
        GROUP BY stock_code, description
        ORDER BY quantity_sold DESC
        LIMIT :limit
        """
    )

    with engine.connect() as connection:
        rows = connection.execute(
            query,
            {"limit": limit},
        ).mappings().all()

    return {
        "products": [dict(row) for row in rows]
    }