#This program reads card data from a USB HID scanner and puts it into a queue.
#Application uses beanstalkd as a dependency.
#Run pip install beanstalkd and pip install python-beanstalkc before running
#Visit https://github.com/beanstalkd/pybeanstalk for more info


import beanstalkc
import datetime
from . import monitor_service

beanstalk = beanstalkc.Connection() #connection to beanstalkd service. To see default port, see /home/pi/.local/lib/python2.7/site-packages
beanstalk.use('default')
beanstalk.watch('default')



def scan():

    while (1):
        print("Started card scanning")
        cardData = raw_input() 
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        data = cardData + ":" + date_time
        beanstalk.put(data)
        monitor_service.monitor_service()
    
scan()    

