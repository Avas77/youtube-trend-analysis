from sqlalchemy import create_engine
import pandas as pd

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'youtube_data'

conn_str = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

def get_engine():
    return create_engine(conn_str)

engine = get_engine()

df = pd.read_csv('dataset/trending_videos_US_20250511_100254.csv')
# Ensure correct column types for PostgreSQL
df['published_at'] = pd.to_datetime(df['published_at'])

# Write to PostgreSQL (table will be created if it doesn't exist)
table_name = 'trending_videos'

df.to_sql(table_name, con=engine, if_exists='append', index=False)

print(f"Data inserted into PostgreSQL table: {table_name}")
