#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


#Historical:'01-05-2019' '02-05-2019' '04-05-2019' '05-05-2019' '06-05-2019' '07-05-2019' '09-05-2019'
#Training:'10-05-2019' '11-05-2019' '12-05-2019' '13-05-2019' '14-05-2019' '15-05-2019' '16-05-2019'
#Testing:'17-05-2019' '18-05-2019' '19-05-2019' '21-05-2019' '23-05-2019' '24-05-2019' '26-05-2019'


# In[3]:


df = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Chapter 5 Crowding Estimation and Prediction/Crowding Prediction/Training Data/19B Saidapet Kelambakkam interchanges all days all trips.csv")


# In[4]:


#day1


# In[5]:


df_day = df[df['Date']=='01-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
#df_day_trip


# In[6]:


df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]


# In[7]:


b = []
a = []
t = []
#date = []
#Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
            #date.append(df_trip['Date'][0])
            #Tripstarttime.append(df_trip['TripStartTime'][0])


# In[8]:


b = np.array(b)
a = np.array(a)
t = np.array(t)
#date = np.array(date)
#Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'T1':t}#,'date':date,#'Tripstarttime':Tripstarttime#
df_his1 = pd.DataFrame(data=d)


# In[9]:


df_his1['T1'].sum()


# In[10]:


#day2


# In[11]:


df_day = df[df['Date']=='02-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
#date = []
#Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
b = np.array(b)
a = np.array(a)
t = np.array(t)
#date = np.array(date)
#Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'T2':t}#,'date':date,#'Tripstarttime':Tripstarttime#
df_his2 = pd.DataFrame(data=d)
df_his2['T2'].sum()


# In[12]:


#Day3


# In[13]:


df_day = df[df['Date']=='04-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
#date = []
#Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
b = np.array(b)
a = np.array(a)
t = np.array(t)
#date = np.array(date)
#Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'T3':t}#,'date':date,#'Tripstarttime':Tripstarttime#
df_his3 = pd.DataFrame(data=d)
df_his3['T3'].sum()


# In[14]:


#Day4


# In[15]:


df_day = df[df['Date']=='05-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
#date = []
#Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
b = np.array(b)
a = np.array(a)
t = np.array(t)
#date = np.array(date)
#Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'T4':t}#,'date':date,#'Tripstarttime':Tripstarttime#
df_his4 = pd.DataFrame(data=d)
df_his4['T4'].sum()


# In[16]:


#Day5


# In[17]:


df_day = df[df['Date']=='06-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
#date = []
#Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
b = np.array(b)
a = np.array(a)
t = np.array(t)
#date = np.array(date)
#Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'T5':t}#,'date':date,#'Tripstarttime':Tripstarttime#
df_his5 = pd.DataFrame(data=d)
df_his5['T5'].sum()


# In[18]:


#Day6


# In[19]:


df_day = df[df['Date']=='07-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
#date = []
#Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
b = np.array(b)
a = np.array(a)
t = np.array(t)
#date = np.array(date)
#Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'T6':t}#,'date':date,#'Tripstarttime':Tripstarttime#
df_his6 = pd.DataFrame(data=d)
df_his6['T6'].sum()


# In[20]:


#Day7


# In[21]:


df_day = df[df['Date']=='09-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
#date = []
#Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
b = np.array(b)
a = np.array(a)
t = np.array(t)
#date = np.array(date)
#Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'T7':t}#,'date':date,#'Tripstarttime':Tripstarttime#
df_his7 = pd.DataFrame(data=d)
df_his7['T7'].sum()


# In[22]:


df_new = pd.merge(df_his1, df_his2, how='left', left_on = ['B','A'], right_on = ['B','A'])
df_new_1 = pd.merge(df_new, df_his3, how='left', left_on = ['B','A'], right_on = ['B','A'])
df_new_2 = pd.merge(df_new_1, df_his4, how='left', left_on = ['B','A'], right_on = ['B','A'])
df_new_3 = pd.merge(df_new_2, df_his5, how='left', left_on = ['B','A'], right_on = ['B','A'])
df_new_4 = pd.merge(df_new_3, df_his6, how='left', left_on = ['B','A'], right_on = ['B','A'])
df_historical = pd.merge(df_new_4, df_his7, how='left', left_on = ['B','A'], right_on = ['B','A'])


# In[23]:


#Day8
#Training:'10-05-2019' '11-05-2019' '12-05-2019' '13-05-2019' '14-05-2019' '15-05-2019' '16-05-2019'
#Training data creation
DF = pd.DataFrame()


# In[24]:


df_day = df[df['Date']=='10-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
date = []
Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
            date.append(df_day_trip['Date'][0])
            Tripstarttime.append(df_day_trip['TripStartTime'][0])
b = np.array(b)
a = np.array(a)
t = np.array(t)
date = np.array(date)
Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'Td':t,'date':date,'Tripstarttime':Tripstarttime}
df_trd = pd.DataFrame(data=d)
print(df_trd['Td'].sum())
df_d = pd.merge(df_trd, df_historical, how='left', left_on = ['B','A'], right_on = ['B','A'])
DF = DF.append(df_d)


# In[25]:


#Day9


# In[26]:


df_day = df[df['Date']=='11-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
date = []
Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
            date.append(df_day_trip['Date'][0])
            Tripstarttime.append(df_day_trip['TripStartTime'][0])
b = np.array(b)
a = np.array(a)
t = np.array(t)
date = np.array(date)
Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'Td':t,'date':date,'Tripstarttime':Tripstarttime}
df_trd = pd.DataFrame(data=d)
print(df_trd['Td'].sum())
df_d = pd.merge(df_trd, df_historical, how='left', left_on = ['B','A'], right_on = ['B','A'])
DF = DF.append(df_d)


# In[27]:


#Day10


# In[28]:


df_day = df[df['Date']=='12-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
date = []
Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
            date.append(df_day_trip['Date'][0])
            Tripstarttime.append(df_day_trip['TripStartTime'][0])
b = np.array(b)
a = np.array(a)
t = np.array(t)
date = np.array(date)
Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'Td':t,'date':date,'Tripstarttime':Tripstarttime}
df_trd = pd.DataFrame(data=d)
print(df_trd['Td'].sum())
df_d = pd.merge(df_trd, df_historical, how='left', left_on = ['B','A'], right_on = ['B','A'])
DF = DF.append(df_d)


# In[29]:


#Day11


# In[30]:


df_day = df[df['Date']=='13-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
date = []
Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
            date.append(df_day_trip['Date'][0])
            Tripstarttime.append(df_day_trip['TripStartTime'][0])
b = np.array(b)
a = np.array(a)
t = np.array(t)
date = np.array(date)
Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'Td':t,'date':date,'Tripstarttime':Tripstarttime}
df_trd = pd.DataFrame(data=d)
print(df_trd['Td'].sum())
df_d = pd.merge(df_trd, df_historical, how='left', left_on = ['B','A'], right_on = ['B','A'])
DF = DF.append(df_d)


# In[31]:


#Day12


# In[32]:


df_day = df[df['Date']=='14-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
date = []
Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
            date.append(df_day_trip['Date'][0])
            Tripstarttime.append(df_day_trip['TripStartTime'][0])
b = np.array(b)
a = np.array(a)
t = np.array(t)
date = np.array(date)
Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'Td':t,'date':date,'Tripstarttime':Tripstarttime}
df_trd = pd.DataFrame(data=d)
print(df_trd['Td'].sum())
df_d = pd.merge(df_trd, df_historical, how='left', left_on = ['B','A'], right_on = ['B','A'])
DF = DF.append(df_d)


# In[33]:


#Day13


# In[34]:


df_day = df[df['Date']=='15-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
date = []
Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
            date.append(df_day_trip['Date'][0])
            Tripstarttime.append(df_day_trip['TripStartTime'][0])
b = np.array(b)
a = np.array(a)
t = np.array(t)
date = np.array(date)
Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'Td':t,'date':date,'Tripstarttime':Tripstarttime}
df_trd = pd.DataFrame(data=d)
print(df_trd['Td'].sum())
df_d = pd.merge(df_trd, df_historical, how='left', left_on = ['B','A'], right_on = ['B','A'])
DF = DF.append(df_d)


# In[35]:


#Day14


# In[36]:


df_day = df[df['Date']=='16-05-2019']
df_day = df_day.reset_index(drop=True)
df_day_trips = df_day[(df_day['TripStartTime']>='17:00:00')&(df_day['TripStartTime']<'19:00:00')]
first = np.sort(df_day_trips['TripStartTime'].unique())[0]
df_day_trip = df_day_trips[df_day_trips['TripStartTime']==first]
df_day_trip = df_day_trip.reset_index(drop=True)
df_day_trip = df_day_trip.iloc[:,:44]
df_day_trip_matrix = df_day_trip.iloc[:,15:]
b = []
a = []
t = []
date = []
Tripstarttime = []
for i in range(29):
    for j in range(29):
        if j > i:
            t.append(df_day_trip_matrix.iloc[i,j])
            b.append('S'+str(i+1))
            a.append('S'+str(j+1))
            date.append(df_day_trip['Date'][0])
            Tripstarttime.append(df_day_trip['TripStartTime'][0])
b = np.array(b)
a = np.array(a)
t = np.array(t)
date = np.array(date)
Tripstarttime = np.array(Tripstarttime)
d = {'B':b,'A':a,'Td':t,'date':date,'Tripstarttime':Tripstarttime}
df_trd = pd.DataFrame(data=d)
print(df_trd['Td'].sum())
df_d = pd.merge(df_trd, df_historical, how='left', left_on = ['B','A'], right_on = ['B','A'])
DF = DF.append(df_d)


# In[37]:


DF = DF.reset_index(drop=True)


# In[38]:


B1 = []
B2 = []
B3 = []
B4 = []
B5 = []
B6 = []
B7 = []
B8 = []
B9 = []
B10 = []
B11 = []
B12 = []
B13 = []
B14 = []
B15 = []
B16 = []
B17 = []
B18 = []
B19 = []
B20 = []
B21 = []
B22 = []
B23 = []
B24 = []
B25 = []
B26 = []
B27 = []
B28 = []
B29 = []
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S1':
        B1.append(1)
    else:
        B1.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S2':
        B2.append(1)
    else:
        B2.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S3':
        B3.append(1)
    else:
        B3.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S4':
        B4.append(1)
    else:
        B4.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S5':
        B5.append(1)
    else:
        B5.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S7':
        B7.append(1)
    else:
        B7.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S6':
        B6.append(1)
    else:
        B6.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S8':
        B8.append(1)
    else:
        B8.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S9':
        B9.append(1)
    else:
        B9.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S10':
        B10.append(1)
    else:
        B10.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S11':
        B11.append(1)
    else:
        B11.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S12':
        B12.append(1)
    else:
        B12.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S13':
        B13.append(1)
    else:
        B13.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S15':
        B15.append(1)
    else:
        B15.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S14':
        B14.append(1)
    else:
        B14.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S16':
        B16.append(1)
    else:
        B16.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S17':
        B17.append(1)
    else:
        B17.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S18':
        B18.append(1)
    else:
        B18.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S19':
        B19.append(1)
    else:
        B19.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S20':
        B20.append(1)
    else:
        B20.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S21':
        B21.append(1)
    else:
        B21.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S22':
        B22.append(1)
    else:
        B22.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S23':
        B23.append(1)
    else:
        B23.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S24':
        B24.append(1)
    else:
        B24.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S25':
        B25.append(1)
    else:
        B25.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S26':
        B26.append(1)
    else:
        B26.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S27':
        B27.append(1)
    else:
        B27.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S28':
        B28.append(1)
    else:
        B28.append(0)
for i in range(np.shape(DF)[0]):
    if DF['B'][i] == 'S29':
        B29.append(1)
    else:
        B29.append(0)
B1 = np.array(B1)
B2 = np.array(B2)
B3 = np.array(B3)
B4 = np.array(B4)
B5 = np.array(B5)
B6 = np.array(B6)
B7 = np.array(B7)
B8 = np.array(B8)
B9 = np.array(B9)
B10 = np.array(B10)
B11 = np.array(B11)
B12 = np.array(B12)
B13 = np.array(B13)
B14 = np.array(B14)
B15 = np.array(B15)
B16 = np.array(B16)
B17 = np.array(B17)
B18 = np.array(B18)
B19 = np.array(B19)
B20 = np.array(B20)
B21 = np.array(B21)
B22 = np.array(B22)
B23 = np.array(B23)
B24 = np.array(B24)
B25 = np.array(B25)
B26 = np.array(B26)
B27 = np.array(B27)
B28 = np.array(B28)
B29 = np.array(B29)
DF['B1'] = B1
DF['B2'] = B2
DF['B3'] = B3
DF['B4'] = B4
DF['B5'] = B5
DF['B6'] = B6
DF['B7'] = B7
DF['B8'] = B8
DF['B9'] = B9
DF['B10'] = B10
DF['B11'] = B11
DF['B12'] = B12
DF['B13'] = B13
DF['B14'] = B14
DF['B15'] = B15
DF['B16'] = B16
DF['B17'] = B17
DF['B18'] = B18
DF['B19'] = B19
DF['B20'] = B20
DF['B21'] = B21
DF['B22'] = B22
DF['B23'] = B23
DF['B24'] = B24
DF['B25'] = B25
DF['B26'] = B26
DF['B27'] = B27
DF['B28'] = B28
DF['B29'] = B29


# In[39]:


A1 = []
A2 = []
A3 = []
A4 = []
A5 = []
A6 = []
A7 = []
A8 = []
A9 = []
A10 = []
A11 = []
A12 = []
A13 = []
A14 = []
A15 = []
A16 = []
A17 = []
A18 = []
A19 = []
A20 = []
A21 = []
A22 = []
A23 = []
A24 = []
A25 = []
A26 = []
A27 = []
A28 = []
A29 = []
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S1':
        A1.append(1)
    else:
        A1.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S2':
        A2.append(1)
    else:
        A2.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S3':
        A3.append(1)
    else:
        A3.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S4':
        A4.append(1)
    else:
        A4.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S5':
        A5.append(1)
    else:
        A5.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S7':
        A7.append(1)
    else:
        A7.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S6':
        A6.append(1)
    else:
        A6.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S8':
        A8.append(1)
    else:
        A8.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S9':
        A9.append(1)
    else:
        A9.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S10':
        A10.append(1)
    else:
        A10.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S11':
        A11.append(1)
    else:
        A11.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S12':
        A12.append(1)
    else:
        A12.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S13':
        A13.append(1)
    else:
        A13.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S15':
        A15.append(1)
    else:
        A15.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S14':
        A14.append(1)
    else:
        A14.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S16':
        A16.append(1)
    else:
        A16.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S17':
        A17.append(1)
    else:
        A17.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S18':
        A18.append(1)
    else:
        A18.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S19':
        A19.append(1)
    else:
        A19.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S20':
        A20.append(1)
    else:
        A20.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S21':
        A21.append(1)
    else:
        A21.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S22':
        A22.append(1)
    else:
        A22.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S23':
        A23.append(1)
    else:
        A23.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S24':
        A24.append(1)
    else:
        A24.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S25':
        A25.append(1)
    else:
        A25.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S26':
        A26.append(1)
    else:
        A26.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S27':
        A27.append(1)
    else:
        A27.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S28':
        A28.append(1)
    else:
        A28.append(0)
for i in range(np.shape(DF)[0]):
    if DF['A'][i] == 'S29':
        A29.append(1)
    else:
        A29.append(0)
A1 = np.array(A1)
A2 = np.array(A2)
A3 = np.array(A3)
A4 = np.array(A4)
A5 = np.array(A5)
A6 = np.array(A6)
A7 = np.array(A7)
A8 = np.array(A8)
A9 = np.array(A9)
A10 = np.array(A10)
A11 = np.array(A11)
A12 = np.array(A12)
A13 = np.array(A13)
A14 = np.array(A14)
A15 = np.array(A15)
A16 = np.array(A16)
A17 = np.array(A17)
A18 = np.array(A18)
A19 = np.array(A19)
A20 = np.array(A20)
A21 = np.array(A21)
A22 = np.array(A22)
A23 = np.array(A23)
A24 = np.array(A24)
A25 = np.array(A25)
A26 = np.array(A26)
A27 = np.array(A27)
A28 = np.array(A28)
A29 = np.array(A29)
DF['A1'] = A1
DF['A2'] = A2
DF['A3'] = A3
DF['A4'] = A4
DF['A5'] = A5
DF['A6'] = A6
DF['A7'] = A7
DF['A8'] = A8
DF['A9'] = A9
DF['A10'] = A10
DF['A11'] = A11
DF['A12'] = A12
DF['A13'] = A13
DF['A14'] = A14
DF['A15'] = A15
DF['A16'] = A16
DF['A17'] = A17
DF['A18'] = A18
DF['A19'] = A19
DF['A20'] = A20
DF['A21'] = A21
DF['A22'] = A22
DF['A23'] = A23
DF['A24'] = A24
DF['A25'] = A25
DF['A26'] = A26
DF['A27'] = A27
DF['A28'] = A28
DF['A29'] = A29


# In[40]:


Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []
Saturday = []
Sunday = []
for i in range(np.shape(DF)[0]):
    if DF['date'][i] == '10-05-2019':
        Friday.append(1)
    else:
        Friday.append(0)
for i in range(np.shape(DF)[0]):
    if DF['date'][i] == '11-05-2019':
        Saturday.append(1)
    else:
        Saturday.append(0)
for i in range(np.shape(DF)[0]):
    if DF['date'][i] == '12-05-2019':
        Sunday.append(1)
    else:
        Sunday.append(0)
for i in range(np.shape(DF)[0]):
    if DF['date'][i] == '13-05-2019':
        Monday.append(1)
    else:
        Monday.append(0)
for i in range(np.shape(DF)[0]):
    if DF['date'][i] == '14-05-2019':
        Tuesday.append(1)
    else:
        Tuesday.append(0)
for i in range(np.shape(DF)[0]):
    if DF['date'][i] == '15-05-2019':
        Wednesday.append(1)
    else:
        Wednesday.append(0)
for i in range(np.shape(DF)[0]):
    if DF['date'][i] == '16-05-2019':
        Thursday.append(1)
    else:
        Thursday.append(0)
Monday = np.array(Monday)
Tuesday = np.array(Tuesday)
Wednesday = np.array(Wednesday)
Thursday = np.array(Thursday)
Friday = np.array(Friday)
Saturday = np.array(Saturday)
Sunday = np.array(Sunday)
DF['Monday'] = Monday
DF['Tuesday'] = Tuesday
DF['Wednesday'] = Wednesday
DF['Thursday'] = Thursday
DF['Friday'] = Friday
DF['Saturday'] = Saturday
DF['Sunday'] = Sunday


# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:


DF.to_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Chapter 5 Crowding Estimation and Prediction/Crowding Prediction/Training Data/training data.csv",index=False)


# In[ ]:




