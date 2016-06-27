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
from ROOT import TProfile

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
	nlines = 0
	
	with open(fname) as inputfile:
		
		for line in inputfile:
			
			data      = line[:-1].split(',')
			latency   = float(data[poslatency])
			elapsed   = float(data[1])
			timestamp = int( data[0] )
			actthread = int( data[8] )
			
			try:
				httpcode  = int( data[2] )
				if httpcode == 200:
					if timestamp in act_threads:
						act_threads[actthread].append( latency )
					else:
						act_threads[actthread]  = [latency]
			except ValueError:
				httpcode  = -1
				
			nlines += 1
			
	print nlines
	print len(act_threads)
	
	inputfile.close()

	#...................................................................................................
	ipoint = 0
	gr1 = ROOT.TGraph()
	
	for threads in sorted(act_threads.keys()):

		responses = numpy.array(act_threads[threads])
		response_time = numpy.mean(responses)
		gr1.SetPoint(ipoint, threads, response_time)
		ipoint += 1

	cname = "thread_response_" + fname.split('/')[2].split('.')[0]
	print cname
	c1 = ROOT.TCanvas(cname, "Canvas for plot 1", 94,162,805,341)
	drawGraphs( gr1, c1, "Response time vs threads", "Number of active threads", "Response times in ms")
	c1.cd()
	gr1.Draw("APL")
	
	#...................................................................................................

	hprof  = TProfile( 'hprof', 'Profile of pz versus px', 1000, 0, 5000, 0, 20 )

	for threads in sorted(act_threads.keys()):

		responses = numpy.array(act_threads[threads])
		response_time = numpy.mean(responses/1000.0)
		hprof.Fill(threads, response_time)
		
	cname = "thread_response_prof_" + fname.split('/')[2].split('.')[0]
	print cname
	c1 = ROOT.TCanvas(cname, "Canvas for plot 1", 94,162,805,341)
	c1.cd()
	hprof.Draw()
	
