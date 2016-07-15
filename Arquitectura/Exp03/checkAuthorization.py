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

#................................................................

cedula = 703927262
email = "autenticated_user@gmail.com"
#email = "foobar@doctor.com"

#................................................................

url = 'http://localhost:4567/api/doc/get'
#url = 'http://157.253.211.97:4567/api/doc/get'

logging.basicConfig(filename='logs/sendConsultTestMongo.log',level=logging.DEBUG)
logging.info('sendConsultTestMongo.py')

def getJson(url,data):

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    try:
        start = time.time()
        response = urllib2.urlopen(req, data)
        end = time.time()
        response_json = json.load( response )
        jdata = ast.literal_eval(response_json)
        logging.info( 'HTTPCode = ' + str(response.getcode() ) )
        return response.getcode(), len(jdata)
    
    except urllib2.URLError, e:
        logging.error('URLError = ' + str(e.reason) )
        return e.code, 0

data = '{ cedula : ' + str(cedula) + ', email : ' + '"' + email + '"' + ' }'
logging.info(data)
value = getJson(url,data)
print"return http code and len(registers): ", value
