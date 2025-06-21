import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

st.title("E-commerce Analysis Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/olist_enhanced_data.csv", parse_dates=["order_purchase_timestamp"])

df = load_data()

pages = [
    "Monthly Sales Trends",
    "Product Category Performance",
    "Delivery Performance vs Reviews"
]
page = st.sidebar.radio("Select Analysis", pages)


if page == "Monthly Sales Trends":
    st.subheader(" Monthly Sales Trends")
    df["Month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)
    monthly_sales = df.groupby("Month")["payment_value"].sum().reset_index()

    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(data=monthly_sales, x="Month", y="payment_value", marker="o", ax=ax)
    plt.xticks(rotation=45)
    ax.set_title("Total Sales per Month")
    ax.set_ylabel("Revenue (BRL)")
    st.pyplot(fig)

elif page == "Product Category Performance":
    st.subheader(" Top 10 Product Categories by Revenue")
    category_sales = df.groupby("product_category_name")[["payment_value"]].sum().sort_values(by="payment_value", ascending=False).head(10).reset_index()

    fig, ax = plt.subplots(figsize=(12, 4))
    sns.barplot(data=category_sales, x="payment_value", y="product_category_name", ax=ax)
    ax.set_title("Top 10 Product Categories by Revenue")
    ax.set_xlabel("Revenue (BRL)")
    st.pyplot(fig)


elif page == "Delivery Performance vs Reviews":
    st.subheader(" Delivery Days vs Review Score")
    delivered = df.dropna(subset=["order_delivered_customer_date"])
    delivered["delivery_days"] = (pd.to_datetime(delivered["order_delivered_customer_date"]) - pd.to_datetime(delivered["order_purchase_timestamp"])).dt.days

    fig, ax = plt.subplots(figsize=(12, 4))
    sns.boxplot(x="review_score", y="delivery_days", data=delivered, ax=ax)
    ax.set_title("Delivery Days Distribution per Review Score")
    st.pyplot(fig)
