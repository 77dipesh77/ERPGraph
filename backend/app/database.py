import sqlite3
from pathlib import Path

# database file location
DB_PATH = Path(__file__).resolve().parent.parent / "erp.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn