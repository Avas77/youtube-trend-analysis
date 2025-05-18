#!/usr/bin/env python
# coding: utf-8

# In[7]:


from sqlalchemy import create_engine
import pandas as pd
from postgres_setup import get_engine

# In[8]:


engine = get_engine()


# In[11]:


df = pd.read_sql('select * from trending_videos', engine)


# In[12]:


df.head()


# In[15]:


df.drop_duplicates(subset=['video_id'], inplace=True)


# In[16]:


df['published_at'] = pd.to_datetime(df['published_at'])


# In[17]:


df['published_at']


# In[20]:


df['video_age_days'] = (pd.Timestamp.now(tz='UTC') - df['published_at']).dt.days


# In[30]:


df['engagement_percent'] = ((df['comment_count'] + df['like_count']) / df['view_count']) * 100


# In[32]:


df['engagement_percent'] = df['engagement_percent'].round(2)


# In[33]:


df.nlargest(10, 'view_count')[['title', 'view_count']]


# In[34]:


df.nlargest(10, 'engagement_percent')[['title', 'engagement_percent']]


# In[35]:


df.to_sql('trending_videos_cleaned', con=engine, if_exists='replace', index=False)


# In[ ]:




