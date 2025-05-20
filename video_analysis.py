import pandas as pd
import streamlit as st
from postgres_setup import get_engine

class VideoAnalysis:
    def __init__(self):
        self.df = self._load_and_prepare_data()
    @st.cache_data
    def _load_data(_self):
        engine = get_engine()
        return pd.read_sql('SELECT * from trending_videos_cleaned', con=engine)
    def _load_and_prepare_data(self):
        df = self._load_data()
        df['published_at'] = pd.to_datetime(df['published_at'], utc=True)
        df['hour'] = df['published_at'].dt.hour
        df['day_of_week'] = df['published_at'].dt.day_name()
        df['engagement'] = (df['comment_count'] + df['like_count']) / (df['view_count'] + 1e-6)
        return df
    def get_df(self):
        return self.df
    def get_filtered_df(self, min_views=0, sort_by='view_count', top_n=10):
        return self.df[self.df['view_count'] >= min_views].sort_values(by=sort_by, ascending=False).head(top_n)
    def get_top_channels_views(self, top_n=10):
        top_channels = self.df.groupby('channel')['view_count'].sum()
        return top_channels.sort_values(ascending=False).head(top_n)
    def get_average_views_per_channel(self, top_n=10):
        average_views = self.df.groupby('channel')['view_count'].mean()
        return average_views.sort_values(ascending=False).head(top_n)
    def get_hourly_distribution(self):
        return self.df['hour'].value_counts().sort_index()
    def get_engagement_by_day(self):
        self.df['engagement'] = (self.df['comment_count'] + self.df['like_count']) / self.df['view_count']
        return self.df.groupby('day_of_week')['engagement'].mean().sort_values(ascending=False)

    def get_correlation(self):
        return self.df[["view_count", "like_count", "comment_count", "engagement_percent"]].corr()





