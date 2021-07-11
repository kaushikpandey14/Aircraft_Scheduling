from datetime import datetime
import math,copy
from dateutil.relativedelta import relativedelta
import pandas as pd

no_of_location=int(input('No. of locations: '))
Type_of_aircrafts=int(input('No. of aircrafts type: '))
Quantity_of_each_type=[]
for i in range(Type_of_aircrafts):
   y=int(input('No. of aircraft of type'+str(i+1)+': '))
   Quantity_of_each_type.append(y)
U=[]


Type=0
for i in Quantity_of_each_type:
    Type+=1
    aircraft_capacity=int(input('Load capacity of type'+str(Type)+' aircraft(in kgs): '))
    processing_time=int(input('Processing time of type'+str(Type)+' aircraft(in Minutes): '))
    start_time = input('Give start time of aircraft type'+str(Type)+' in format(DD.MM.YYYY HH.MM.SS): ')
    start_time_format=datetime.strptime(start_time,'%d.%m.%Y %H.%M.%S')
    for j in range(i):  
        tup=[Type,j+1,aircraft_capacity,processing_time,start_time_format]
        U.append(tup)
        
U1=copy.deepcopy(U)
U2=copy.deepcopy(U)
mission_start_time = input('Mission start time in format(DD.MM.YYYY HH.MM.SS): ')#,reverse = True
mission_start_time_format=datetime.strptime(mission_start_time,'%d.%m.%Y %H.%M.%S')
f=[]
processing_time=[]
for i in U:
    processing_time.append(i)
def sortforth(val): 
    return val[3]
processing_time.sort(key = sortforth)
#print(min(U[ ][4]))
def sortforth(val): 
    return val[4]
U.sort(key = sortforth)
def sortforth(val): 
    return val[4]
U1.sort(key = sortforth)
def sortforth(val): 
    return val[4]
U2.sort(key = sortforth)

for p in U1:
    m=p[3]
    p[4]=mission_start_time_format+(relativedelta(hours=+1, minutes=+m)+relativedelta(minutes=+m))  
    

for q in U2:
    m=q[3]
    q[4]=mission_start_time_format+(relativedelta(hours=+1, minutes=+m)+relativedelta(minutes=+m))*2  
    


Starttym_mission=[]
strt_tym_of_missions1=[]

def Bmission(mission_start_time_format,U):
    
    luggage_load=int(input('total luggage/food/crew load of mission assigned: '))
    fuel_load=int(input('total fuel supplies load of mission assigned: '))
    mergeable_load=luggage_load+fuel_load
    ammunation_load=int(input('total ammunition load of mission assigned: '))
    

    def shedule(U,mission_start_time_format,total_load):
        
        Tload_can_be_carried=0
        for i in U:
            Tload_can_be_carried=Tload_can_be_carried+i[2]

        if Tload_can_be_carried>=total_load:
            y=[]
            for j in U:
                
                if total_load>=(-48000):
                    A=j
                    y.append(A)
                    
                total_load=total_load-j[2]
           
           
            z=(mission_start_time_format,y)
            S.append(z)
        else:
            b=0
            
            while total_load>=0:
                if total_load>=0:
                    x=[]
                    for j in U: 
                        if total_load>=0:
                            x.append(j)
                        
                        total_load=total_load-j[2]
                    U=copy.deepcopy(U)
                    for p in U:
                        m=p[3]
                        p[4]=mission_start_time_format+(relativedelta(hours=+1, minutes=+m)+relativedelta(minutes=+m))*(b+1)
                  
                    processing_time1=max(processing_time)
                    m=processing_time1[3]
                    mission_start_time_format=mission_start_time_format+(relativedelta(hours=+1, minutes=+m)+relativedelta(minutes=+m))*b  
                    strt_tym_of_missions1.append(mission_start_time_format)       
                    z=(mission_start_time_format,x)
                    S.append(z)
                    b+=1

                
        



    n=0
    F=0
    for i in mergeable_load,ammunation_load:
        total_load=i
        if n==0 :
            S=[]
            shedule(U,mission_start_time_format,total_load)
            print('--------OUTPUT SUB MISSION '+str(n+1)+'--------')
            print('Nos. of Sub-Sub-Mission assigned: ',len(S))
            print('Start time of mission are:\n',S)
            F=len(S)
            f.append(F)

        else:
            U=copy.deepcopy(U)
            for p in U:
                m=p[3]
                p[4]=mission_start_time_format+(relativedelta(hours=+1, minutes=+m)+relativedelta(minutes=+m))*(F)
            mission_start_time=str(strt_tym_of_missions1[-1]+(relativedelta(hours=+1, minutes=+m)+relativedelta(minutes=+m)))
            mission_start_time_format=datetime.strptime(mission_start_time,'%Y-%m-%d %H:%M:%S')
            S=[]
            shedule(U,mission_start_time_format,total_load)
            print('--------OUTPUT SUB MISSION '+str(n+1)+'--------')
            print('Nos. of Sub-Sub-Mission assigned: ',len(S))
            print('Start time of mission are:\n',S)
            G=len(S)
            f.append(G)
        n+=1                
            

for d in range(no_of_location):
   
    if d==0:
        print('-----------------------------------OUTPUT MISSION LOCATION 1-----------------------------------')
        Bmission(mission_start_time_format,U)

    else:
        U=copy.deepcopy(U)
       
        H=f[0]+f[1]
        for p in U:
                m=p[3]
                p[4]=mission_start_time_format+(relativedelta(hours=+1, minutes=+m)+relativedelta(minutes=+m))*(H)
        mission_start_time=str(strt_tym_of_missions1[-1]+(relativedelta(hours=+1, minutes=+m)+relativedelta(minutes=+m))*2)
        mission_start_time_format=datetime.strptime(mission_start_time,'%Y-%m-%d %H:%M:%S')
        strt_tym_of_missions1.append(mission_start_time_format)
        print('-----------------------------------OUTPUT MISSION LOCATION 2-----------------------------------')
        
        for i in range(Type_of_aircrafts):
            processing_time=int(input('Processing time of type'+str(i+1)+' aircraft(in minutes): '))
            for j in U:
                if j[0]==i+1:
                    j[3]=processing_time

        processing_time=[]
        for i in U:
            processing_time.append(i)
        def sortforth(val): 
            return val[3]
        processing_time.sort(key = sortforth)
        Bmission(mission_start_time_format,U)
