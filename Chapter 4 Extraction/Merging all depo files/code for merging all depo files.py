#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import glob
import os


# In[2]:


path = 'C:/Users/DSNikhil/Downloads/Codes and Corresponding files/ETM Data_Selected/031116'


# In[3]:


allcsvfiles = glob.glob(os.path.join(path, '*.csv'))
dataframes = []
for file in allcsvfiles:
    df = pd.read_csv(file)
    dataframes.append(df)
result = pd.concat(dataframes,ignore_index=True)


# In[4]:


result.to_csv('C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Chapter 4 Extraction/Merging all depo files/ETM ticketing_3_11.csv',index=False)

