# -*- coding: utf-8 -*-

import beanstalkc

def connection():
    beanstalk = beanstalkc.Connection() 
    beanstalk.use('default')
    beanstalk.watch('default')
    return beanstalk