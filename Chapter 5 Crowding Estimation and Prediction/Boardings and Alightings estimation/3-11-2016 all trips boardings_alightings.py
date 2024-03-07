#!/usr/bin/env python
# coding: utf-8
Assumptions:
For a schedule, origin and destination remains fixed, stage names are also fixed
For a schedule, all unique stages are collected from all the trips which gives the stage list for that schedule
# In[19]:


import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from numpy import *


# In[20]:


df = pd.read_csv("C:/Users/DSNikhil/Downloads/Codes and Corresponding files/ETM each day all trips superset/ETM ticketing_3_11.csv")


# In[21]:


DF = pd.DataFrame()
source_array = np.unique(df['Source'])
for source in source_array:
    df_source = df[df['Source']==source]
    df_source = df_source.reset_index(drop=True)
    destination_array = np.unique(df_source['Destination'])
    for destination in destination_array:
        df_source_destination = df_source[df_source['Destination']==destination]
        df_source_destination = df_source_destination.reset_index(drop=True)
        schedule_array = np.unique(df_source_destination['Schedule_Name'])
        for schedule in schedule_array:
            df_source_destination_schedule = df_source_destination[df_source_destination['Schedule_Name']==schedule]
            df_source_destination_schedule = df_source_destination_schedule.reset_index(drop=True)
            a1 = np.array(df_source_destination_schedule['FromStage'].unique())
            a2 = np.array(df_source_destination_schedule['ToStage'].unique())
            a3 = np.concatenate((a1,a2),axis=0)
            all_stages = np.array(np.unique(a3))
            trips_array = np.unique(df_source_destination_schedule['TripStartTime'])
            i = 0
            for trip in trips_array:
                df_source_destination_schedule_trip = df_source_destination_schedule[df_source_destination_schedule['TripStartTime']==trip]
                df_source_destination_schedule_trip = df_source_destination_schedule_trip.reset_index(drop=True)
                i = i + 1
                TripStartDate = []
                Depot = []
                Schedule = []
                Route = []
                ServiceType = []
                ETM_No = []
                Fleet_ID = []
                TripNo = []
                RunNo = []
                TripStartTime = []
                Source = []
                Destination = []
                Number_of_boardings = []
                Number_of_alightings = []
                Number_of_interchanges = []
                for stage in all_stages:
                    dest_array = np.array(df_source_destination_schedule_trip[df_source_destination_schedule_trip['FromStage']==stage]['ToStage'].unique())
                    Number_of_interchanges.append(np.shape(dest_array)[0])
                    trip_no = df_source_destination_schedule_trip['TripNo'][0]
                    TripNo.append(trip_no)
                    RunNo.append(i)
                    schedule_name = df_source_destination_schedule_trip['Schedule_Name'][0]
                    Schedule.append(schedule_name)
                    adult_sum = df_source_destination_schedule_trip[df_source_destination_schedule_trip['FromStage']==stage]['Adult'].sum()
                    child_sum = df_source_destination_schedule_trip[df_source_destination_schedule_trip['FromStage']==stage]['Child'].sum()
                    total_sum = adult_sum + child_sum
                    Number_of_boardings.append(total_sum)
                    adult_sum = df_source_destination_schedule_trip[df_source_destination_schedule_trip['ToStage']==stage]['Adult'].sum()
                    child_sum = df_source_destination_schedule_trip[df_source_destination_schedule_trip['ToStage']==stage]['Child'].sum()
                    total_sum = adult_sum + child_sum
                    Number_of_alightings.append(total_sum)
                    trip_start_time = df_source_destination_schedule_trip['TripStartTime'][0]
                    TripStartTime.append(trip_start_time)
                    fleet_id = df_source_destination_schedule_trip['FLEETNO'][0]
                    Fleet_ID.append(fleet_id)
                    etm_no = df_source_destination_schedule_trip['ETMNO'][0]
                    ETM_No.append(etm_no)
                    trip_start_date = df_source_destination_schedule_trip['TripStartDate'][0]
                    TripStartDate.append(trip_start_date)
                    depot = df_source_destination_schedule_trip['Depot_Name'][0]
                    Depot.append(depot)
                    source = df_source_destination_schedule_trip['Source'][0]
                    Source.append(source)
                    destination = df_source_destination_schedule_trip['Destination'][0]
                    Destination.append(destination)
                    route = schedule_name.split('-')[0]
                    Route.append(route)
                    service_type = schedule_name.split('-')[3]
                    ServiceType.append(service_type)
                stages = all_stages
                TripStartDate = np.array(TripStartDate)
                Depot = np.array(Depot)
                Schedule = np.array(Schedule)
                Route = np.array(Route)
                ServiceType = np.array(ServiceType)
                ETM_No = np.array(ETM_No)
                Fleet_ID = np.array(Fleet_ID)
                TripNo = np.array(TripNo)
                RunNo = np.array(RunNo)
                TripStartTime = np.array(TripStartTime)
                Source = np.array(Source)
                Destination = np.array(Destination)
                Number_of_boardings = np.array(Number_of_boardings)
                Number_of_alightings = np.array(Number_of_alightings)
                Number_of_interchanges = np.array(Number_of_interchanges)
                #print(np.shape(Depot))
                d = {'TripStartDate':TripStartDate,'Depot':Depot,'Schedule':Schedule,'Route':Route,'ServiceType':ServiceType,'ETM_No':ETM_No,'Fleet_ID':Fleet_ID,'TripNo':TripNo,'RunNo':RunNo,'TripStartTime':TripStartTime,'Source':Source,'Destination':Destination,'stage_name':stages,'Number_of_boardings':Number_of_boardings,'Number_of_alightings':Number_of_alightings}
                final_df = pd.DataFrame(data=d)
                DF = DF.append(final_df)
DF


# In[24]:


DF.to_csv('C:/Users/DSNikhil/Downloads/Codes and Corresponding files/Chapter 5 Crowding Estimation and Prediction/Boardings and Alightings estimation/Boardings Alightings all trips 3-11-2016.csv',index=False)


# In[ ]:




