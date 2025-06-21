import pandas as pd

def add_features(df):
    # Converting dates
    df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
    df["order_approved_at"] = pd.to_datetime(df["order_approved_at"])
    df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])

    # Delivery time in days
    df["delivery_time_days"] = (df["order_delivered_customer_date"] - df["order_approved_at"]).dt.days

    # Delay vs estimate 
    df["delay_vs_estimate"] = (df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]).dt.days

    # Categorizing order value
    bins = [0, 50, 150, df["TotalAmount"].max()]
    labels = ['Low', 'Medium', 'High']
    df["order_value_category"] = pd.cut(df["TotalAmount"], bins=bins, labels=labels)

    # Number of items per order
    item_counts = df.groupby("order_id")["order_item_id"].count().rename("items_per_order")
    df = df.merge(item_counts, on="order_id", how="left")

    return df
