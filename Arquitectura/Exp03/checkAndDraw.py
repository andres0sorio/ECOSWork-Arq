#!/usr/bin/python

"""
sends URL request (POST) to consult patient episodes
checks authorization
"""

import json
import urllib2
import time
import unittest
from time import sleep
import logging
import ast
import datetime
from datetime import date
from datetime import timedelta

import numpy as np
import matplotlib.pyplot as plt

#................................................................

cedula = 703927262
email = "autenticated_user@gmail.com"
#email = "foobar@doctor.com"

#................................................................

url = 'http://localhost:4567/api/doc/get'

logging.basicConfig(filename='logs/sendConsultTestMongo.log',level=logging.DEBUG)
logging.info('sendConsultTestMongo.py')

def getJson(url,data):

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    try:
        start = time.time()
        response = urllib2.urlopen(req, data)
        end = time.time()
        response_json = json.load( response )
        jdata = ast.literal_eval(response_json)
        logging.info( 'HTTPCode = ' + str(response.getcode() ) )
        return response.getcode(), jdata
    
    except urllib2.URLError, e:
        logging.error('URLError = ' + str(e.reason) )
        return e.code, 0

data = '{ cedula : ' + str(cedula) + ', email : ' + '"' + email + '"' + ' }'
logging.info(data)
value, jdata = getJson(url,data)

episode_intensity = {}

for episode in jdata:
    episode_time = episode['fecha'] + " " + episode['hora']
    t0 = datetime.datetime.strptime( episode_time, '%m/%d/%Y %H:%M:%S' )
    timestamp = int(t0.strftime("%s"))
    #print timestamp, float(episode['nivelDolor'])
    episode_intensity[timestamp] = float(episode['nivelDolor'] )

x_data = []
y_data = []

for t0 in sorted(episode_intensity.keys()):
    x_data.append(float(t0))
    y_data.append(episode_intensity[t0])


# Create a Figure object.
fig = plt.figure(figsize=(5, 4))
# Create an Axes object.
ax = fig.add_subplot(1,1,1) # one row, one column, first plot
# Plot the data.
ax.scatter(x_data, y_data, color="red", marker="^")
# Add a title.
ax.set_title("Migrane intensity over time")
# Add some axis labels.
ax.set_xlabel("Timestamp")
ax.set_ylabel("Intensity")
# Produce an image.
fig.savefig("scatterplot.png")  
