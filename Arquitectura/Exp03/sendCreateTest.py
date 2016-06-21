from Episodio import Episodio
from Migrana import Migrana

import json
import urllib2
import time
import numpy
import pylab
import random
import unittest
from time import sleep

## Test for AS-Experiment (backend with Postgresql)


def generateData() :
    
    pacienteID = 456124
    fecha = '2016/12/31 19:00:00'

    p1 = Episodio()
    m1 = Migrana()
    p1.setID(pacienteID)
    m1.setID(pacienteID)
    m1.setFecha(fecha)
    data = p1.__dict__
    del data['migrana']
    data['migrana'] = m1.__dict__
    return data

def sendJson(host, data):

    req = urllib2.Request(host)
    req.add_header('Content-Type', 'application/json')
    start = time.time()
    response = urllib2.urlopen(req, json.dumps(data))
    end = time.time()
    print response
    return (end - start)

host = 'http://localhost:5000/api/episode/create'

pointsP1 = []

output = open('data/experiment3-latency.csv', 'w')

def runLatencyExperiment(ntimes):

    for i in range(0,ntimes):
        data = generateData()
        value = sendJson(host,data)
        pointsP1.append(value)
        print i
        sleep(0.500)



runLatencyExperiment(250)

output.close()

pylab.hist(pointsP1, label='Latency')
pylab.title('Simple service simulation')
pylab.xlabel('reponse time [s]')
pylab.ylabel('Frecuency')
pylab.show()


