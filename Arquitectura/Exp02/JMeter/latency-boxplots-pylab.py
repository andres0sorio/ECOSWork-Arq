#!/usr/bin/python

import numpy
import pylab
import random
import unittest
import os,sys
import string
from optparse import OptionParser
import logging


#-----------------------------------------------------
parser = OptionParser()
parser.add_option("-i", type = "string", dest="input",
                  help="Input file with results", metavar="input" )


parser.add_option("-o", type = "string", dest="output",
                  help="Name of output figure", metavar="output" )

(options, args) = parser.parse_args()

if options.input is None:
        parser.error("please give an input")

if options.output is None:
        parser.error("please give an ouput")
#-----------------------------------------------------

infile = options.input
outfile = options.output
poslatency = 5

logging.basicConfig(filename='quick-pylab.log',level=logging.DEBUG)

def openResults( resultsfile ):
    lbs = []
    fnames = []
    with open(resultsfile) as inputfile:
        for line in inputfile:
            data = line[:-1].split(',')
            fnames.append( data[0] )
            lbs.append( data[1] )
    inputfile.close()
    return fnames, lbs

def readData( infile ):
    pointsP1 = []
    http_success = 0
    http_error = 0
    nlines = 0

    with open(infile) as inputfile:
	    
	    for line in inputfile:
		    data = line[:-1].split(',')

		    try:
			    if len(data) > 7:
				    poslatency = 1
			    latency = float(data[poslatency])
			    httpcode  = int( data[2] )
			    if httpcode == 200:
				    pointsP1.append(latency)
				    http_success += 1
			    else:
				    http_error += 1
				    
		    except ValueError:
			    http_error += 1
			    logging.error('Sample data had a strange behaviour')
			    logging.info(line)

		    nlines += 1
		    
    print http_error, http_success, nlines
    inputfile.close()
    return pointsP1

filenames, labels = openResults( infile )

data = []

for iname in filenames:
    pointsP1 = readData( iname )
    data.append( pointsP1 )

fig = pylab.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)

bp = ax.boxplot(data, patch_artist=True)

fig.suptitle('Concurrency experiments Box1', fontsize=14, fontweight='bold')

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    box.set( color='#7570b3', linewidth=2)
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

ax.set_xticklabels( labels )
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

ax.set_xlabel('Concurrent users')
ax.set_ylabel('Latency [ms]')
ax.set_yscale('log')

locs, lbs = pylab.xticks()
pylab.setp(lbs, rotation=45)

fig.savefig(outfile, bbox_inches='tight')
