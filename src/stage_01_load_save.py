### Step : 1
from src.utils.all_utils import read_config, create_directory
import argparse
import pandas as pd
import os

### Step : 3
def get_data(config_path):
    config = read_config(config_path)
    # print(config)
    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path,sep=";")
    # print(df.head())

    # Save Dataset in the Local Directory
    # create a path to directory : artifacts/raw_local_dir/data.csv
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    create_directory(dirs=[raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    # print("raw_local_file_path : ",raw_local_file_path)

    df.to_csv(raw_local_file_path,sep=",",index=False)

    


### Step : 2
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c", default='config/config.yaml')
    parsed_args = args.parse_args()
    # print(parsed_args)
    get_data(config_path=parsed_args.config)
