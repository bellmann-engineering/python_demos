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


# In[38]:


mask = (df['date'] >= '2017-01-01') & (df['date'] <= '2017-12-31')


# In[40]:


df_2017 = df[mask]


# In[42]:


highest = df_2017['close'].max()


# In[43]:


df[df['close'] == highest]


# In[45]:


df


# In[46]:


df['comment'] = 'abc'


# In[47]:


df


# In[48]:


df.drop('comment', axis=1, inplace=True) # 1 means column, 0 means row


# In[49]:


df


# In[50]:


df['year'] = df['date'].dt.year


# In[51]:


df


# In[54]:


df_2017= df[df['year'] == 2017]


# In[55]:


df_2017['close'].max()


# In[58]:


max_value = df_2017['close'].max()


# In[59]:


df_2017[df['close'] == max_value]


# In[ ]:





# In[ ]:




