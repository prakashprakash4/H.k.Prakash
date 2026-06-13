import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page title
st.set_page_config(page_title="Sales Performance Dashboard", layout="wide")

st.title("📊 Sales Performance Dashboard")

# Sample Sales Data
np.random.seed(42)

months = pd.date_range(start='2025-01-01', periods=12, freq='M')

data = {
    "Date": np.random.choice(months, 500),
    "Region": np.random.choice(["North", "South", "East", "West"], 500),
    "Product": np.random.choice(["Laptop", "Mobile", "Tablet", "Headphones"], 500),
    "Sales": np.random.randint(1000, 10000, 500),
    "Profit": np.random.randint(200, 3000, 500),
    "Orders": np.random.randint(1, 10, 500)
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter Data")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_df = df[df["Region"].isin(region)]

# KPI Cards
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Orders"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{total_sales:,}")
col2.metric("Total Profit", f"₹{total_profit:,}")
col3.metric("Total Orders", total_orders)

st.markdown("---")

# Monthly Sales Trend
monthly_sales = filtered_df.groupby(
    filtered_df["Date"].dt.strftime('%b')
)["Sales"].sum().reset_index()

fig1 = px.line(
    monthly_sales,
    x="Date",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

# Region-wise Sales
region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()

fig2 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Region-wise Sales",
    text_auto=True
)

# Top Products
product_sales = filtered_df.groupby("Product")["Sales"].sum().reset_index()

fig3 = px.pie(
    product_sales,
    names="Product",
    values="Sales",
    title="Top Products"
)

# Layout
col4, col5 = st.columns(2)

with col4:
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    st.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig3, use_container_width=True)
