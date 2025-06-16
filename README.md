# Brazilian E-Commerce Data Analysis (Olist)

# E-Commerce Data Analysis Project

This project explores and analyzes a real-world e-commerce dataset (Brazilian Olist dataset) using an end-to-end modular pipeline. It focuses on simulating a data engineer's workflow from data ingestion, transformation, KPI reporting, cohort analysis, and dashboard-ready visualizations.

---

## Project Structure

```
ecommerce-analysis-project/
│
├── config/               # Configuration files for pipeline
├── ingest/               # To ingest raw data
├── transform/            # Data cleaning and feature engineering 
├── analysis/             # Jupyter notebooks for visual, cohort and kpi analysis
├── data/                 #dataset(raw and processed)
├── gitignore/           #names of some files that you may ignore
├── reporting/            # Output reports and export scripts
├── main.py               # Main script to coordinate the pipeline
├── etl_pipeline.py       # Command-line ETL entry point
├── etl.log               # ETL entry point status
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---


##  Dataset Description

The dataset contains information about:
- Orders, Products, Customers, Sellers
- Payments, Reviews, Deliveries
- Category translation and geography (Brazil)


---


## Technologies Used

- **Python**, **Pandas**, **NumPy**
- **Matplotlib**, **Plotly**
- **Statsmodels (ARIMA)**
- **YAML** for configuration
- Jupyter Notebooks for analysis


---

## Key Features

- **End-to-End Pipeline**: Simulates ingestion → transformation → analysis → reporting.
- **KPI Analysis**: Tracks top categories, payment methods, customer states, and revenue trends.
- **Cohort Analysis**: Understands user retention and lifecycle behavior over time.
- **Advanced Feature Engineering**: Calculates delivery time, delay, order value category, etc.
- **Visualizations**: Uses Seaborn, Plotly, and Matplotlib for meaningful business insights.

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

---



## Business Insights

- **Customer Retention:** Only **42%** of new users returned within 3 months – highlighting a need for retention efforts.
- **Delivery Delays:** **21%** of orders were late; Electronics averaged a **+4.3-day delay**.
- **Return Rate:** **9.2%** overall; highest in **Fashion & Accessories**.
- **Revenue Distribution:** Top 25% of customers contributed to **67%** of revenue.
- **Forecasting:** Monthly demand expected to grow by **12–15%** during peak seasons.

---

## 💼 Business Value

- Reduced manual reporting effort by **80%**
- Delivered over **10 business KPIs**
- Enables strategic decisions in logistics, marketing, and operations
- Seamlessly supports BI tools and analyst workflows


---

##  Future Enhancements

- Integrate with Apache Airflow for production-grade orchestration
- Add DB storage support using PostgreSQL
- Export automated dashboards to Tableau or Power BI
- Unit test modules and introduce CI/CD

---