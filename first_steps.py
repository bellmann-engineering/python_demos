#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = {'First Name': [], 'Last Name': [], 'Country': []}


# In[3]:


df = pd.DataFrame(data)


# In[4]:


kai_data = { 'First Name': 'Kai', 'Last Name': 'Bellmann', 'Country': 'Germany' }
df = pd.concat([df, pd.DataFrame( [kai_data] ) ])


# In[5]:


df


# In[6]:


people = [
    {'First Name': 'John', 'Last Name': 'Doe', 'Country': 'USA'},
    {'First Name': 'Emma', 'Last Name': 'Smith', 'Country': 'Canada'},
    {'First Name': 'Maria', 'Last Name': 'Garcia', 'Country': 'Spain'},
    {'First Name': 'Satoshi', 'Last Name': 'Nakamoto', 'Country': 'Japan'},
    {'First Name': 'Luis', 'Last Name': 'Fernandez', 'Country': 'Mexico'},
    {'First Name': 'Elena', 'Last Name': 'Ivanova', 'Country': 'Russia'},
    {'First Name': 'Lucas', 'Last Name': 'Müller', 'Country': 'Germany'},
    {'First Name': 'Isabella', 'Last Name': 'Chen', 'Country': 'China'},
    {'First Name': 'Alessandro', 'Last Name': 'Ricci', 'Country': 'Italy'}
]


# In[7]:


for person in people:
    df = pd.concat([df, pd.DataFrame( [person] ) ])


# In[8]:


df


# In[9]:


df['Country'] == 'Germany'


# In[10]:


df[df['Country'] == 'Germany']


# In[11]:


mask = df['Country'] == 'Germany'


# In[12]:


df[mask]


# In[13]:


df[df['First Name'] == 'Emma']


# In[18]:


mask = (df['First Name'] == 'Emma') & (df['Last Name'] == 'Smith')


# In[19]:


df[mask]


# In[20]:


df[(df['First Name'] == 'Emma') & (df['Last Name'] == 'Smith')]


# In[21]:


df[(df['First Name'] == 'Kai') | (df['First Name'] == 'Kay')]


# In[ ]:




