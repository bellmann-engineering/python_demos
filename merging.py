#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[20]:


data1 = {'PersonID': [1,2,3,4,5],
         'Name': ['Alice', 'Bob', 'Marie', 'David', 'Kai'],
         'CityID': [101, 102, 101, 103, 99]
        }

data2 = {'CityID': [100, 101, 102, 103, 99],
         'CityName': ['London', 'Frankfurt', 'Stuttgart', 'Berlin', 'Nürnberg']
        }


# In[21]:


persons = pd.DataFrame(data1)


# In[22]:


cities = pd.DataFrame(data2)


# In[24]:


merged = pd.merge(persons, cities, on='CityID', how='left')


# In[30]:


cols = ['Name', 'CityName']
merged[cols]


# In[ ]:




