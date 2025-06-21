# Brazilian E-Commerce Data Analysis (Olist)

# E-Commerce Data Analysis Project

This project explores and analyzes a real-world e-commerce dataset (Brazilian Olist dataset) using an modular pipeline. It focuses on simulating a data engineer's workflow from data ingestion, transformation, KPI reporting, cohort analysis, and dashboard-ready visualizations.

---

## Project Structure

```
ecommerce-analysis-project/
├── analysis/ # Jupyter notebooks for business analysis
│ ├── Monthly_sales
│ ├── Delivery_performance
│ ├── churn_prediction
│ └── productcategory_performance
├── config/
│ └── config.yaml # Centralized config for paths
├── data/
│ ├── raw/ # Original raw CSV files
│ └── processed/ # Cleaned and transformed datasets
├── ingest/
│ └── load_raw_data.py # Reads config and loads raw files
├── transform/
│ ├── merge_and_clean.py # Merge, clean, and enhance raw data
│ └── add_features.py # Feature engineering for analysis
├── dashboard_app.py # Streamlit dashboard app
├── etl_pipeline.py # Runs full ETL pipeline
├── main.py # Main entry point to orchestrate everything
├── requirements.txt # Project dependencies
└── README.md

---


##  Dataset Description
The dataset is publicly available from Kaggle and includes:

- Order details (timestamps, payments, reviews)
- Customer and seller information
- Products with category metadata
- Geolocation data


---


## Technologies Used

- **Python**, **Pandas**, **NumPy** – ETL and feature engineering
- **Matplotlib**, **Seaborn**, **Plotly** – Data visualization
- **Scikit-learn** – KMeans for customer segmentation
- **Streamlit** – Interactive dashboard
- **YAML** – Config management

---
##  Key Features

-  Modular ETL pipeline with config-driven ingestion and transformation
-  Trend and performance analysis using Jupyter notebooks
-  Data cleaning and preprocessing from 9 interconnected CSV files
-  Product category and monthly sales performance tracking
-  Delivery time analysis and its impact on customer satisfaction
-  Interactive dashboard using Streamlit
-  Business-friendly insights presented with visual storytelling

---


##  How to Run

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute the pipeline:
   ```bash
   python etl_pipeline.py
   ```

3. Open and explore analysis notebooks:
   - `analysis/kpi_analysis.ipynb`
   - `analysis/visual_analysis.ipynb`
   - `analysis/cohort_analysis.ipynb`

4. Launch the Streamlit Dashboard
```bash
   streamlit run dashboard_app.py
---


## Business Insights
- **Sales Trends**: Revenue peaks during Q4, indicating seasonal demand spikes.
- **Delivery Performance**: Slower deliveries correlate with lower review scores.
- **Product Performance**: Categories like `beleza_saude` and `relógios_presentes` drive highest revenue.
- **Churn Risk**: Customers with high wait times and low orders show churn tendencies.
- **Customer Segments**: Segments based on frequency, recency, and spending help in targeting offers.

---

##  Future Enhancements

- Integrate with Apache Airflow for production-grade orchestration
- Add DB storage support using PostgreSQL
- Export automated dashboards to Tableau or Power BI
- Unit test modules and introduce CI/CD

---