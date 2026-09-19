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