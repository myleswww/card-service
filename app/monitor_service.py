# -*- coding: utf-8 -*-

#/usr/bin/python3

import beanstalkc
import requests
import re #used for splitting strings
import json


service = beanstalkc.Connection() #set connection to default connection
service.use('default') #use and watch the default tube
service.watch('default')

def format_data(job):
    '''format the data so it is in json format'''

<<<<<<< Updated upstream
    a = re.split(':', job)
    data_card = [
        {'card_id' : a[0],monitor_service.monitor_service()
         'date_time' : a[1]}]
=======
    a = re.split('!', job)
    data_card = "{'card_id' : a[0], 'date_time' : a[1]}"

    

    print(a[0])
>>>>>>> Stashed changes
    print(a[1])
    return data_card

def send_to_api(queued_job):
    '''send it to the api'''
<<<<<<< Updated upstream

    val = requests.post('http://127.0.0.1:5000/records').ok
    #if successful, set val to true, otherwise false
    return val
=======
    headers = {"content-type":"application/json"}
    url = 'http://127.0.0.1:5000/records'

    val = requests.post(url = url, data = queued_job, headers=headers) 

    val.raise_for_status() #need code 200
    
    return val.ok

>>>>>>> Stashed changes



def monitor_service():
    print("Starting queue monitoring")

    job = service.reserve() #get job
    print(job.body)

    while (1): #while loop checks if any data is in the queue and then dequeues it
        if job.body != None:  #use is not None
            
            #send data to api
            new_data = format_data(job.body) #format
            status = send_to_api(new_data) #function to post
            print(status)
            #if sending to service is successful:
            if (status):
                job.delete()
        
            #else, bury it then kick it:
<<<<<<< Updated upstream
            if(status != True): #use is false orif(Not status)
=======
            if(status is False): #use is false orif(Not status)
>>>>>>> Stashed changes
                job.bury()
                job.kick()
        
            #get next job
            job = service.reserve()

if __name__=='__main__':
    monitor_service()