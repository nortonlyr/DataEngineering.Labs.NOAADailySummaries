import json
import os
import pickle
from typing import Dict
import pandas as pd


def read_json(file_path: str) -> Dict:
    with open(file_path) as f:
        json_input = json.load(f)
    return json_input


def read_all_json_files(JSON_ROOT):
    for dirpath, dirname, filenames in os.walk(JSON_ROOT):
        result = []
        for f in filenames:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(JSON_ROOT, f))
                for i in json_content['results']:
                    i['source'] = f 
                    result.append(i)
    df_location = pd.DataFrame(result)
    return df_location


def read_all_json_files2(json_root):
    for root, _, files in os.walk(json_root):
        result = []
        for f in files:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(json_root, f))
                result.append(json_content)
    return result




def write_pickle(file_path, data):
    with open(file_path, "wb") as handler:
        pickle.dump(data, handler)


def load_pickle(file_path):
    with open(file_path, 'rb') as handler:
        data = pickle.load(handler)
    return data


if __name__ == "__main__":

    # Part 2 Proof

    content = read_all_json_files('./data/marvel')
    print(content)

    write_pickle("marvel.pickle", content)
    marvel_content = load_pickle("marvel.pickle")
    print(marvel_content)

