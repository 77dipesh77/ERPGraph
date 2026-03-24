import pandas as pd
import os

DATASET_PATH = "../../dataset"

def load_json_folder(folder):

    folder_path = os.path.join(DATASET_PATH, folder)
    dataframes = []

    for file in os.listdir(folder_path):
        if file.endswith(".jsonl"):
            path = os.path.join(folder_path, file)
            df = pd.read_json(path, lines=True)
            dataframes.append(df)

    if len(dataframes) == 0:
        return None

    return pd.concat(dataframes)


def most_ordered_products():

    sales_items = load_json_folder("sales_order_items")

    counts = sales_items["material"].value_counts()

    return counts.head(10)


if __name__ == "__main__":

    result = most_ordered_products()

    print("Top Products:")
    print(result)