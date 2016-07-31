{

  /*
    
    this is script reads 1 column data
    
   */

  ifstream in;

  gStyle->SetOptStat(0);

  in.open("data/08-07-2016/experiment-latency.dat");
  
  double xtime;
  int np = 0; 
  int ndataset = 0;
  double xx;
  int pindex = 0;
  
  TH1D * histos[15]; //we need approx. 15 TGraphs (1 per dataset)
  
  histos[0] = new TH1D("Exp1","Sending POST requests to our Test Application"  ,100, 0.0, 100);
  histos[1] = new TH1D("Exp2","Nginx balancer Latency",100, 0.0, 100);
  histos[2] = new TH1D("Exp3","Nginx balancer Latency",100, 0.0, 100);
  
  while ( in.good() ) 
  {
    in >> xx;
    histos[0]->Fill(xx*1000.0);
    ++pindex;
    
  }
  
  std::cout << "Total dataset read " << pindex << " " << std::endl;

  in.close();
  in.open("data/08-07-2016/experiment-latency-box0.dat");
  
  pindex = 0;
  
  while ( in.good() ) 
  {
    
    in >> xx;
    histos[1]->Fill(xx*1000.0);
    ++pindex;
    
  }
  std::cout << "Total dataset read " << pindex << " " << std::endl;
  
  in.close();
  
  in.open("data/08-07-2016-SSL/experiment-latency-ssl.dat");
  
  pindex = 0;
  
  while ( in.good() ) 
  {
    
    in >> xx;
    histos[2]->Fill(xx*1000.0);
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
  histos[2]->SetFillColor(4);

  histos[1]->Draw("SAME");
  histos[2]->Draw("SAME");
  
  TLegend * legend = new TLegend(0.72,0.70,0.96,0.89,NULL,"brNDC");
  legend->AddEntry (histos[0], "Direct", "f" );
  legend->AddEntry (histos[1], "Balancer", "f" );
  legend->AddEntry (histos[2], "Balancer+SSL", "f" );
  
  legend->Draw();

  std::cout << histos[0]->GetStdDev() << histos[0]->GetStdDevError() << std::endl;
  std::cout << histos[1]->GetStdDev() << histos[1]->GetStdDevError() << std::endl;
  std::cout << histos[2]->GetStdDev() << histos[2]->GetStdDevError() << std::endl;
  
  canvas->Print("Latency_plot_exps_SSL.png");
  

}

