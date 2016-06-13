#!/usr/bin/python

import numpy
import pylab
import random
import unittest
import time
import datetime
from datetime import date

pointsP1X = []
pointsP1Y = []

nRequests = 0
t0 = datetime.datetime
ti = datetime.datetime
tlast = datetime.datetime

x = 0.0
xmax = 0.0
timeint = 1

with open('concurrency-9000.csv') as inputfile:
    for line in inputfile:

        data = line[:-1].split(',')
        latency = float(data[5])
        timestamp = float(data[0])
        ti = datetime.datetime.fromtimestamp(timestamp/1000.0)

        if nRequests == 0:
            pointsP1X.append(x)
            pointsP1Y.append(nRequests)
            t0 = ti
            nRequests += 1
            continue

        x = ((ti - t0).seconds) + ((ti - t0).microseconds/1000000.0)

        if x > 100.0 :
            print x, nRequests
            continue

        if x > xmax:
            xmax = x

        if x  > timeint:
            pointsP1X.append(x)
            pointsP1Y.append(nRequests)
            timeint += 1.0
        
        nRequests += 1

pointsP1X.append(x)
pointsP1Y.append(nRequests)

print xmax

inputfile.close()

pylab.plot(pointsP1X,pointsP1Y, 'ro')
pylab.ylabel('some numbers')
pylab.show()

