import pandas as pd
import os
df = pd.read_csv("data/processed/olist_cleaned_data.csv")
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

#KPIs
total_sales = df['TotalAmount'].sum()
average_order_value = df.groupby('order_id')['TotalAmount'].sum().mean()
monthly_sales = df.set_index('order_purchase_timestamp').resample('M')['TotalAmount'].sum()
top_categories = df['product_category_name_english'].value_counts().head(5)

# Combining all KPIs
kpi_data = {
    'Total Sales': [round(total_sales, 2)],
    'Average Order Value': [round(average_order_value, 2)],
    'Top Categories': [", ".join(top_categories.index.tolist())],
    'Top Category Counts': [", ".join(top_categories.astype(str).tolist())],
}

kpi_df = pd.DataFrame(kpi_data)

#output directory
os.makedirs("data/reports", exist_ok=True)

kpi_df.to_csv("data/reports/kpis_summary.csv", index=False)
print(" KPI report saved to data/reports/kpis_summary.csv")
