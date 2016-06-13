#!/usr/bin/python

import numpy
import pylab
import random
import unittest

pointsP1  = []
pointsP2  = []
pointsP3  = []
pointsP4  = []
pointsP5  = []
pointsP6  = []
pointsP7  = []
pointsP8  = []
pointsP9  = []
pointsP10 = []
pointsP11 = []
pointsP12 = []
pointsP13 = []

with open('result1000.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP1.append(latency)

inputfile.close()

with open('result2000.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP2.append(latency)

inputfile.close()

with open('result4000.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP3.append(latency)

inputfile.close()

with open('result6000.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP4.append(latency)

inputfile.close()

with open('result8000.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP5.append(latency)

inputfile.close()

with open('result10000.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP6.append(latency)

inputfile.close()

with open('result13000.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP7.append(latency)

inputfile.close()

with open('concurrency-13000.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP8.append(latency)

inputfile.close()

with open('concurrency-13000-2.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP9.append(latency)

inputfile.close()

with open('concurrency-13000-3.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP10.append(latency)

inputfile.close()

with open('concurrency-13000-R1.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[6])
        pointsP11.append(latency)

inputfile.close()

with open('concurrency-13000-R2.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[6])
        pointsP12.append(latency)

inputfile.close()

with open('concurrency-13000-Box2.csv') as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        latency = float(data[5])
        pointsP13.append(latency)

inputfile.close()

data = [  pointsP1, pointsP2 , pointsP3, pointsP4, pointsP5, pointsP6 , pointsP7,
          pointsP8, pointsP9, pointsP10, pointsP11, pointsP12, pointsP13] 
labels = [ '1000', '2000', '4000', '6000', '8000', '10000', '13000','13000Box31',
           '13000Box32', '13000Box33', '13000Box3R', '13000Box3R2', '13000Box2' ]

#pylab.hist(pointsP1, bins=50, range=[0.0,80.0])

fig = pylab.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)

bp = ax.boxplot(data, patch_artist=True)

fig.suptitle('Concurrency experiments Box1', fontsize=14, fontweight='bold')

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
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

fig.savefig('fig1.png', bbox_inches='tight')
