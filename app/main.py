# -*- coding: utf-8 -*-

#This program reads card data from a USB HID scanner and puts it into a queue.

import beanstalkc
import datetime
from . import monitor_service, beanstalkd_connection
import smtplib

smtpObj = smtplib.SMTP('outlook.office365.com')
sender = 'mbwright@butler.edu'
recievers = ['techteam@butler.edu']

try:
   beanstalk = beanstalkd_connection.connection()
except ConnectionError:
    #literally do something, send a tweet or a text
    message = """From: <mbwright@butler.edu>
    To: <techteam@butler.edu>, <npartenh@butler.edu>
    Subject: Automated Message: Event Scanner Error
    
    The beanstalkd service on Scanner #1 could not be connected to, 
    please restart the service.
    #This is an automated message.
    """
    try:
        smtpObj.sendmail(sender, recievers, message)
    except SMTPException:
        print('Errpr: Unable to send email')



def scan():
'''When a card is scanned as keyboard input, the current time is recorded and sent to beanstalkd service'''
    while (1):
        print("Started card scanning")
        card_data = raw_input() 
        time_now = datetime.datetime.now()
        current_date_time = time_now.strftime("%m/%d/%Y, %H:%M:%S")
        data = card_data + ":" + current_date_time
        beanstalk.put(data)
        
if __name__== '__main__':    
    scan()    

