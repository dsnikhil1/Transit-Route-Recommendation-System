#!/usr/bin/env python
# coding: utf-8

# In[2]:


#only ady #and #spd #tvm depos have 19B 


# In[3]:


import numpy as np
import pandas as pd


# In[4]:


df = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/ETM Data_Selected/031116/ADY_031116.csv")
#route name extraction from Schedule name
df2 = df[df['Schedule_Name'].str.match('19B')]
ady_schedule = np.array(df2['Schedule_Name'].unique())
source_array = np.array(df2[df2['Schedule_Name']==ady_schedule[0]]['Source'].unique())
schedule_array = np.array(df2['Schedule_Name'].unique())
a = df['Depot_Name'].unique()[0]
Depo_name = []
Schedule_name = []
Source = []
Destination = []
for s in schedule_array:
      for t in source_array:
            dest_array = np.array(df2[(df2['Schedule_Name']==s) & (df2['Source']==t)]['Destination'].unique())
            for d in dest_array:
                Destination.append(d)
                Source.append(t)
                Schedule_name.append(s)
                Depo_name.append(a)
Depo_name = np.array(Depo_name)
Schedule_name = np.array(Schedule_name)
Source = np.array(Source)
Destination = np.array(Destination)
d = {'Depo_name': Depo_name,'Schedule_name':Schedule_name,'Source':Source,'Destination':Destination}
final_df = pd.DataFrame(data=d)
df_ady = final_df
df_ady_2 = df_ady.drop_duplicates(['Source','Destination'])


# In[5]:


df = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/ETM Data_Selected/031116/AND_031116.csv")
df2 = df[df['Schedule_Name'].str.match('19B')]
ady_schedule = np.array(df2['Schedule_Name'].unique())
source_array = np.array(df2[df2['Schedule_Name']==ady_schedule[0]]['Source'].unique())
schedule_array = np.array(df2['Schedule_Name'].unique())
a = df['Depot_Name'].unique()[0]
Depo_name = []
Schedule_name = []
Source = []
Destination = []
for s in schedule_array:
      for t in source_array:
            dest_array = np.array(df2[(df2['Schedule_Name']==s) & (df2['Source']==t)]['Destination'].unique())
            for d in dest_array:
                Destination.append(d)
                Source.append(t)
                Schedule_name.append(s)
                Depo_name.append(a)
Depo_name = np.array(Depo_name)
Schedule_name = np.array(Schedule_name)
Source = np.array(Source)
Destination = np.array(Destination)
d = {'Depo_name': Depo_name,'Schedule_name':Schedule_name,'Source':Source,'Destination':Destination}
final_df = pd.DataFrame(data=d)
df_and = final_df
df_and_2 = df_and.drop_duplicates(['Source','Destination'])


# In[6]:


df = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/ETM Data_Selected/031116/SPD_031116.csv")
df2 = df[df['Schedule_Name'].str.match('19B')]
ady_schedule = np.array(df2['Schedule_Name'].unique())
source_array = np.array(df2[df2['Schedule_Name']==ady_schedule[0]]['Source'].unique())
schedule_array = np.array(df2['Schedule_Name'].unique())
a = df['Depot_Name'].unique()[0]
Depo_name = []
Schedule_name = []
Source = []
Destination = []
for s in schedule_array:
      for t in source_array:
            dest_array = np.array(df2[(df2['Schedule_Name']==s) & (df2['Source']==t)]['Destination'].unique())
            for d in dest_array:
                Destination.append(d)
                Source.append(t)
                Schedule_name.append(s)
                Depo_name.append(a)
Depo_name = np.array(Depo_name)
Schedule_name = np.array(Schedule_name)
Source = np.array(Source)
Destination = np.array(Destination)
d = {'Depo_name': Depo_name,'Schedule_name':Schedule_name,'Source':Source,'Destination':Destination}
final_df = pd.DataFrame(data=d)
df_spd = final_df
df_spd_2 = df_spd.drop_duplicates(['Source','Destination'])


# In[7]:


df = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/ETM Data_Selected/031116/TVM_031116.csv")
df2 = df[df['Schedule_Name'].str.match('19B')]
ady_schedule = np.array(df2['Schedule_Name'].unique())
source_array = np.array(df2[df2['Schedule_Name']==ady_schedule[0]]['Source'].unique())
schedule_array = np.array(df2['Schedule_Name'].unique())
a = df['Depot_Name'].unique()[0]
Depo_name = []
Schedule_name = []
Source = []
Destination = []
for s in schedule_array:
      for t in source_array:
            dest_array = np.array(df2[(df2['Schedule_Name']==s) & (df2['Source']==t)]['Destination'].unique())
            for d in dest_array:
                Destination.append(d)
                Source.append(t)
                Schedule_name.append(s)
                Depo_name.append(a)
Depo_name = np.array(Depo_name)
Schedule_name = np.array(Schedule_name)
Source = np.array(Source)
Destination = np.array(Destination)
d = {'Depo_name': Depo_name,'Schedule_name':Schedule_name,'Source':Source,'Destination':Destination}
final_df = pd.DataFrame(data=d)
df_tvm = final_df
df_tvm_2 = df_tvm.drop_duplicates(['Source','Destination'])


# In[8]:


df_a = df_ady.append(df_and,ignore_index=True)
df_b = df_a.append(df_spd,ignore_index=True)
df_c = df_b.append(df_tvm,ignore_index=True)


# In[9]:


#df_c.to_csv('19B_all_trips_sources_destinations_3_11.csv',index=False)
#to include repeated schedules


# In[10]:


df_a = df_ady_2.append(df_and_2,ignore_index=True)
df_b = df_a.append(df_spd_2,ignore_index=True)
df_c = df_b.append(df_tvm_2,ignore_index=True)


# In[13]:


#only unique source destination pairs
df_c.to_csv('C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Chapter 4 Extraction/Source Destination Segregation all 19B trips 3-11-2016/19B_all_trips_sources_destinations_unique_3_11.csv',index=False)


# In[ ]:




