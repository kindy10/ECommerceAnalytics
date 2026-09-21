import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.dashboard.api_client import (
    get_monthly_revenue,
    get_revenue_by_country,
    get_top_products,
    get_total_revenue,
    get_transaction_count,
)

API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
)


st.title("📊 E-Commerce Analytics Dashboard")

st.write(
    "Interactive dashboard for exploring e-commerce sales data."
)


try:
    total_revenue = get_total_revenue(API_URL)
    transaction_count = get_transaction_count(API_URL)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Total Revenue",
            value=f"£{total_revenue:,.2f}",
        )

    with col2:
        st.metric(
            label="Transaction Count",
            value=f"{transaction_count:,}",
        )

    products = get_top_products(API_URL)

    st.subheader("🏆 Top-Selling Products")

    st.dataframe(
        products,
        use_container_width=True,
    )

    countries = get_revenue_by_country(API_URL)

    st.subheader("🌍 Revenue by Country")

    st.bar_chart(
        {
            item["country"]: item["revenue"]
            for item in countries
        }
    )

    monthly_revenue = get_monthly_revenue(API_URL)

    st.subheader("📈 Monthly Revenue")

    monthly_data = {
        item["month"]: item["revenue"]
        for item in monthly_revenue
    }

    st.line_chart(monthly_data)

except Exception as error:
    st.error(error)