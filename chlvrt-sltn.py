#!/usr/bin/env python
# coding: utf-8

#Chilavert Project
# ------------------------
# Author: Joao Henrique B Gomes 
#
# #### Exploring the European Soccer Database: Can Goalkeepers take free kicks?


import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading the database:

# In[2]:


cnx = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)


# In[3]:


df.head()


# In[4]:


df = df.dropna()


# In[15]:


df.columns


# In[68]:


plt.scatter(df['id'][:10000],df['gk_diving'][:10000])
plt.axhline(y = 50, color = 'r', linestyle = '-')


# Creating mask to filter only the goalkeepers based on the attributes:
# - GK diving
# - GK handling
# - GK kicking
# - GK positioning
# - GK reflexes
# 
# Goalkeepers with bad attributes are also filtered out.

# In[59]:


div_mask = df['gk_diving'] > 50
han_mask = df['gk_handling'] > 50
kic_mask = df['gk_kicking'] > 50
pos_mask = df['gk_positioning'] > 50
ref_mask = df['gk_reflexes'] > 50


data = df[div_mask & han_mask & kic_mask & pos_mask & ref_mask].copy()


# In[60]:


data.shape


# In[69]:





# In[ ]:





# Relevant attributes for free kicks:  
# - Free kick accuracy  
# - Shot power
# 
# Creating a new attribute (free kick proficiency) to account for both power and accuracy in a weighted fashion:

# In[61]:


data['fk_proficiency'] = (3*data['free_kick_accuracy'] + 2*data['shot_power'])/5


# Creating a mask to find the proficient goalkeepers:

# In[63]:


gk_takers = data['fk_proficiency'] > 70

data[gk_takers]


# In[70]:


plt.scatter(data['id'][:10000], data['fk_proficiency'][:10000])
plt.axhline(y = 70, color = 'r', linestyle = '-')


# We found 7 goalkeepers who also could potentially take free kicks in matches. Through their FIFA player ID, these players can be identified.
# 
# According to fifaindex.com, these are the players we found:
# 
# | FIFA player ID | Player Name | Team | Overall | Game edition|
# |:--------------:|:-----------:|:----:|:-------:|:-----------:|
# |1219| Christian Abbiati | Torino FC (ITA) | 85 | FIFA 07 |
# |192593| Danijel Subašić | AS Monaco FC (FRA) | 71 | FIFA 13 |
# |3974| José Moreira | SL Benfica (POR) | 76 | FIFA 07 |
# |48717| Júlio César | Inter Milan (ITA) | 79 | FIFA 07|
# |49472| Ludovic Butelle | Valencia CF (SPA) | 75 | FIFA 07 |
# |111106| Sergio Aragoneses | Hércules CF (SPA) | 64 | FIFA 07 |
# |153297| Simon Pouplin | Stade Rennais FC (FRA) | 70 | FIFA 07 |

# In[ ]:




