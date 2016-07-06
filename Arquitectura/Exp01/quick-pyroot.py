#!/usr/bin/env python

"""

"""

import ROOT
from optparse import OptionParse

#-----------------------------------------------------
parser = OptionParser()
parser.add_option("-i", type = "string", dest="input",
                  help="Input file with results", metavar="input" )

(options, args) = parser.parse_args()

if options.input is None:
        parser.error("please give an input")

#-----------------------------------------------------

filename = options.input

gr = ROOT.TGraph()
h1 = ROOT.TH1F("Exp1","Latency (0.5 ms per bin)", 100, 0.0, 50.00)

with open(filename) as inputfile:
    for line in inputfile:
        data = line[:-1].split(',')
        if data[1] != '200':
            print "reponse != 200"
        gr.SetPoint(int(data[0]), float(data[0]), float(data[2])*1000.0)
        h1.Fill( float(data[2])*1000.0)

c1 = ROOT.TCanvas("Plot1", "Canvas for plot 1", 94,162,805,341)
c1.SetFillColor(10)
c1.SetGridy()
c1.cd()

gr.SetTitle("Latency graph")
gr.GetXaxis().SetTitle("Time step")
gr.GetXaxis().CenterTitle(True)
gr.GetXaxis().SetLabelFont(42)
gr.GetXaxis().SetTitleSize(0.05)
gr.GetXaxis().SetTitleOffset(0.88)
gr.GetXaxis().SetTitleFont(42)
gr.GetYaxis().SetTitle("Latency [ms]")
gr.GetYaxis().CenterTitle(True)
gr.GetYaxis().SetLabelFont(42)
gr.GetYaxis().SetLabelSize(0.05)
gr.GetYaxis().SetTitleSize(0.05)
gr.GetYaxis().SetTitleOffset(0.91)
gr.SetMinimum(0.0)
gr.SetMaximum(10.0)
gr.SetMarkerColor(4)
gr.SetMarkerStyle(7)  
gr.Draw("AP")

gr.GetXaxis().SetRangeUser(0.0,11000)
gr.Draw("AP");
c1.Update()

c2 = ROOT.TCanvas("Plot2", "Canvas for plot 1", 385,103,607,452)
c2.SetFillColor(10)
c2.cd()

h1.SetFillColor(5)
h1.GetXaxis().SetTitle("Latency [ms]")
h1.GetXaxis().CenterTitle(True)
h1.GetXaxis().SetLabelFont(42)
h1.GetXaxis().SetLabelSize(0.035)
h1.GetXaxis().SetTitleSize(0.05)
h1.GetXaxis().SetTitleOffset(0.88)
h1.GetXaxis().SetTitleFont(42)
h1.GetYaxis().SetTitle("Sample")
h1.GetYaxis().CenterTitle(True)
h1.GetYaxis().SetLabelFont(42)
h1.GetYaxis().SetLabelSize(0.035)
h1.GetYaxis().SetTitleSize(0.05)
h1.GetYaxis().SetTitleOffset(0.98)
h1.GetYaxis().SetTitleFont(42)

h1.Draw()
  
inputfile.close()

