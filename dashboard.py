import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from video_analysis import VideoAnalysis

analyzer = VideoAnalysis()
df = analyzer.get_df()

st.title("📊 YouTube Trending Dashboard")

st.sidebar.header("Filters")
min_views = st.sidebar.slider("Minimum Views", 0, int(df['view_count'].max()), 1000)
sort_by = st.sidebar.selectbox("Sort By", ['view_count', 'engagement_percent', 'video_age_days'])
top_n = st.sidebar.slider("Top N Videos", 5, 50, 10)

filtered_df = analyzer.get_filtered_df(min_views, sort_by, top_n)

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
top_total = analyzer.get_top_channels_views(top_n)
st.bar_chart(top_total)

st.subheader("📊 Top 10 Channels by Average Views")
top_avg = analyzer.get_average_views_per_channel(top_n)
st.bar_chart(top_avg)

st.header("🕒 Time-Based Analysis")

st.subheader("🕓 What Time Are Videos Published?")
hourly_dist = analyzer.get_hourly_distribution()
st.bar_chart(hourly_dist)

st.subheader("📆 Which Days Have Higher Engagement?")
engagement_by_day = analyzer.get_engagement_by_day()
print(engagement_by_day)
st.bar_chart(engagement_by_day)

st.subheader("📈 Correlation Analysis")
fig, ax = plt.subplots()
sns.heatmap(analyzer.get_correlation(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# Footer
st.caption("Built with 💙 by Avas | Data from YouTube API")