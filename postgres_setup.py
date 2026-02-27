from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os
import glob
import argparse

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

conn_str = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_engine():
    return create_engine(conn_str)

def get_latest_csv(dataset_dir: str = "dataset") -> str:
    pattern = os.path.join(dataset_dir, "*.csv")
    files = glob.glob(pattern)
    if not files:
        raise FileNotFoundError(f"No CSV files found in '{dataset_dir}'. Expected pattern: {pattern}")
    return max(files, key=os.path.getmtime)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        help="Path to input CSV. If omitted, loads the latest CSV from dataset/"
    )
    args = parser.parse_args()

    csv_path = args.input if args.input else get_latest_csv("dataset")
    print(f"Loading CSV: {csv_path}")

    engine = get_engine()

    df = pd.read_csv(csv_path)

    # Ensure correct column types for PostgreSQL
    if "published_at" in df.columns:
        df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")

    table_name = "trending_videos"
    df.to_sql(table_name, con=engine, if_exists="append", index=False)

    print(f"Data inserted into PostgreSQL table: {table_name}")

if __name__ == "__main__":
    main()