import pandas as pd
from pathlib import Path
from database import get_connection

# dataset folder path
DATASET_PATH = Path(__file__).resolve().parent.parent.parent / "dataset"

def load_tables():

    conn = get_connection()

    for folder in DATASET_PATH.iterdir():

        if folder.is_dir():

            csv_files = list(folder.glob("*.csv"))

            if not csv_files:
                continue

            df = pd.concat([pd.read_csv(f) for f in csv_files])

            table_name = folder.name

            df.to_sql(table_name, conn, if_exists="replace", index=False)

            print(f"Loaded {table_name}")

    conn.close()


if __name__ == "__main__":
    load_tables()