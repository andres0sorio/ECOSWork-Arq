#!/usr/bin/python

"""
send URL request (POST) to write a json document to our Mongo DB
writes latency results to a file for latter processing
"""
import sys
sys.path.append('../')
from ExpPkg import JsonEpisodeHelper

import json
import urllib2
import time
import random
import unittest
from time import sleep
import ast
import logging

#................................................................

cedula = 703927262
#email = "autenticated_user@gmail.com"
email = "foobar@doctor.com"
#email = "test@correo.com"
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
        return e.code

data = '{ cedula : ' + str(cedula) + ', email : ' + '"' + email + '"' + ' }'
logging.info(data)
value = getJson(url,data)
print"return code: ", value
