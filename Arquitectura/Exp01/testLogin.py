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
import logging
from time import sleep

#host = 'http://localhost:4567/api/user/create' #ok
#host = 'http://box1.as-experiments.test:8080/api/user/create'  # ok box 1
#host = 'http://server.as-experiments.test:8080/api/user/create' #    B0

pointsP1 = []
waittime = 0.005
output = open('data/experiment-latency.dat', 'w')
output_3xcols = open('data/experiment-latency-3xcols.dat', 'w')
failed_episodes = open('data/failed_episodes.dat', 'w')

logging.basicConfig(filename='logs/sendCreateTestMongo.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.info('sendCreateTestMongo')

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

    req = urllib2.Request(host)
    req.add_header('Content-Type', 'application/json')
    try:
        start = time.time()
        response = urllib2.urlopen(req, json.dumps(data))
        end = time.time()
        code = response.getcode()
        return (end - start), code
    except urllib2.URLError, e:
        logging.error('URLError = ' + str(e.reason) )

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

runLatencyExperiment(1000)

output.close()
output_3xcols.close()
failed_episodes.close()
