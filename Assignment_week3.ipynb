#!/usr/bin/env python
# coding: utf-8

# #### Step 1: Loading Libraries

# In[12]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

print('Libraries imported.')


# ### Step 2: Loading data from Wikipedia

# In[13]:


request = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
Toronto  = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M',header=0)[0]
Toronto.rename(columns = {'Postcode':'PostalCode'},inplace=True)


# In[14]:


Toronto.set_index('Borough').drop('Not assigned').reset_index(inplace=True)


# #### Step 3: The dataframe will consist of three columns: PostalCode, Borough, and Neighborhood

# In[15]:


Toronto.head(20)


# #### Step 4: More than one neighborhood can exist in one postal code area. For example, in the table on the Wikipedia page, you will notice that M5A is listed twice and has two neighborhoods: Harbourfront and Regent Park. These two rows will be combined into one row with the neighborhoods separated with a comma as shown in row 11 in the above table.

# In[16]:


Toronto = Toronto.groupby(['PostalCode','Borough'])['Neighbourhood'].apply(', '.join).reset_index()


# #### Step 5: If a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough. So for the 9th cell in the table on the Wikipedia page, the value of the Borough and the Neighborhood columns will be Queen's Park.

# In[17]:


Toronto.loc[my_table['Neighbourhood']=='Not assigned','Neighbourhood'] = my_table.loc[my_table['Neighbourhood']=='Not assigned']['Borough']


# ##### Check the table to make sure Harbourfront and Regent Park are merged in M5A and Queen's Park is shown correctly at Neighbourhood.

# In[19]:


## Table checking
Toronto.loc[Toronto['PostalCode']=='M5A']


# In[20]:


Toronto.loc[Toronto['Neighbourhood']=="Queen's Park"]


# ##### Note: Clean your Notebook and add Markdown cells to explain your work and any assumptions you are making.

# ### In the last cell of your notebook, use the .shape method to print the number of rows of your dataframe.

# In[23]:


Toronto.shape


# In[ ]:




