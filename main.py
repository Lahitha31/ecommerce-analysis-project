from ingest.load_raw_data import load_raw_data
from transform.merge_and_clean import merge_data
import yaml

def run_pipeline(config_path="config/config.yaml"):
    print("Reading config...")
    data_dict = load_raw_data(config_path)
    print("Data loaded.")

    print("Merging and transforming...")
    final_df = merge_data(data_dict)

    with open(config_path) as f:
        config = yaml.safe_load(f)
    output_path = config["processed_data_path"]

    print(f"Saving final dataset to {output_path}")
    final_df.to_csv(output_path, index=False)

if __name__ == "__main__":
    run_pipeline()
