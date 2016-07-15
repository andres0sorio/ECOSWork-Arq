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

host = 'https://localhost:4567/api/user/create' #ok
#host = 'https://server.as-experiments.test:8089/api/user/create' # B0

pointsP1 = []
waittime = 0.005
output = open('data/experiment-latency-ssl.dat', 'w')
output_3xcols = open('data/experiment-latency-3xcols-ssl.dat', 'w')
failed_episodes = open('data/failed_episodes-ssl.dat', 'w')

logging.basicConfig(filename='logs/sendCreateTestMongo.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.info('sendCreateTestMongoSSL')

def generateData() :
    
    pacienteID = 26253282
    fecha = '2016/12/31'
    hora = '12:00:00'

    p1 = JsonEpisodeHelper()
    p1.setCedula(pacienteID)
    p1.setFecha(fecha)
    p1.setHora(hora)
    
    return p1.__dict__

def sendJson(host, data):

    headers = {'Content-Type': 'application/json'}
    try:
        start = time.time()
        response = requests.post( host, data=json.dumps(data), headers=headers, verify=False)
        end = time.time()
        code = response.status_code
        return (end - start), code
    except requests.exceptions.RequestException as e:
        logging.error('URLError = ' + str(e.message) )
    
    return -1, -1

def saveEpisode(data):
    failed_episodes.write(str(data) + '\n')
    
def runLatencyExperiment(ntimes):

    for i in range(0,ntimes):
        success = False
        data = generateData()
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
                    continue
        if success == False:
            saveEpisode(data)
        else:
            points = str(value)
            httpcode = str(code)
            output.write( points + '\n')
            output_3xcols.write(str(i) + ',' + httpcode + ',' + points + '\n')
            
        sleep(0.010)

runLatencyExperiment(10)

output.close()
output_3xcols.close()
failed_episodes.close()
