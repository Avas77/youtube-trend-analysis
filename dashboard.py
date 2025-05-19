import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from video_analysis import (load_data, get_filtered_df, get_top_channels_views, get_average_views_per_channel,
                            get_hourly_distribution, get_engagement_by_day, extract_time_features)

df = load_data()

st.title("📊 YouTube Trending Dashboard")

st.sidebar.header("Filters")
min_views = st.sidebar.slider("Minimum Views", 0, int(df['view_count'].max()), 1000)
sort_by = st.sidebar.selectbox("Sort By", ['view_count', 'engagement_percent', 'video_age_days'])
top_n = st.sidebar.slider("Top N Videos", 5, 50, 10)

filtered_df = get_filtered_df(df, min_views, sort_by, top_n)

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

st.subheader("🔝 Top 10 Channels by Total Views")
top_total = get_top_channels_views(filtered_df, sort_by, top_n)
st.bar_chart(top_total)

st.subheader("📊 Top 10 Channels by Average Views")
top_avg = get_average_views_per_channel(filtered_df, sort_by, top_n)
st.bar_chart(top_avg)

st.header("🕒 Time-Based Analysis")

transformed_df = extract_time_features(filtered_df)

st.subheader("🕓 What Time Are Videos Published?")
hourly_dist = get_hourly_distribution(transformed_df)
st.bar_chart(hourly_dist)

st.subheader("📆 Which Days Have Higher Engagement?")
engagement_by_day = get_engagement_by_day(transformed_df)
print(engagement_by_day)
st.bar_chart(engagement_by_day)

# Footer
st.caption("Built with 💙 by Avas | Data from YouTube API")