#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import glob
import os


# In[24]:


path = 'C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Nov 2016 Consolidated/ETM_2016_11_Nov/11_Nov/081116'


# In[25]:


allcsvfiles = glob.glob(os.path.join(path, '*.csv'))
dataframes = []
for file in allcsvfiles:
    df = pd.read_csv(file)
    dataframes.append(df)
result = pd.concat(dataframes,ignore_index=True)
df = result


# In[26]:


Date = []
Depo_name = []
Schedule_name = []
Fleet_ID = []
Source = []
Destination = []
Trip_Start_Time = []
Trip_End_Time = []
First_Ticket_Time = []
Last_Ticket_Time = []
ETM_NO = []
depos = np.array(df['Depot_Name'].unique())
for depo in depos:
    df_depo = df[df['Depot_Name']==depo]
    schedules = np.array(df_depo['Schedule_Name'].unique())
    for schedule in schedules:
        df_depo_sch = df_depo[df_depo['Schedule_Name']==schedule] 
        trips = np.array(df_depo_sch['TripStartTime'].unique())
        for trip in trips:
            df_depo_sch_trip = df_depo_sch[df_depo_sch['TripStartTime']==trip]
            df_depo_sch_trip = df_depo_sch_trip.reset_index(drop=True)
            ETM_NO.append(df_depo_sch_trip['ETMNO'][0])
            Trip_Start_Time.append(df_depo_sch_trip['TripStartTime'][0])
            Trip_End_Time.append(df_depo_sch_trip['TripEndTime'][0])
            Date.append(df_depo_sch_trip['TripStartDate'][0])
            First_Ticket_Time.append(min(df_depo_sch_trip['TicketIssuedTime']))
            Last_Ticket_Time.append(max(df_depo_sch_trip['TicketIssuedTime']))
            Source.append(df_depo_sch_trip['Source'][0])
            Destination.append(df_depo_sch_trip['Destination'][0])
            Fleet_ID.append(df_depo_sch_trip['FLEETNO'][0])
            Schedule_name.append(df_depo_sch_trip['Schedule_Name'][0])
            Depo_name.append(df_depo_sch_trip['Depot_Name'][0])
Date = np.array(Date)
Depo_name = np.array(Depo_name)
Schedule_name = np.array(Schedule_name)
Fleet_ID = np.array(Fleet_ID)
Source = np.array(Source)
Destination = np.array(Destination)
Trip_Start_Time = np.array(Trip_Start_Time)
Trip_End_Time = np.array(Trip_End_Time)
First_Ticket_Time = np.array(First_Ticket_Time)
Last_Ticket_Time = np.array(Last_Ticket_Time)
ETM_NO = np.array(ETM_NO)
d = {'Date':Date, 'Depo_name':Depo_name, 'Schedule_name': Schedule_name, 'Fleet_ID':Fleet_ID, 'Source':Source,'Destination':Destination,
    'Trip_Start_Time':Trip_Start_Time, 'Trip_End_Time':Trip_End_Time, 'First_Ticket_Time':First_Ticket_Time,
    'Last_Ticket_Time':Last_Ticket_Time, 'ETM_NO':ETM_NO}
final_df = pd.DataFrame(data=d)


# In[27]:


final_df['Fleet_ID'].astype(str)
final_df['Fleet_ID'] = final_df['Fleet_ID'].replace(" ","")
df_mapping = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Nov 2016 Consolidated/KNP GLB ETM Mapping.csv")
df_mapping = df_mapping[df_mapping['FLEET ID'].notna()]
df_mapping = df_mapping.reset_index(drop=True)
df_mapping['FLEET ID'].astype(str)
df_mapping['FLEET ID'] = df_mapping['FLEET ID'].str[2:]
df_mapping_array = np.array(df_mapping['FLEET ID'])
df_mapping_array_2 = []
#for i in range(len(df_mapping)):
    #df_mapping['FLEET ID'][i] = df_mapping['FLEET ID'][i].replace(" ","")
for i in df_mapping_array:
    necss = i.replace(" ","")
    df_mapping_array_2.append(necss)
df_mapping_array_2 = np.array(df_mapping_array_2)
df_mapping = df_mapping.drop(['FLEET ID'], axis =1)
df_mapping['FLEET ID'] = df_mapping_array_2
Fleet_ID = np.array(df_mapping['FLEET ID'])
Depo_name = np.array(df_mapping['DEPOT'])
Route_number = np.array(df_mapping['ROUTE\nNO.'])
Device_number = np.array(df_mapping['DEVICE ID'])
d = {'Fleet_ID':Fleet_ID, 'Depo_name': Depo_name, 'Route_number':Route_number, 'Route_number':Route_number, 'Device_number':Device_number}
final_df_mapping = pd.DataFrame(data=d)


# In[28]:


df_map = final_df_mapping[final_df_mapping['Depo_name'].notna()]
df_map = df_map.reset_index(drop=True)


# In[29]:


new_df = pd.merge(final_df, df_map,  how='left', left_on=['Fleet_ID','Depo_name'], right_on = ['Fleet_ID','Depo_name'])
last_df = new_df[new_df['Device_number'].notna()]


# In[30]:


#last_df


# In[31]:


s = np.array(last_df['Schedule_name'].unique())
r = []
f = []
dev = []
for sch in s:
    r.append(last_df[last_df['Schedule_name']==sch]['Route_number'].unique()[0])
    f.append(last_df[last_df['Schedule_name']==sch]['Fleet_ID'].unique()[0])
    dev.append(last_df[last_df['Schedule_name']==sch]['Device_number'].unique()[0])
r = np.array(r)
f = np.array(f)
dev = np.array(dev)


# In[32]:


d = {'Schedule':s,'Fleet_ID':f,'Route':r,'Device_number':dev}
table = pd.DataFrame(data=d)
#table


# In[33]:


match = []
for i in range(len(table)):
    match.append(table['Route'][i] in table['Schedule'][i])
match = np.array(match)
table['match'] = match


# In[34]:


def get_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


# In[35]:


location = []
for i in range(len(table)):
    dev_num = table['Device_number'][i]
    #print(dev_num)
    dev_num = int(dev_num)
    dev_num = str(dev_num)
    str2 = '.csv'
    dev_name_1 = dev_num + str2
    path1 = 'C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Nov 2016 Consolidated/KNP_2016_11_Nov_1/2016-11-08'
    array_1 = get_all(dev_name_1,path1)
    str3 = '2016-11-08_'
    dev_name_2 = str3 + dev_name_1
    path2 = 'C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Nov 2016 Consolidated/KNP_2016_11_Nov_2/2016_11_Nov_2/2016-11-08'
    array_2 = get_all(dev_name_2,path2)
    if len(array_1) > 0:
        location.append('KNP_2016_11_Nov_1')
    elif len(array_2) > 0:
        location.append('KNP_2016_11_Nov_2')
    else: 
        location.append('File not found in KNP folders')
location = np.array(location)


# In[36]:


table['GPS file location'] = location


# In[37]:


table_1 = table[table['match']==True]
final_output_file = table_1[table_1['GPS file location']!='File not found in KNP folders']
final_output_file = final_output_file.reset_index(drop=True)
date = final_df['Date'][0]
final_output_file['Date'] = date


# In[38]:


final_output_file


# In[39]:


final_output_file.to_csv('ETM_GPS_exact matches_available files_08_11_2016.csv',index=False)


# In[ ]:




