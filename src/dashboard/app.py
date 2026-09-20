import requests
import streamlit as st


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
    revenue_response = requests.get(
        f"{API_URL}/api/analytics/revenue",
        timeout=5,
    )

    count_response = requests.get(
        f"{API_URL}/api/analytics/transactions/count",
        timeout=5,
    )

    revenue_response.raise_for_status()
    count_response.raise_for_status()

    revenue_data = revenue_response.json()
    count_data = count_response.json()

    total_revenue = revenue_data["total_revenue"]
    transaction_count = count_data["transaction_count"]

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

    products_response = requests.get(
        f"{API_URL}/api/analytics/products/top",
        params={"limit": 10},
        timeout=5,
    )

    products_response.raise_for_status()

    products_data = products_response.json()

    st.subheader("🏆 Top-Selling Products")

    st.dataframe(
        products_data["products"],
        use_container_width=True,
    )

except requests.RequestException:
    st.error(
        "Unable to connect to the Analytics API. "
        "Make sure the FastAPI server is running."
    )