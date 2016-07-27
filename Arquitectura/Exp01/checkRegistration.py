#!/usr/bin/python

"""
sends URL request (POST) to consult patient episodes
checks authorization
"""

import json
import urllib2
import time
import unittest
from time import sleep
import logging
import ast
import datetime
from datetime import date
from datetime import timedelta

#................................................................

cedula = 94418
email = "osorio.af@gmail.com"
name = "Juan"
lastName1 = "Osorio"
lastName2 = "Osorio"
password = "ASDedc"
birthDate = "01/01/2000"

#................................................................

url = 'http://192.168.1.103:4567/citizen/create'

logging.basicConfig(filename='send.log',level=logging.DEBUG)
logging.info('checkRegistration.py')

def sendJson(url,data):

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    try:
        start = time.time()
        response = urllib2.urlopen(req, data)
        end = time.time()
        logging.info( 'HTTPCode = ' + str(response.getcode() ) )
        return response.getcode()
    
    except urllib2.URLError, e:
        logging.error('URLError = ' + str(e.reason) )
        return e, 0

data = '{ \"identification\" : ' + str(cedula)
data += ', \"email\" : ' + '"' + email + '"'
data += ", \"name\" : " + '"' + name + '"'
data += ", \"lastName1\"  : " + '"' + lastName1  + '"'
#data += ", lastName2  : " + '"' + lastName2  + '"'
data += ", \"password\"   : " + '"' + password   + '"'
#data += ", \"birthDate  : " + '"' + birthDate  + '"'
data += ' }'


#logging.info(data)
value = sendJson(url,data)
print json.dumps(data), value
