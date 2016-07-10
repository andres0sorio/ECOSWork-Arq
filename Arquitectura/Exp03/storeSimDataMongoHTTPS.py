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
import logging

from time import sleep

host = 'https://localhost:4567/api/user/create'

pointsP1 = []
output = open('data/experiment-latency.dat', 'w')
waittime = 0.005
failed_episodes = open('logs/failed_episodes.dat', 'w')

logging.basicConfig(filename='logs/storeSimDataMongoHTTPS.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('sendCreateTestMongoHTTPS')

def generateData( inputline) :

    data = inputline.split(',')
    
    p1 = JsonEpisodeHelper()
    p1.setCedula(  int(data[0]))
    p1.setFecha(       data[1] )
    p1.setHora(        data[2] )
    p1.setNivel(   int(data[3]))
    p1.setMedicamento( data[4] )
    p1.setActividad(   data[5] )
    
    return p1.__dict__

def sendJson(host, data):

    headers = {'Content-Type': 'application/json'}
    try:
        start = time.time()
        response = requests.post( host, data=json.dumps(data), headers=headers, verify=False)
        end = time.time()
        code = response.status_code
        if code == 200:
            logging.info('Success sending episode: httpcode ' + str(code))
        return (end - start), code
    except requests.exceptions.RequestException as e:
        logging.error('URLError = ' + str(e.message) )
    
    return -1, -1

def saveEpisode(data):
    failed_episodes.write(str(data) + '\n')
    
def runLatencyExperiment(fname):

    with open(fname) as inputfile:
        
	for line in inputfile:
            data = generateData( line[:-1] )
            success = False
            value, code = sendJson(host,data)
            if code == 200:
                pointsP1.append(value)
                success = True
                logging.info('Success sending episode: httpcode ' + str(code))
            elif code <= 0:
                for j in range(3):
                    logging.info('will try to send episode again')
                    sleep(waittime)
                    value, code = sendJson(host,data)
                    if code == 200:
                        pointsP1.append(value)
                        success = True
                        logging.info('Success sending episode: httpcode ' + str(code))
                        break
                    else:
                        logging.info('Failed attemp no')
                        continue
            if success == False:
                saveEpisode(data)
            else:
                points = str(value)
                output.write(points + '\n')
            
            sleep(0.050)
        
    inputfile.close()

runLatencyExperiment("data/simulated_records.dat")

output.close()

failed_episodes.close()

