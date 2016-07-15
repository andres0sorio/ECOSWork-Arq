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
#email = "foobar@doctor.com" # authorized profile
email ="autenticated_user@gmail.com"

#................................................................

host = 'https://localhost:4567/api/doc/get'

sim_data = 'data/simulated_records.dat'

logging.basicConfig(filename='logs/checkIntegrityMongoHTTPS.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('checkIntegrityMongoHTTPS')

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

    return []

def getObject(inputline):

    data = inputline.split(',')
    p1 = JsonEpisodeHelper()
    p1.setCedula(  int(data[0]))
    p1.setFecha(       data[1] )
    p1.setHora(        data[2] )
    p1.setNivel(   int(data[3]))
    p1.setMedicamento( data[4] )
    p1.setActividad(   data[5] )
    return p1

def checkIntegrity(fname):

    with open(fname) as inputfile:

        episodes_cedula = {}
        counter = 0
        total = 0
        for line in inputfile:
            episode = getObject( line[:-1] )
            cedula = episode.getCedula()
            
            if cedula in episodes_cedula:
                episodes_cedula[cedula].append( episode )
            else:
                episodes_cedula[cedula]  = [episode]
            break
        inputfile.close()

        #print len(episodes_cedula)

        for cedula in sorted(episodes_cedula.keys()):

            data = '{ cedula : ' + str(cedula) + ', email : ' + '"' + email + '"' + ' }'
            print data
            consult_results = getJson(host,data)

            #print consult_results[0]
            #print episodes_cedula[cedula][0].__dict__
            
            for episode in episodes_cedula[cedula]:
                total += 1
                for xepisode in consult_results:
                    if episode.__dict__ == xepisode:
                        counter += 1
                        break

        print counter,total
        
checkIntegrity(sim_data)
