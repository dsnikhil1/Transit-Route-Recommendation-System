#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from numpy import *


# In[2]:


from datetime import datetime

def convert(fraction):
    hr = int(fraction * 24)
    mi = int((float(fraction * 24) - hr) * 60)
    sec = int((((float(fraction * 24) - hr) * 60) - mi) * 60)
    year = datetime.now().year  # replace with required year
    month = datetime.now().month  # replace with required month
    day = datetime.now().day  # replace with required day
    return datetime(year, month, day, hr, mi, sec)

#date_time = convert(1/8)
#print(type(date_time))
#print(date_time)


# In[3]:


df_headers = pd.read_excel('C:/Users/DSNikhil/Downloads/Codes and Corresponding files/RouteWise_20052019/headers_May2019.xlsx',header=None)
df_headers[30] = 'Route'
df_headers[31] = 'Service_type'


# In[4]:


df_route_tickets = pd.read_csv('C:/Users/DSNikhil/Downloads/Codes and Corresponding files/RouteWise_20052019/19B.csv',header=None)
df_tickets_data = pd.DataFrame()
df_tickets_data = df_tickets_data.append(df_headers)
df_tickets_data = df_tickets_data.append(df_route_tickets)
df_tickets_data = df_tickets_data.rename(columns = df_tickets_data.iloc[0])
df_tickets_data = df_tickets_data.iloc[1:]


# In[5]:


df_tickets_data['TicketIssuedTime'] = pd.to_numeric(df_tickets_data['TicketIssuedTime'])
df_tickets_data['TripStartTime'] = pd.to_numeric(df_tickets_data['TripStartTime'])


# In[6]:


all_stages_route_dataframe = pd.read_excel('C:/Users/DSNikhil/Downloads/Codes and Corresponding files/RouteWise_20052019/stageList.xlsx')
all_stages_route_initial = np.array(all_stages_route_dataframe['19B'])
all_stages_route = [x for x in all_stages_route_initial if str(x)!= 'nan']
#all_stages_route


# In[7]:


trip_start_time = []
ticket_issued_time = []
for i in range(np.shape(df_tickets_data)[0]):
    a = convert(df_tickets_data['TripStartTime'][i])
    #a = a.replace(" ","")
    trip_start_time.append(a)
    b = convert(df_tickets_data['TicketIssuedTime'][i])
    #b = b.replace(" ","")
    ticket_issued_time.append(b)
trip_start_time = np.array(trip_start_time)
ticket_issued_time = np.array(ticket_issued_time)
df_tickets_data['TripStartTime'] = trip_start_time
df_tickets_data['TicketIssuedTime'] = ticket_issued_time


# In[8]:


#final_df['Fleet_ID'] = final_df['Fleet_ID'].replace(" ","")
df_tickets_data['TicketIssuedTime'] = pd.to_datetime(df_tickets_data['TicketIssuedTime'])
df_tickets_data['TripStartTime'] = pd.to_datetime(df_tickets_data['TripStartTime'])


# In[9]:


DF = pd.DataFrame()
source_array = np.unique(df_tickets_data['Source'])
for source in source_array:
    df_tickets_data_source = df_tickets_data[df_tickets_data['Source']==source]
    df_tickets_data_source = df_tickets_data_source.reset_index(drop=True)
    destination_array = np.unique(df_tickets_data_source['Destination'])
    for destination in destination_array:
        df_tickets_data_source_destination = df_tickets_data_source[df_tickets_data_source['Destination']==destination]
        df_tickets_data_source_destination = df_tickets_data_source_destination.reset_index(drop=True)
        schedule_array = np.unique(df_tickets_data_source_destination['Schedule_Name'])
        for schedule in schedule_array:
            df_tickets_data_source_destination_schedule = df_tickets_data_source_destination[df_tickets_data_source_destination['Schedule_Name']==schedule]
            df_tickets_data_source_destination_schedule = df_tickets_data_source_destination_schedule.reset_index(drop=True)
            trips_array = np.unique(df_tickets_data_source_destination_schedule['TripNo'])
            for trip in trips_array:
                df_tickets_data_source_destination_schedule_trip = df_tickets_data_source_destination_schedule[df_tickets_data_source_destination_schedule['TripNo']==trip]
                df_tickets_data_source_destination_schedule_trip = df_tickets_data_source_destination_schedule_trip.reset_index(drop=True)
                source_stage = source
                destination_stage = destination
                a = source_stage in all_stages_route
                b = destination_stage in all_stages_route
                if a == True and b == True:
                    source_index = all_stages_route.index(source)
                    destination_index = all_stages_route.index(destination)                
                    if source_index < destination_index:
                        first_ticket_array = []        
                        s = np.shape(all_stages_route)[0]
                        necss_mat = np.empty((s,s))
                        for i in range(np.shape(all_stages_route)[0]):
                            df_tickets_data_source_destination_schedule_trip_stage_i = df_tickets_data_source_destination_schedule_trip[df_tickets_data_source_destination_schedule_trip['FromStage']==all_stages_route[i]]
                            first_ticket = df_tickets_data_source_destination_schedule_trip_stage_i['TicketIssuedTime'].min()
                            first_ticket_array.append(first_ticket)
                            for j in range(np.shape(all_stages_route)[0]):
                                if i == j:
                                    necss_mat[i][j] = 0
                                elif i > j:
                                    necss_mat[i][j] = -1
                                elif i < j:
                                    df_tickets_data_source_destination_schedule_trip_stage_i = df_tickets_data_source_destination_schedule_trip[df_tickets_data_source_destination_schedule_trip['FromStage']==all_stages_route[i]]
                                    stage_i_size = np.shape(df_tickets_data_source_destination_schedule_trip_stage_i)[0]
                                    df_tickets_data_source_destination_schedule_trip_stage_i = df_tickets_data_source_destination_schedule_trip_stage_i.reset_index(drop=True)
                                    df_tickets_data_source_destination_schedule_trip_stage_i['TicketIssuedTime'] = pd.to_datetime(df_tickets_data_source_destination_schedule_trip_stage_i['TicketIssuedTime'])
                                    df_tickets_data_source_destination_schedule_trip_stage_j = df_tickets_data_source_destination_schedule_trip[df_tickets_data_source_destination_schedule_trip['FromStage']==all_stages_route[j]]
                                    stage_j_size = np.shape(df_tickets_data_source_destination_schedule_trip_stage_j)[0]
                                    df_tickets_data_source_destination_schedule_trip_stage_j = df_tickets_data_source_destination_schedule_trip_stage_j.reset_index(drop=True)
                                    df_tickets_data_source_destination_schedule_trip_stage_j['TicketIssuedTime'] = pd.to_datetime(df_tickets_data_source_destination_schedule_trip_stage_j['TicketIssuedTime'])
                                    if stage_i_size > 0 and stage_j_size > 0:
                                        first_ticket_stage_i = df_tickets_data_source_destination_schedule_trip_stage_i['TicketIssuedTime'].min()
                                        first_ticket_stage_j = df_tickets_data_source_destination_schedule_trip_stage_j['TicketIssuedTime'].min()
                                        travel_time_i_j = first_ticket_stage_j-first_ticket_stage_i
                                        travel_time_i_j_minutes = travel_time_i_j.total_seconds() / 60
                                        necss_mat[i][j] = travel_time_i_j_minutes
                                    else:
                                        necss_mat[i][j] = -2
                        names = [_ for _ in all_stages_route]
                        final_df = pd.DataFrame(necss_mat,index=names,columns=names)
                        final_df['TripStartDate'] = df_tickets_data_source_destination_schedule_trip['TripStartDate'][0]
                        final_df['Depot'] = df_tickets_data_source_destination_schedule_trip['Depot'][0]
                        final_df['Source'] = source
                        final_df['Destination'] = destination
                        final_df['Direction'] = 'UP'
                        final_df['Schedule_Name'] = df_tickets_data_source_destination_schedule_trip['Schedule_Name'][0]
                        final_df['Route'] = df_tickets_data_source_destination_schedule_trip['Route'][0]
                        final_df['Service_type'] = df_tickets_data_source_destination_schedule_trip['Service_type'][0]
                        final_df['ETMNO'] = df_tickets_data_source_destination_schedule_trip['ETMNO'][0]
                        final_df['FLEETNO'] = df_tickets_data_source_destination_schedule_trip['FLEETNO'][0]
                        final_df['TripNo'] = df_tickets_data_source_destination_schedule_trip['TripNo'][0]
                        final_df['TripStartTime'] = df_tickets_data_source_destination_schedule_trip['TripStartTime'][0]
                        final_df['TripEndTime'] = df_tickets_data_source_destination_schedule_trip['TripEndTime'][0]
                        first_ticket_array = np.array(first_ticket_array)
                        final_df['First_Ticket_Stage'] = first_ticket_array
                        DF = DF.append(final_df)
                    elif source_index > destination_index:
                        first_ticket_array = []        
                        s = np.shape(all_stages_route)[0]
                        necss_mat = np.empty((s,s))
                        for i in range(np.shape(all_stages_route)[0]):
                            df_tickets_data_source_destination_schedule_trip_stage_i = df_tickets_data_source_destination_schedule_trip[df_tickets_data_source_destination_schedule_trip['FromStage']==all_stages_route[i]]
                            first_ticket = df_tickets_data_source_destination_schedule_trip_stage_i['TicketIssuedTime'].min()
                            first_ticket_array.append(first_ticket)
                            for j in range(np.shape(all_stages_route)[0]):
                                if i == j:
                                    necss_mat[i][j] = 0
                                elif i < j:
                                    necss_mat[i][j] = -1
                                elif i > j:
                                    df_tickets_data_source_destination_schedule_trip_stage_i = df_tickets_data_source_destination_schedule_trip[df_tickets_data_source_destination_schedule_trip['FromStage']==all_stages_route[i]]
                                    stage_i_size = np.shape(df_tickets_data_source_destination_schedule_trip_stage_i)[0]
                                    df_tickets_data_source_destination_schedule_trip_stage_i = df_tickets_data_source_destination_schedule_trip_stage_i.reset_index(drop=True)
                                    df_tickets_data_source_destination_schedule_trip_stage_i['TicketIssuedTime'] = pd.to_datetime(df_tickets_data_source_destination_schedule_trip_stage_i['TicketIssuedTime'])
                                    df_tickets_data_source_destination_schedule_trip_stage_j = df_tickets_data_source_destination_schedule_trip[df_tickets_data_source_destination_schedule_trip['FromStage']==all_stages_route[j]]
                                    stage_j_size = np.shape(df_tickets_data_source_destination_schedule_trip_stage_j)[0]
                                    df_tickets_data_source_destination_schedule_trip_stage_j = df_tickets_data_source_destination_schedule_trip_stage_j.reset_index(drop=True)
                                    df_tickets_data_source_destination_schedule_trip_stage_j['TicketIssuedTime'] = pd.to_datetime(df_tickets_data_source_destination_schedule_trip_stage_j['TicketIssuedTime'])
                                    if stage_i_size > 0 and stage_j_size > 0:
                                        first_ticket_stage_i = df_tickets_data_source_destination_schedule_trip_stage_i['TicketIssuedTime'].min()
                                        first_ticket_stage_j = df_tickets_data_source_destination_schedule_trip_stage_j['TicketIssuedTime'].min()
                                        travel_time_i_j = first_ticket_stage_j-first_ticket_stage_i
                                        travel_time_i_j_minutes = travel_time_i_j.total_seconds() / 60
                                        necss_mat[i][j] = travel_time_i_j_minutes
                                    else:
                                        necss_mat[i][j] = -2
                        names = [_ for _ in all_stages_route]
                        final_df = pd.DataFrame(necss_mat,index=names,columns=names)
                        final_df['TripStartDate'] = df_tickets_data_source_destination_schedule_trip['TripStartDate'][0]
                        final_df['Depot'] = df_tickets_data_source_destination_schedule_trip['Depot'][0]
                        final_df['Source'] = source
                        final_df['Destination'] = destination
                        final_df['Direction'] = 'DOWN'
                        final_df['Schedule_Name'] = df_tickets_data_source_destination_schedule_trip['Schedule_Name'][0]
                        final_df['Route'] = df_tickets_data_source_destination_schedule_trip['Route'][0]
                        final_df['Service_type'] = df_tickets_data_source_destination_schedule_trip['Service_type'][0]
                        final_df['ETMNO'] = df_tickets_data_source_destination_schedule_trip['ETMNO'][0]
                        final_df['FLEETNO'] = df_tickets_data_source_destination_schedule_trip['FLEETNO'][0]
                        final_df['TripNo'] = df_tickets_data_source_destination_schedule_trip['TripNo'][0]
                        final_df['TripStartTime'] = df_tickets_data_source_destination_schedule_trip['TripStartTime'][0]
                        final_df['TripEndTime'] = df_tickets_data_source_destination_schedule_trip['TripEndTime'][0]
                        first_ticket_array = np.array(first_ticket_array)
                        final_df['First_Ticket_Stage'] = first_ticket_array
                        DF = DF.append(final_df)


# In[11]:


DF.to_csv('Stage to Stage approximate travel time estimates for 19B on 20-05-2019.csv')


# In[ ]:




