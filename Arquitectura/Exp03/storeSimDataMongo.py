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

host = 'http://157.253.17.148:4567/api/episode/create'
pointsP1 = []
output = open('experiment-latency.dat', 'w')
waittime = 0.005
failed_episodes = open('failed_episodes.dat', 'w')

logging.basicConfig(filename='storeSimDataMongo.log',level=logging.DEBUG)
logging.info('sendCreateTestMongo')

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

runLatencyExperiment("simulated_records.dat")

output.close()

failed_episodes.close()

