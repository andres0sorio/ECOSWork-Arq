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
from ROOT import TLegend
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

ndata = 0
lat_histos = []
elp_histos = []

for fname in filenames:

	act_threads  = {}
	transactions = {}
	nlines = 0
	http_error = 0

	h1name = "Latency_" + str(ndata)
	h2name = "Elapsed_" + str(ndata)
	
	h1 = ROOT.TH1F(h1name,"Latency (2.0 ms per bin)", 100, 0.0, 200.00)
	h2 = ROOT.TH1F(h2name,"Elapsed (2.0 ms per bin)", 100, 0.0, 200.00)
		
	with open(fname) as inputfile:
		
		for line in inputfile:
			
			data      = line[:-1].split(',')

			try:
				latency   = float(data[poslatency])
				elapsed   = float(data[1])
				httpcode  = int( data[2] )
				
				if httpcode == 200:
					h1.Fill(latency)
					h2.Fill(elapsed)
				else:
					http_error += 1
					
			except ValueError:
				httpcode  = -1
			nlines += 1
			
	print nlines		
	inputfile.close()

	lat_histos.append( h1 )
	elp_histos.append( h2 )

	ndata += 1

isfirst = True

legend = TLegend(0.68,0.68,0.989,0.939)

ncolor = [1,2,3,4,5,6,7,8,9,10]

c1 = ROOT.TCanvas("Combinedhistos", "Canvas for plot 1", 200,112,677,601)
c1.SetFillColor(10)
c1.SetGridy()
c1.SetLogy()
c1.cd()

ndata = 0
for h in lat_histos:
	h.SetLineColor(ncolor[ndata])
	h.SetLineWidth(2)
	dataset = "N_" + str(ndata)
	legend.AddEntry(h,dataset,"l")
	if isfirst:
		
		h.GetXaxis().SetTitle("Latency [ms]")
		h.GetYaxis().SetTitle("Samples (normalized)")
		h.DrawNormalized()
		isfirst = False
		ndata += 1
		continue

	
	h.DrawNormalized("SAME")
	ndata += 1

legend.Draw()
	
