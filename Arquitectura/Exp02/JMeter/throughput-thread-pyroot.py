#!/usr/bin/python

import numpy
import random
import unittest
import time
import datetime
from datetime import date
import ROOT
from ROOT import TTimeStamp
from ROOT import TDatime
from optparse import OptionParser

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
x  = 0.0

poslatency = 10
actthreads = 8

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

def drawGraphs( cgraph, canvas, title, xtitle, ytitle):
	
	canvas.SetFillColor(10)
	canvas.SetGridy()
    
	cgraph.SetTitle(title)
	cgraph.GetXaxis().SetTitle(xtitle)
	cgraph.GetXaxis().CenterTitle(True)
	cgraph.GetXaxis().SetLabelFont(42)
	cgraph.GetXaxis().SetTitleSize(0.05)
	cgraph.GetXaxis().SetTitleOffset(0.88)
	cgraph.GetXaxis().SetTitleFont(42)
	cgraph.GetYaxis().SetTitle(ytitle)
	cgraph.GetYaxis().CenterTitle(True)
	cgraph.GetYaxis().SetLabelFont(42)
	cgraph.GetYaxis().SetLabelSize(0.05)
	cgraph.GetYaxis().SetTitleSize(0.05)
	cgraph.GetYaxis().SetTitleOffset(0.91)
	cgraph.SetMarkerColor(4)
	cgraph.SetMarkerStyle(7)  
	
filenames, labels = openResults( infile )

for fname in filenames:

	act_threads  = {}
	transactions = {}
	nlines = 0
	
	with open(fname) as inputfile:
		
		for line in inputfile:
			
			data      = line[:-1].split(',')
			latency   = float(data[poslatency])
			elapsed   = float(data[1])
			timestamp = int( data[0] )
			actthread = int( data[8] )
			httpcode  = int( data[2] )
			
			if httpcode == 200:
				if timestamp in act_threads:
					act_threads[timestamp].append( actthread )
					transactions[timestamp] += 1
				
				else:
					act_threads[timestamp]  = [actthread]
					transactions[timestamp] = 1
				
			nlines += 1
			
	print nlines		
	inputfile.close()

	#...................................................................................................

	eventbin     = []
	eventbins    = []
	timebins     = []
	isfirst      = True
	elapsed_time = 0
	firsttime    = 0.0
	counter      = 1
	timeint      = 0.500
	convfactor   = (1.0/timeint)
	
	for timestamp in sorted(act_threads.keys()):

		ti = datetime.datetime.fromtimestamp(timestamp/1000.0)
		
		if isfirst:
			t0 = ti
			ti_1 = ti
			isfirst = False
			firsttime = (t0.second + t0.microsecond/1000000.0)
			timebins.append(0.0)
			continue

		x = ((ti - t0).seconds) + ((ti - t0).microseconds/1000000.0)

		deltaT = ((ti - ti_1).seconds) + ((ti - ti_1).microseconds/1000000.0)

		if x > timeint:
			eventbins.append( eventbin )
			eventbin = []
			t0 = ti
			timebins.append( timeint*counter )
			counter += 1
				
		for thread in act_threads[timestamp]:
			eventbin.append(thread)

		elapsed_time += deltaT
		ti_1 = ti

	print elapsed_time
	
	timebins.append( elapsed_time )
	eventbins.append( eventbin )

	gr1 = ROOT.TGraph()
	
	ipoint = 0
	for bin in eventbins:
		threads = numpy.array(bin)
		avg_threads = numpy.mean(threads)
		gr1.SetPoint(ipoint, timebins[ipoint], avg_threads)
		ipoint += 1

	cname = "act_threads_" + fname.split('/')[2].split('.')[0]
	print cname
	c1 = ROOT.TCanvas(cname, "Canvas for plot 1", 94,162,805,341)
	drawGraphs( gr1, c1, "Threads vs time", "Time step [sec] (granularity 500 ms)", "Average active threads")
	c1.cd()
	gr1.Draw("APL")
	
	#..........................................................................................................
	
	timebins           = []
	transactions_inbin = []
	ntrans             = 0
	firsttime          = 0.0
	elapsed_time       = 0
	isfirst            = True
	timeint            = 1.000
	convfactor         = (1.0/timeint)
	counter            = 1
	
	for timestamp in sorted(transactions.keys()):

		ti = datetime.datetime.fromtimestamp(timestamp/1000.0)

		if isfirst:
			t0 = ti
			ti_1 = ti
			isfirst = False
			firsttime = (t0.second + t0.microsecond/1000000.0)
			timebins.append(0.0)
			continue

		x = ((ti - t0).seconds) + ((ti - t0).microseconds/1000000.0)

		deltaT = ((ti - ti_1).seconds) + ((ti - ti_1).microseconds/1000000.0)

		if x > timeint:
			transactions_inbin.append( ntrans )
			ntrans = 0
			t0 = ti
			timebins.append( timeint*counter )
			counter += 1

		ntrans += transactions[timestamp]
		elapsed_time += deltaT
		ti_1 = ti

	print elapsed_time

	timebins.append( elapsed_time )
	transactions_inbin.append( ntrans )
	
	gr2 = ROOT.TGraph()

	ipoint = 0
	for tran in transactions_inbin:
		gr2.SetPoint(ipoint, timebins[ipoint], tran*convfactor)
		ipoint += 1
		
	cname = "throughput_time_" + fname.split('/')[2].split('.')[0]
	print cname
	c1 = ROOT.TCanvas(cname, "Canvas for plot 2", 94,162,805,341)
	drawGraphs( gr2, c1, "HTTP requests (success)", "Elapsed time (granularity 1 s)", "Number of transactions per second")
	c1.cd()
	gr2.Draw("APL")

