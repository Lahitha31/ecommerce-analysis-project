import pandas as pd

def load_raw_olist_data(base_path="C:/Users/MSI/Desktop/ecommerce-analysis-project/data/raw/"):


    datasets = {
        "orders": pd.read_csv(base_path + "olist_orders_dataset.csv"),
        "order_items": pd.read_csv(base_path + "olist_order_items_dataset.csv"),
        "payments": pd.read_csv(base_path + "olist_order_payments_dataset.csv"),
        "products": pd.read_csv(base_path + "olist_products_dataset.csv"),
        "customers": pd.read_csv(base_path + "olist_customers_dataset.csv"),
        "reviews": pd.read_csv(base_path + "olist_order_reviews_dataset.csv"),
        "sellers": pd.read_csv(base_path + "olist_sellers_dataset.csv"),
        "category_translation": pd.read_csv(base_path + "product_category_name_translation.csv")
    }
    return datasets
