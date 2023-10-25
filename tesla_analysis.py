#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df = pd.read_csv('tesla-stock-price.csv', parse_dates=['date'])


# In[8]:


df


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df.dtypes


# In[16]:


start_date = '2018-07-15'
end_date = '2018-07-31'

mask = (df['date'] >= start_date) & (df['date'] <= end_date)


# In[17]:


july_data_df = df[mask]


# In[18]:


july_data_df


# In[24]:


df[df['close'] < 150]


# In[28]:


bad_days = df.loc[df['close'] < 150, ['date', 'close']]


# In[29]:


bad_days


# In[30]:


bad_days.sort_values(by='date')


# In[31]:


bad_days.sort_values(by='date', ascending=False)


# In[ ]:




