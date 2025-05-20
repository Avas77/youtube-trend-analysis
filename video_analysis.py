import pandas as pd
import streamlit as st
from postgres_setup import get_engine

engine = get_engine()

@st.cache_data
def load_data():
    return pd.read_sql('SELECT * from trending_videos_cleaned', con=engine)

def get_filtered_df(df, min_views, sort_by, top_n):
    return df[df['view_count'] >= min_views].sort_values(by=sort_by, ascending=False).head(top_n)

def get_top_channels_views(df, sort_by, top_n):
    top_channels = df.groupby('channel')['view_count'].sum()
    return top_channels.sort_values(ascending=False).head(top_n)

def get_average_views_per_channel(df, sort_by, top_n):
    average_views = df.groupby('channel')['view_count'].mean()
    return average_views.sort_values(ascending=False).head(top_n)

def extract_time_features(df):
    df['published_at'] = pd.to_datetime(df['published_at'], utc=True)
    df['hour'] = df['published_at'].dt.hour
    df['day_of_week'] = df['published_at'].dt.day_name()
    return df

def get_hourly_distribution(df):
    return df['hour'].value_counts().sort_index()

def get_engagement_by_day(df):
    df['engagement'] = (df['comment_count'] + df['like_count']) / df['view_count']
    return df.groupby('day_of_week')['engagement'].mean().sort_values(ascending=False)

def get_correlation(df):
    return df[["view_count", "like_count", "comment_count", "engagement_percent"]].corr()