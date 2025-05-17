from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime


# --- CONFIGURATION ---
API_KEY = 'AIzaSyCmBl5YX200cdYkxKjy7QOhzq13GFeNugY'
REGION = 'US'  # Change as needed
MAX_RESULTS = 50  # API max per call
OUTPUT_FORMAT = 'csv'

# --- YOUTUBE API CLIENT ---
youtube = build('youtube', 'v3', developerKey=API_KEY)

# --- API CALL ---
request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode=REGION,
    maxResults=MAX_RESULTS
)

response = request.execute()

video_data = []

for item in response['items']:
    video_info = {
        'video_id': item['id'],
        'title': item['snippet']['title'],
        'channel': item['snippet']['channelTitle'],
        'published_at': item['snippet']['publishedAt'],
        'category_id': item['snippet']['categoryId'],
        'view_count': int(item['statistics'].get('viewCount', 0)),
        'like_count': int(item['statistics'].get('likeCount', 0)),
        'comment_count': int(item['statistics'].get('commentCount', 0))
    }
    video_data.append(video_info)

df = pd.DataFrame(video_data)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

filename = f"trending_videos_{REGION}_{timestamp}.csv"
df.to_csv(f"dataset/{filename}", index=False)

print(f"Data saved to {filename}")

