import os
import pandas as pd
from ingest.load_raw_data import load_raw_olist_data

def get_clean_data():
    data = load_raw_olist_data()

    df = data["orders"] \
        .merge(data["order_items"], on="order_id", how="inner") \
        .merge(data["products"][["product_id", "product_category_name"]], on="product_id", how="left") \
        .merge(data["category_translation"], on="product_category_name", how="left") \
        .merge(data["payments"], on="order_id", how="left") \
        .merge(data["customers"], on="customer_id", how="left")

    df["TotalAmount"] = df["price"] + df["freight_value"]

    # Create the directory if it doesn't exist
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/olist_cleaned_data.csv", index=False)

    return df
