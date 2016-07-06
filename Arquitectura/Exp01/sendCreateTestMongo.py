#!/usr/bin/python

"""
send URL request (POST) to write a json document to our Mongo DB
writes latency results to a file for latter processing
"""

from JsonEpisodeHelper import JsonEpisodeHelper

import json
import urllib2
import time
import numpy
import pylab
import random
import unittest
import logging
from time import sleep

host = 'http://localhost:4567/api/episode/create'
pointsP1 = []
waittime = 0.100
output = open('experiment-latency.dat', 'w')
failed_episodes = open('failed_episodes.dat', 'w')

logging.basicConfig(filename='sendCreateTestMongo.log',level=logging.DEBUG)
logging.info('sendCreateTestMongo')

def generateData() :
    
    pacienteID = 456124
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
    except urllib2.HTTPError, e:
        logging.error( 'HTTPError = ' + str(e.code) )
    except urllib2.URLError, e:
        logging.error('URLError = ' + str(e.reason) )
    finally:
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
            output.write(points + '\n')
            
        sleep(0.050)

runLatencyExperiment(2)

output.close()

failed_episodes.close()
