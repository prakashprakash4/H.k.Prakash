import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page Config
st.set_page_config(page_title="Personal Expense Dashboard", layout="wide")

# Title
st.title("💰 Personal Expense Dashboard")

# Sample Expense Data
np.random.seed(42)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

categories = [
    "Food", "Travel", "Shopping",
    "Bills", "Entertainment", "Medical"
]

data = {
    "Month": np.random.choice(months, 200),
    "Category": np.random.choice(categories, 200),
    "Expense": np.random.randint(500, 10000, 200),
    "Income": np.random.randint(15000, 50000, 200)
}

df = pd.DataFrame(data)

# Sidebar Filter
st.sidebar.header("Filter Data")

selected_month = st.sidebar.multiselect(
    "Select Month",
    options=df["Month"].unique(),
    default=df["Month"].unique()
)

filtered_df = df[df["Month"].isin(selected_month)]

# KPI Cards
total_income = filtered_df["Income"].sum()
total_expense = filtered_df["Expense"].sum()
savings = total_income - total_expense

col1, col2, col3 = st.columns(3)

col1.metric("Total Income", f"₹{total_income:,}")
col2.metric("Total Expense", f"₹{total_expense:,}")
col3.metric("Savings", f"₹{savings:,}")

st.markdown("---")

# Expense by Category
category_expense = filtered_df.groupby("Category")[
    "Expense"
].sum().reset_index()

fig1 = px.pie(
    category_expense,
    names="Category",
    values="Expense",
    title="Expense by Category"
)

# Monthly Expense Trend
monthly_expense = filtered_df.groupby("Month")[
