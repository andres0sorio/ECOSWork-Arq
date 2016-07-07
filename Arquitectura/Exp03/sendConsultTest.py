import sys
sys.path.append('../')
from ExpPkg import JsonEpisodeHelper

import json
import urllib2
import time
import numpy
import pylab
import random
import unittest
from time import sleep

host = 'http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false'

def getJson(url):

    start = time.time()
    response = urllib2.urlopen(url)
    end = time.time()
    print json.loads(response.read())
    return (end - start)

def runLatencyExperiment(ntimes):

    for i in range(0,ntimes):
        value = getJson(host)
        pointsP1.append(value)
        print i
        sleep(0.050)
        points = str(value)

runLatencyExperiment(2)

