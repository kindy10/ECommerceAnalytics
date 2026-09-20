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
    response = requests.get(
        f"{API_URL}/api/analytics/revenue",
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    total_revenue = data["total_revenue"]

    st.metric(
        label="Total Revenue",
        value=f"£{total_revenue:,.2f}",
    )

except requests.RequestException:
    st.error(
        "Unable to connect to the Analytics API. "
        "Make sure the FastAPI server is running."
    )