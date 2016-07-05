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
from time import sleep

host = 'http://localhost:4567/api/episode/create'
pointsP1 = []
output = open('experiment-latency.dat', 'w')

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
    start = time.time()
    response = urllib2.urlopen(req, json.dumps(data))
    end = time.time()
    print response
    return (end - start)

def runLatencyExperiment(fname):
    
    with open(fname) as inputfile:
		
	for line in inputfile:
            data = generateData( line[:-1] )
            #print data
            value = sendJson(host,data)
            pointsP1.append(value)
            sleep(0.050)
            points = str(value)
            output.write(points + '\n')

    inputfile.close()

runLatencyExperiment("simulated_records.dat")

output.close()
