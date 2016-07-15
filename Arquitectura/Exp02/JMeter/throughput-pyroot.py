#!/usr/bin/python

import numpy
import random
import unittest
import time
import datetime
from datetime import date
import ROOT
from optparse import OptionParser
from ROOT import TTimeStamp
from ROOT import TDatime

#-----------------------------------------------------
parser = OptionParser()
parser.add_option("-i", type = "string", dest="input",
                  help="Input file with results", metavar="input" )

(options, args) = parser.parse_args()

if options.input is None:
        parser.error("please give an input")

#-----------------------------------------------------

infile = options.input

t0 = datetime.datetime
ti = datetime.datetime
tlast = datetime.datetime

x = 0.0
xmax = 0.0
timeint = 0.500
convfactor = (1.0/timeint)
poslatency = 5 #for backward compatibility with old data
poscode = 2 

thr_summary = open('thr_summary.dat','w')

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

filenames, labels = openResults( infile )

summary = ROOT.TGraph()
h1 = ROOT.TH1F("Exp1","Latency (0.5 ms per bin)", 100, 0.0, 50.00)

jpoint = 0

for fname in filenames:

    gr = ROOT.TGraph()
    gr_lat_th = ROOT.TGraph()

    eventbin  = []
    eventbins = []
    timebins  = []
    timenorm  = {}
    isfirst = True
    firsttime = 0.0
    http_error = 0
    with open(fname) as inputfile:

        for line in inputfile:

            data = line[:-1].split(',')
	    if len(data) > 8:
		    poslatency = 10
		    poscode = 2
	    elif len(data) > 7 and len(data) < 10:
		    poslatency = 6
		    poscode = 2
	    try:
		    latency = float(data[poslatency]) 
		    timestamp = int( data[0] )

		    if len(data) > 7:
			    httpcode  = int( data[poscode] )
		    else:
			    httpcode = 200 # for backward comptability with old data
		    
		    if httpcode == 200:
			    if timestamp in timenorm:
				    timenorm[timestamp].append(latency)
			    else:
				    timenorm[timestamp]  = [latency]
		    else:
			    http_error += 1
			    
	    except ValueError:
			httpcode  = -1

    inputfile.close()

    for timestamp in sorted(timenorm.keys()):

	    ti = datetime.datetime.fromtimestamp(timestamp/1000.0)
	    	    
            if isfirst:
		    t0 = ti
		    isfirst = False
		    firsttime = (t0.second + t0.microsecond/1000000.0)
		    timebins.append(0.0)
		    continue

            x = abs( ((ti - t0).seconds) + ((ti - t0).microseconds/1000000.0) )

	    if x > timeint:
		    eventbins.append( eventbin )
		    eventbin = []
		    t0 = ti
		    delta = (t0.second + t0.microsecond/1000000.0) - firsttime
		    if delta < 0:
			    delta = delta + 60.0
		    timebins.append( delta )

	    for lat in timenorm[timestamp]:
		    eventbin.append(lat)

    ipoint = 0

    throughput = []

    for bin in eventbins:
        throughput.append( float(len(bin)) )
        gr.SetPoint(ipoint, timebins[ipoint], float(len(bin))*convfactor )
	latencies = numpy.array(bin)
	avg_latency = latencies.mean()
	gr_lat_th.SetPoint(ipoint, float(len(bin))*convfactor, avg_latency)
        ipoint += 1

    th = numpy.array(throughput)

    #summary.SetPoint(jpoint, (jpoint+1), th.mean() * convfactor )
    summary.SetPoint(jpoint, float(labels[jpoint]), th.mean() * convfactor )
    thr_summary.write( labels[jpoint] + ',' + str( th.mean() * convfactor ) + '\n' )
    
    cname = "throughput_" + fname.split('/')[2].split('.')[0]
    
    c1 = ROOT.TCanvas(cname, "Canvas for plot 1", 94,162,805,341)
    c1.SetFillColor(10)
    c1.SetGridy()
    c1.cd()
    
    gr.SetMinimum(0.0)
    gr.SetMaximum(2000.0)
    
    #gr.GetXaxis().SetTimeDisplay(1)
    #gr.GetXaxis().SetTimeFormat("%M%S")
    
    gr.SetTitle("Throughput - Expected users in 10 s")
    #gr->SetMarkerColor(2)
    #gr->SetMarkerStyle(4)
    gr.GetXaxis().SetTitle("Time step")
    gr.GetXaxis().CenterTitle(True)
    gr.GetXaxis().SetLabelFont(42)
    gr.GetXaxis().SetTitleSize(0.05)
    gr.GetXaxis().SetTitleOffset(0.88)
    gr.GetXaxis().SetTitleFont(42)
    gr.GetYaxis().SetTitle("Throughput [requests/sec]")
    gr.GetYaxis().CenterTitle(True)
    gr.GetYaxis().SetLabelFont(42)
    gr.GetYaxis().SetLabelSize(0.05)
    gr.GetYaxis().SetTitleSize(0.05)
    gr.GetYaxis().SetTitleOffset(0.91)
    gr.SetMarkerColor(4)
    gr.SetMarkerStyle(7)  
    gr.Draw("AP")

    c1.Print( "./ThroughputResults/" + cname + ".png")

    jpoint += 1

    cname = "latvsthroug_" + fname.split('/')[2].split('.')[0]

    c2 = ROOT.TCanvas(cname, "Canvas for plot 1", 94,162,805,341)
    c2.SetFillColor(10)
    c2.SetGridy()
    c2.cd()
    
    gr_lat_th.SetMinimum(0.0)
    gr_lat_th.SetMaximum(2000.0)
    
    gr_lat_th.SetTitle("Throughput graph")
    gr_lat_th.GetXaxis().SetTitle("Throughput [requests/sec]")
    gr_lat_th.GetXaxis().CenterTitle(True)
    gr_lat_th.GetXaxis().SetLabelFont(42)
    gr_lat_th.GetXaxis().SetTitleSize(0.05)
    gr_lat_th.GetXaxis().SetTitleOffset(0.88)
    gr_lat_th.GetXaxis().SetTitleFont(42)
    gr_lat_th.GetYaxis().SetTitle("Average latency")
    gr_lat_th.GetYaxis().CenterTitle(True)
    gr_lat_th.GetYaxis().SetLabelFont(42)
    gr_lat_th.GetYaxis().SetLabelSize(0.05)
    gr_lat_th.GetYaxis().SetTitleSize(0.05)
    gr_lat_th.GetYaxis().SetTitleOffset(0.91)
    gr_lat_th.SetMarkerColor(4)
    gr_lat_th.SetMarkerStyle(7)  
    gr_lat_th.Draw("AP")

    c2.Print( "./ThroughputResults/" + cname + ".png")

c1 = ROOT.TCanvas("Summary", "Canvas for plot 1", 94,162,805,341)
c1.SetFillColor(10)
c1.SetGridy()
c1.cd()

summary.SetMarkerColor(4)
summary.SetMarkerStyle(21)
summary.SetMarkerSize(0.8)
   
summary.SetTitle("Throughput - Concurrent users expected in 10 s")
summary.GetXaxis().SetTitle("Concurrent users")
summary.SetMarkerColor(2)
summary.SetMarkerStyle(4)
summary.GetXaxis().CenterTitle(True)
summary.GetXaxis().SetLabelFont(42)
summary.GetXaxis().SetTitleSize(0.05)
summary.GetXaxis().SetTitleOffset(0.88)
summary.GetXaxis().SetTitleFont(42)
summary.GetYaxis().SetTitle("Throughput [requests/sec]")
summary.GetYaxis().CenterTitle(True)
summary.GetYaxis().SetLabelFont(42)
summary.GetYaxis().SetLabelSize(0.05)
summary.GetYaxis().SetTitleSize(0.05)
summary.GetYaxis().SetTitleOffset(0.91)
summary.Draw("AP")

thr_summary.close()
