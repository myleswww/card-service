# -*- coding: utf-8 -*-

#This program reads card data from a USB HID scanner and puts it into a queue.

import beanstalkc
import datetime
from monitor_service import *
from beanstalkd_connection import *
import smtplib


def init():
    '''Takes the event ID and passes it along to the API'''

    print("Please enter the event ID:")
    event_id = raw_input()

    scan(event_id)




def scan(event_id):
    '''When a card is scanned as keyboard input, the current time is recorded and sent to beanstalkd service'''

    beanstalk = connection() #connect to beanstalkd

    while (1):
        print("Started card scanning")
        card_data = raw_input() 
        time_now = datetime.datetime.now()
        current_date_time = time_now.strftime("%m/%d/%Y, %H:%M:%S")
        data = card_data + "!" + current_date_time
        beanstalk.put(data)
        
if __name__== '__main__':    
    init()    

