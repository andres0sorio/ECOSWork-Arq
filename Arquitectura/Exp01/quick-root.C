{

  /*
    
    
    this is script reads 1 column data

   */

  ifstream in;

  gStyle->SetOptStat(0);

  in.open("experiment-latency-1.dat");
  
  double time;
  int np = 0; 
  int ndataset = 0;
  double xx;
  int pindex = 0;
  
  TH1D * histos[15]; //we need approx. 15 TGraphs (1 per dataset)
  
  histos[0] = new TH1D("Exp1","Latency histogram(s)",100, 0.0, 0.100);
  histos[1] = new TH1D("Exp2","Nginx balancer Latency",100, 0.0, 0.100);
  
  while ( in.good() ) 
  {
    in >> xx;
    histos[0]->Fill(xx);
    ++pindex;
    
  }
  
  std::cout << "Total dataset read " << pindex << " " << std::endl;

  in.close();
  in.open("experiment-latency-2.dat");
  
  pindex = 0;
  
  while ( in.good() ) 
  {
    
    in >> xx;
    histos[1]->Fill(xx);
    ++pindex;
    
  }
  std::cout << "Total dataset read " << pindex << " " << std::endl;
  
  in.close();
  
  TCanvas * canvas = new TCanvas("Plot1", "Canvas for plot 1", 94, 262,700, 502 );
  canvas->SetFillColor(10);
  
  //Important set log scale on both axis
  //canvas->SetLogx();
  //canvas->SetLogy();
  
  canvas->cd();
  
  histos[0]->GetXaxis()->SetTitle("Latency [1 ms per bin]");
  histos[0]->GetXaxis()->CenterTitle(true);
  histos[0]->GetXaxis()->SetLabelFont(42);
  histos[0]->GetXaxis()->SetLabelSize(0.035);
  histos[0]->GetXaxis()->SetTitleSize(0.035);
  histos[0]->GetXaxis()->SetTitleFont(42);
  histos[0]->GetYaxis()->SetTitle("Samples");
  histos[0]->GetYaxis()->CenterTitle(true);
  histos[0]->GetYaxis()->SetLabelFont(42);
  histos[0]->GetYaxis()->SetLabelSize(0.035);
  histos[0]->GetYaxis()->SetTitleSize(0.035);
  histos[0]->GetYaxis()->SetTitleFont(42);

  histos[0]->SetFillColor(5);
  histos[0]->Draw();

  histos[1]->SetFillColor(38);
  histos[1]->Draw("SAME");
  
  TLegend * legend = new TLegend(0.72,0.70,0.96,0.89,NULL,"brNDC");
  legend->AddEntry (histos[0], "Local", "f" );
  legend->AddEntry (histos[1], "Nginx (Rpi)", "f" );
  
  legend->Draw();
    

}

