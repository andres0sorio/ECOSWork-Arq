#!/usr/bin/python

import numpy
import random
import unittest
import time
import datetime
from datetime import date
import ROOT
from optparse import OptionParser

#-----------------------------------------------------
parser = OptionParser()
parser.add_option("-i", type = "string", dest="input",
                  help="Input file with results", metavar="input" )


#parser.add_option("-o", type = "string", dest="output",
#                  help="Name of output figure", metavar="output" )

(options, args) = parser.parse_args()

if options.input is None:
        parser.error("please give an input")

#if options.output is None:
#        parser.error("please give an ouput")
#-----------------------------------------------------

infile = options.input
#outfile = options.output

t0 = datetime.datetime
ti = datetime.datetime
tlast = datetime.datetime

x = 0.0
xmax = 0.0
timeint = 1.0

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

    with open(fname) as inputfile:

        eventbin  = []
        eventbins = []
        isfirst = True
        
        for line in inputfile:

            data = line[:-1].split(',')
            latency = float(data[5])
            timestamp = float(data[0])
            ti = datetime.datetime.fromtimestamp(timestamp/1000.0)

            if isfirst:
                t0 = ti
                isfirst = False
                continue

            x = abs( ((ti - t0).seconds) + ((ti - t0).microseconds/1000000.0) )

            if x > 3600:
                continue
            
            if x > timeint:
                eventbins.append(eventbin)
                eventbin = []
                t0 = ti

            eventbin.append( latency )
            
    inputfile.close()

    ipoint = 0

    throughput = []
    
    for bin in eventbins:
        throughput.append( float(len(bin)) )
        gr.SetPoint(ipoint, ipoint + 1, float(len(bin)) )
        ipoint += 1

    th = numpy.array(throughput)

    summary.SetPoint(jpoint, jpoint+1, th.mean() )
    
    cname = fname.split('/')[1].split('.')[0]
    
    c1 = ROOT.TCanvas(cname, "Canvas for plot 1", 94,162,805,341)
    c1.SetFillColor(10)
    c1.SetGridy()
    c1.cd()

    gr.SetTitle("Throughput graph")
    gr.GetXaxis().SetTitle("Time step")
    gr.GetXaxis().CenterTitle(True)
    gr.GetXaxis().SetLabelFont(42)
    gr.GetXaxis().SetTitleSize(0.05)
    gr.GetXaxis().SetTitleOffset(0.88)
    gr.GetXaxis().SetTitleFont(42)
    gr.GetYaxis().SetTitle("Throughput [samples/sec]")
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


c1 = ROOT.TCanvas("Summary", "Canvas for plot 1", 94,162,805,341)
c1.SetFillColor(10)
c1.SetGridy()
c1.cd()

summary.SetMarkerColor(4)
summary.SetMarkerStyle(21)
summary.SetMarkerSize(0.8)
   
summary.SetTitle("Throughput graph")
summary.GetXaxis().SetTitle("Concurrent users")
summary.GetXaxis().CenterTitle(True)
summary.GetXaxis().SetLabelFont(42)
summary.GetXaxis().SetTitleSize(0.05)
summary.GetXaxis().SetTitleOffset(0.88)
summary.GetXaxis().SetTitleFont(42)
summary.GetYaxis().SetTitle("Throughput [samples/sec]")
summary.GetYaxis().CenterTitle(True)
summary.GetYaxis().SetLabelFont(42)
summary.GetYaxis().SetLabelSize(0.05)
summary.GetYaxis().SetTitleSize(0.05)
summary.GetYaxis().SetTitleOffset(0.91)
summary.SetMarkerColor(4)
summary.SetMarkerStyle(7)  
summary.Draw("AP")

