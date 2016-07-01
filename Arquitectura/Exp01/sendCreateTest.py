#!/usr/bin/python 

"""
send URL request (just GET)
writes latency results to a file for latter processing
"""

import urllib2
import random
import time
from time import sleep

#host     = 'http://localhost:4567/hello'
host     = 'http://192.168.1.118:4567/hello'

pointsP1 = []
output   = open('experiment-latency.dat', 'w')

def sendRequest(host):

    start = time.time()
    req = urllib2.Request(host)
    response = urllib2.urlopen(req)
    end = time.time()
    print response.getcode()
    return (end - start)

def runLatencyExperiment(ntimes):

    for i in range(0,ntimes):
        value = sendRequest(host)
        pointsP1.append(value)
        sleep(0.050)
        points = str(value)
        output.write(points + '\n')

runLatencyExperiment(100)

output.close()
