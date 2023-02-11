### Step : 1
from src.utils.all_utils import read_config, create_directory, save_local_df
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split

### Step : 3
def split_and_save(config_path, params_path):
    config = read_config(config_path)
    params = read_config(params_path)
    # print(config)

    # Read data from artifacts
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]
    split_data_dir = config["artifacts"]["split_data_dir"]
    train_data_filename = config["artifacts"]["train"]
    test_data_filename = config["artifacts"]["test"]

    random_state = params["base"]["random_state"]
    test_size = params["base"]["test_size"]

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    create_directory(dirs=[raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    # print("raw_local_file_path : ",raw_local_file_path)

    df = pd.read_csv(raw_local_file_path)
    # print(df.head())

    train , test = train_test_split(df,test_size=test_size,random_state=random_state)

    create_directory(dirs=[os.path.join(artifacts_dir,split_data_dir)])
    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_filename)
    test_data_path = os.path.join(artifacts_dir,split_data_dir,test_data_filename)

    save_local_df(train,train_data_path)
    save_local_df(test,test_data_path)



    


### Step : 2
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c", default='config/config.yaml')
    args.add_argument("--params","-p", default='params.yaml')
    parsed_args = args.parse_args()
    # print(parsed_args)
    split_and_save(config_path=parsed_args.config,params_path=parsed_args.params)
