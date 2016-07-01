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
    start = time.time()
    response = urllib2.urlopen(req, json.dumps(data))
    end = time.time()
    print response
    return (end - start)

def runLatencyExperiment(ntimes):

    for i in range(0,ntimes):
        data = generateData()
        print data
        value = sendJson(host,data)
        pointsP1.append(value)
        print i
        sleep(0.050)
        points = str(value)
        output.write(points + '\n')

runLatencyExperiment(2)

output.close()
