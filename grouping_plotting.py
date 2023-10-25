#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('tesla-stock-price.csv', parse_dates=['date'])


# In[5]:


df['year'] = df['date'].dt.year


# In[9]:


df.groupby('year')['close'].mean()


# In[10]:


import matplotlib.pyplot as plt


# In[11]:


yearly_avg_close = df.groupby('year')['close'].mean()


# In[14]:


yearly_avg_close.plot(kind='bar', title='close avg per year', xlabel='Year', ylabel='avg close price')
plt.show()


# In[16]:


df.plot(x='date', y='close', kind='line', title='TESLA', xlabel='Date', ylabel='close price')
plt.show()


# In[ ]:




