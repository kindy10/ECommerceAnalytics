from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)

    invoice_no = Column(String, nullable=False)
    stock_code = Column(String, nullable=False)
    description = Column(String, nullable=False)

    quantity = Column(Integer, nullable=False)
    invoice_date = Column(DateTime, nullable=False)
    unit_price = Column(Float, nullable=False)

    customer_id = Column(Float, nullable=True)
    country = Column(String, nullable=False)