import os
import pandas as pd

DATASET_PATH = "../../dataset"

def load_folder(folder):
    path = os.path.join(DATASET_PATH, folder)

    if not os.path.exists(path):
        print("Folder not found:", folder)
        return

    for file in os.listdir(path):
        if file.endswith(".jsonl"):
            file_path = os.path.join(path, file)

            df = pd.read_json(file_path, lines=True)

            print(f"\nLoaded {file}")
            print("Rows:", len(df))
            print("Columns:", list(df.columns))

folders = os.listdir(DATASET_PATH)

for folder in folders:
    load_folder(folder)