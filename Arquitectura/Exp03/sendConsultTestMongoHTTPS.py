#!/usr/bin/python

"""
send URL request (POST) to write a json document to our Mongo DB
writes latency results to a file for latter processing
"""
import sys
sys.path.append('../')
from ExpPkg import JsonEpisodeHelper

import requests
import json
import time
import random
import unittest
from time import sleep
import ast
import logging

#................................................................

cedula = 703927262
email = "autenticated_user@gmail.com"
#email = "foobar@doctor.com"
#................................................................

host = 'https://localhost:4567/api/doc/get'

logging.basicConfig(filename='logs/sendConsultTestMongoHTTPS.log',level=logging.DEBUG)
logging.info('sendConsultTestMongoHTTPS.py')

def getJson(host,data):

    headers = {'Content-Type': 'application/json'}
    try:
        start = time.time()
        response = requests.post( host, data=json.dumps(data), headers=headers, verify=False)
        end = time.time()
        print response
        try:
            response_json = response.json() 
            print response_json
        except ValueError as e:
            print e.message

        #jdata = ast.literal_eval(response_json)
        #for jd in jdata:
        #    del jd['_id']
            
    except requests.exceptions.RequestException as e:
        logging.error('URLError = ' + str(e.message) )

    return -1





data = '{ cedula : ' + str(cedula) + ', email : ' + '"' + email + '"' + ' }'
logging.info(data)
value = getJson(host,data)
print"return code: ", value
