import streamlit as st
import pandas as pd
from postgres_setup import get_engine
import seaborn as sns
import matplotlib.pyplot as plt

engine = get_engine()

@st.cache_data
def load_data():
    return pd.read_sql('SELECT * from trending_videos_cleaned', con=engine)

df = load_data()

st.title("📊 YouTube Trending Dashboard")

st.sidebar.header("Filters")
min_views = st.sidebar.slider("Minimum Views", 0, int(df['view_count'].max()), 1000)
sort_by = st.sidebar.selectbox("Sort By", ['view_count', 'engagement_percent', 'video_age_days'])
top_n = st.sidebar.slider("Top N Videos", 5, 50, 10)

filtered_df = df[df['view_count'] >= min_views].sort_values(by=sort_by, ascending=False).head(top_n)

# Display Table
st.subheader(f"Top {top_n} Videos sorted by {sort_by}")
st.dataframe(filtered_df[['title', 'channel', 'view_count', 'engagement_percent', 'video_age_days']])

# Charts
st.subheader("📈 Views vs Engagement")
st.bar_chart(filtered_df.set_index('title')[['view_count', 'engagement_percent']])

st.subheader("📅 Video Age Distribution")
fig, ax = plt.subplots()
sns.histplot(df['video_age_days'], kde=True, ax=ax)
st.pyplot(fig)

# Footer
st.caption("Built with 💙 by Avas | Data from YouTube API")