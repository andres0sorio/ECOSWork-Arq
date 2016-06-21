from JsonEpisodeHelper import JsonEpisodeHelper

import json
import urllib2
import time
import numpy
import pylab
import random
import unittest
from time import sleep


def getJson(url,data):

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    start = time.time()
    response = urllib2.urlopen(req, data)
    end = time.time()
    print json.loads(response.read())
    return (end - start)

url = 'http://localhost:4567/api/episode/create'
    
pointsP1 = []

output = open('experiment2-latency', 'w')

def runLatencyExperiment(ntimes):

    for i in range(0,ntimes):
        data = '{ cedula : 1234123 }'
        value = getJson(host,data)
        pointsP1.append(value)
        print i
        sleep(0.050)
        points = str(value)
        output.write(points + '\n')

runLatencyExperiment(2)

##pylab.hist(pointsP1, label='Latency')
##pylab.title('Simple service simulation')
##pylab.xlabel('reponse time [s]')
##pylab.ylabel('Frecuency')
#pylab.show()

#output.close()




