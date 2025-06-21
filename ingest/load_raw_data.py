import pandas as pd
import os
import yaml

def load_raw_data(config_path="config/config.yaml"):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    raw_path = config["raw_data_path"]
    files = config["files"]

    data = {}
    for key, file in files.items():
        path = os.path.join(raw_path, file)
        data[key] = pd.read_csv(path)
    return data
