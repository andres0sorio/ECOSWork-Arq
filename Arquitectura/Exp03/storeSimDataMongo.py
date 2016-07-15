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

#host = 'http://server.as-experiments.test:8080/api/user/create'
host = 'http://localhost:4567/api/user/create'

pointsP1 = []
waittime = 0.005
failed_episodes = open('logs/failed_episodes.dat', 'w')

logging.basicConfig(filename='logs/storeSimDataMongo.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
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
        logging.info( 'HTTPCode = ' + str(code) )
        return (end - start), code
    except urllib2.URLError, e:
        logging.error('URLError = ' + str(e.reason) )

    return -1, -1

def saveEpisode(data):
    failed_episodes.write(str(data) + '\n')




def saveData(fname):
    counter = 0
    with open(fname) as inputfile:
        
	for line in inputfile:
            data = generateData( line[:-1] )
            success = False
            value, code = sendJson(host,data)

            if code == 200:
                pointsP1.append(value)
                success = True
            elif code <= 0:

                for j in range(3):
                    logging.info('will try to send episode again')
                    sleep(waittime)
                    #value, code = sendJson(host,data)
                    code = -1
                    if code == 200:
                        pointsP1.append(value)
                        success = True
                        break
                    else:
                        logging.info('Failed attemp number: ' + str(j+1) )
                        continue

            if success == False:
                saveEpisode(data)
            else:
                points = str(value)
                logging.info('Success sending episode: httpcode ' + str(code) + ' ' + points)

            counter += 1
            sleep(0.001)
            if counter >= 500:
                break
            
    inputfile.close()

saveData("data/simulated_records.dat")

failed_episodes.close()

