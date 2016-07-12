#!/usr/bin/python

import unittest
import time
import datetime
from datetime import date
import ROOT
from optparse import OptionParser
from ROOT import TTimeStamp
from ROOT import TDatime
from ROOT import TLegend

#-----------------------------------------------------
parser = OptionParser()
parser.add_option("-i", type = "string", dest="input",
                  help="Input file with results", metavar="input" )

(options, args) = parser.parse_args()

if options.input is None:
        parser.error("please give an input")

#-----------------------------------------------------

infile = options.input

filenames = infile.split(',')

summary = ROOT.TGraph()

graphs = []

for fname in filenames:

	gr = ROOT.TGraph()
	npoint = 0
	with open(fname) as inputfile:
		for line in inputfile:
			
			data = line[:-1].split(',')
			x1 = float(data[0])
			y1 = float(data[1])
			print x1, y1
			gr.SetPoint(npoint, x1, y1)
			npoint += 1
	
	inputfile.close()
	graphs.append(gr)

c1 = ROOT.TCanvas("Summary", "Canvas for plot 1", 180,202,657,434)
c1.SetFillColor(10)
c1.SetGridy()
c1.cd()

npoint = 0
legend = TLegend(0.1603053,0.7083333,0.3832061,0.8651961)

markers_colors = [2,2,4]
markers_style  = [4,4,21]
labels = ["box0 (Exp 1)","box0 (Exp 1)","Balancer"]

for gr in graphs:
        
	gr.SetMarkerColor(markers_colors[npoint])
	gr.SetMarkerStyle(markers_style[npoint])
	gr.SetMarkerSize(1.0)
	
	gr.SetTitle("Throughput - Concurrent users expected in 10 s")
	gr.GetXaxis().SetTitle("Concurrent users")

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

	if npoint == 0:
		gr.Draw("APL")
	else:
                gr.Draw("PL")
                
        legend.AddEntry(gr,labels[npoint],"p")
 	npoint += 1
	
legend.Draw()
