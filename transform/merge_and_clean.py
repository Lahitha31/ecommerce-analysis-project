import pandas as pd

def merge_data(data_dict):
    df = data_dict["orders"] \
        .merge(data_dict["order_items"], on="order_id", how="left") \
        .merge(data_dict["payments"], on="order_id", how="left") \
        .merge(data_dict["products"], on="product_id", how="left") \
        .merge(data_dict["customers"], on="customer_id", how="left") \
        .merge(data_dict["reviews"], on="order_id", how="left")

    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
    df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])

    return df
