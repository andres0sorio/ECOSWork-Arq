from JsonEpisodeHelper import JsonEpisodeHelper

import json
import urllib2
import time
import numpy
import pylab
import random
import unittest
from time import sleep
import ast

url = 'http://localhost:4567/api/episode/get'
sim_data = 'simulated_records.dat'

def getJson(url,data):

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    start = time.time()
    response = urllib2.urlopen(req, data)
    end = time.time()
    response_json = json.load( response )
    jdata = ast.literal_eval(response_json)

    for jd in jdata:
        del jd['_id']
    
    return jdata
   
def getObject(inputline):

    data = inputline.split(',')
    p1 = JsonEpisodeHelper()
    p1.setCedula(  int(data[0]))
    p1.setFecha(       data[1] )
    p1.setHora(        data[2] )
    p1.setNivel(   int(data[3]))
    p1.setMedicamento( data[4] )
    p1.setActividad(   data[5] )
    return p1

def checkIntegrity(fname):

    with open(fname) as inputfile:

        episodes_cedula = {}
        counter = 0
        total = 0
        for line in inputfile:
            episode = getObject( line[:-1] )
            cedula = episode.getCedula()
            
            if cedula in episodes_cedula:
                episodes_cedula[cedula].append( episode )
            else:
                episodes_cedula[cedula]  = [episode]

        inputfile.close()

        #print len(episodes_cedula)

        for cedula in sorted(episodes_cedula.keys()):

            data = '{ cedula : ' + str(cedula) + '}'
            consult_results = getJson(url,data)

            #print consult_results[0]
            #print episodes_cedula[cedula][0].__dict__
            
            for episode in episodes_cedula[cedula]:
                total += 1
                for xepisode in consult_results:
                    if episode.__dict__ == xepisode:
                        counter += 1
                        break

        print counter,total
        

checkIntegrity(sim_data)


