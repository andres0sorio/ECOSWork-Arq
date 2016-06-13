{
  ifstream in;
  
  in.open("experiment1-latency.dat"); //this file contains all of your data
  
  std::string header[6]; //each data set has a header part (x, y, xelow, xeup, yelow, yeup)
  
  double time; //this we keep
  
  int np = 0; //good np is going to be the number of points per dataset
  int ndataset = 0;
  
  TH1D * histos[15]; //we need approx. 15 TGraphs (1 per dataset)

  histos[0] = new TH1D("Exp1","Latency",100, 0.0, 0.020);
  
  double xx;
  
  while ( in.good() ) 
  {
    
    int pindex = 0;
    
    in >> xx;
    histos[0]->Fill(xx);
    
    ++pindex;
    
  }
  
  std::cout << "Total dataset read " << pindex << " " << std::endl;
  
  //Plot each Dataset on a sigle Canvas (all combined)
  
  TCanvas * canvas = new TCanvas("Plot1", "Canvas for plot 1", 94, 262,700, 502 );
  canvas->SetFillColor(10);

  //Important set log scale on both axis
  //canvas->SetLogx();
  //canvas->SetLogy();
  
  //Datasets options (Markers: style, color, size) : You can also do it by hand using the interactive Editor
  int style[15];
  int color[15];
  float size[15];
  
  //For dataset No1
  style[0] = 22;
  color[0] = 2;
  size[0]  = 1.0;
  
  //For dataset No2
  style[1] = 25;
  color[1] = 4;
  size[1]  = 1.0;

  //For dataset No3
  style[2] = 24;
  color[2] = 3;
  size[2]  = 1.0;

  canvas->cd();
  
  histos[0]->Draw();
  
  in.close();
  
}

// .q (quit)
//.x graph-tuto.C
