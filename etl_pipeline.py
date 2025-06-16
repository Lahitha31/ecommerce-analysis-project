import logging
from ingest.load_raw_data import load_raw_olist_data
from transform.merge_and_clean import get_clean_data
from transform.add_features import add_features

import pandas as pd
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    logging.info("Starting ETL pipeline")

    df = get_clean_data()
    df = add_features(df) 

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/olist_enhanced_data.csv", index=False)

    logging.info("ETL pipeline completed successfully. Data saved to data/processed/olist_enhanced_data.csv")

except Exception as e:
    logging.error("ETL pipeline failed")
    logging.exception(e)
