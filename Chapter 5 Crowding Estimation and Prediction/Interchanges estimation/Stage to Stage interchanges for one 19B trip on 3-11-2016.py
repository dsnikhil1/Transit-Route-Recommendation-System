#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt


# In[3]:


all_stages_19B_dataframe = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Chapter 5 Crowding Estimation and Prediction/Interchanges estimation/19B_Kelambakkam_T.Nagar_3_11 stages list_Adyar depo (ordered).csv")


# In[8]:


all_stages = np.array(all_stages_19B_dataframe['Stage_name'])


# In[9]:


names = [_ for _ in all_stages]


# In[10]:


df = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/ETM each day all trips superset/ETM ticketing_3_11.csv")
df_source = df[df['Source']=='KELAMBAKKA']
df_source_destination = df_source[df_source['Destination']=='T.NAGAR   ']


# In[11]:


df_source_destination_trip = df_source_destination[df_source_destination['TripNo']==1]


# In[12]:


s = np.shape(all_stages)[0]
necss_mat = np.empty((s,s))
for i in range(np.shape(all_stages)[0]):
    for j in range(np.shape(all_stages)[0]):
        from_stage = all_stages[i]
        to_stage = all_stages[j]
        df_necessary = df_source_destination_trip[(df_source_destination_trip['FromStage']==from_stage) & 
                                                  (df_source_destination_trip['ToStage']==to_stage)]
        adult_sum = df_necessary['Adult'].sum()
        child_sum = df_necessary['Child'].sum()
        total_sum = adult_sum + child_sum
        necss_mat[i][j] = total_sum


# In[13]:


final_df = pd.DataFrame(necss_mat,index=names,columns=names)


# In[14]:


final_df


# In[15]:


final_df['number_of_boardings'] = final_df.sum(axis=0)
col_list = list(final_df)
col_list.remove('number_of_boardings')
final_df['number_of_alightings'] = final_df[col_list].sum(axis=1)


# In[16]:


final_df.to_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Chapter 5 Crowding Estimation and Prediction/Interchanges estimation/19B_Kelambakkam_T.Nagar_3_11_one_trip_stage to stage interchanges.csv",index=False)

