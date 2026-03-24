import os
import pandas as pd
import networkx as nx

DATASET_PATH = "../../dataset"

graph = nx.DiGraph()

def load_json_folder(folder):

    folder_path = os.path.join(DATASET_PATH, folder)
    dataframes = []

    if not os.path.exists(folder_path):
        return None

    for file in os.listdir(folder_path):
        if file.endswith(".jsonl"):
            path = os.path.join(folder_path, file)
            df = pd.read_json(path, lines=True)
            dataframes.append(df)

    if len(dataframes) == 0:
        return None

    return pd.concat(dataframes)


def build_graph():

    print("Loading datasets...")

    sales_orders = load_json_folder("sales_orders")
    sales_order_items = load_json_folder("sales_order_items")

    print("Building graph...")

    if sales_orders is not None:
        for _, row in sales_orders.iterrows():
            graph.add_node(row["salesOrder"], type="sales_order")

            if "soldToParty" in row:
                graph.add_edge(row["soldToParty"], row["salesOrder"], relation="placed")

    if sales_order_items is not None:
        for _, row in sales_order_items.iterrows():
            graph.add_edge(row["salesOrder"], row["material"], relation="contains_product")

    print("Graph built successfully")
    print("Nodes:", graph.number_of_nodes())
    print("Edges:", graph.number_of_edges())


if __name__ == "__main__":
    build_graph()