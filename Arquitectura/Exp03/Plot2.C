{
//=========Macro generated from canvas: Plot2/Canvas for plot 1
//=========  (Tue Jun 21 04:41:11 2016) by ROOT version5.34/36
   TCanvas *Plot2 = new TCanvas("Plot2", "Canvas for plot 1",385,103,607,452);
   Plot2->SetHighLightColor(2);
   Plot2->Range(-6.25,-271.0313,56.25,2439.281);
   Plot2->SetFillColor(10);
   Plot2->SetBorderMode(0);
   Plot2->SetBorderSize(2);
   Plot2->SetFrameFillColor(0);
   Plot2->SetFrameBorderMode(0);
   Plot2->SetFrameBorderMode(0);
   
   TH1F *Exp1 = new TH1F("Exp1","Latency",100,0,50);
   Exp1->SetBinContent(4,433);
   Exp1->SetBinContent(5,2065);
   Exp1->SetBinContent(6,1690);
   Exp1->SetBinContent(7,1074);
   Exp1->SetBinContent(8,1687);
   Exp1->SetBinContent(9,1890);
   Exp1->SetBinContent(10,743);
   Exp1->SetBinContent(11,388);
   Exp1->SetBinContent(12,335);
   Exp1->SetBinContent(13,255);
   Exp1->SetBinContent(14,185);
   Exp1->SetBinContent(15,70);
   Exp1->SetBinContent(16,47);
   Exp1->SetBinContent(17,46);
   Exp1->SetBinContent(18,29);
   Exp1->SetBinContent(19,13);
   Exp1->SetBinContent(20,13);
   Exp1->SetBinContent(21,9);
   Exp1->SetBinContent(22,2);
   Exp1->SetBinContent(23,2);
   Exp1->SetBinContent(24,5);
   Exp1->SetBinContent(25,3);
   Exp1->SetBinContent(26,1);
   Exp1->SetBinContent(28,2);
   Exp1->SetBinContent(29,1);
   Exp1->SetBinContent(30,1);
   Exp1->SetBinContent(32,1);
   Exp1->SetBinContent(33,1);
   Exp1->SetBinContent(34,1);
   Exp1->SetBinContent(40,1);
   Exp1->SetBinContent(42,1);
   Exp1->SetBinContent(45,1);
   Exp1->SetBinContent(47,1);
   Exp1->SetBinContent(50,1);
   Exp1->SetBinContent(60,1);
   Exp1->SetBinContent(72,1);
   Exp1->SetBinContent(101,1);
   Exp1->SetEntries(11000);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *text = ptstats->AddText("Exp1");
   text->SetTextSize(0.0368);
   text = ptstats->AddText("Entries = 11000  ");
   text = ptstats->AddText("Mean  =  3.679");
   text = ptstats->AddText("RMS   =  1.491");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   Exp1->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(Exp1);
   Exp1->SetFillColor(5);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Exp1->SetLineColor(ci);
   Exp1->GetXaxis()->SetTitle("Latency [ms]");
   Exp1->GetXaxis()->CenterTitle(true);
   Exp1->GetXaxis()->SetLabelFont(42);
   Exp1->GetXaxis()->SetLabelSize(0.035);
   Exp1->GetXaxis()->SetTitleSize(0.05);
   Exp1->GetXaxis()->SetTitleOffset(0.88);
   Exp1->GetXaxis()->SetTitleFont(42);
   Exp1->GetYaxis()->SetTitle("Sample ");
   Exp1->GetYaxis()->CenterTitle(true);
   Exp1->GetYaxis()->SetLabelFont(42);
   Exp1->GetYaxis()->SetLabelSize(0.035);
   Exp1->GetYaxis()->SetTitleSize(0.05);
   Exp1->GetYaxis()->SetTitleOffset(0.98);
   Exp1->GetYaxis()->SetTitleFont(42);
   Exp1->GetZaxis()->SetLabelFont(42);
   Exp1->GetZaxis()->SetLabelSize(0.035);
   Exp1->GetZaxis()->SetTitleSize(0.035);
   Exp1->GetZaxis()->SetTitleFont(42);
   Exp1->Draw("");
   
   TPaveText *pt = new TPaveText(0.4247851,0.9348739,0.5752149,0.9957983,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   text = pt->AddText("Latency");
   pt->Draw();
   Plot2->Modified();
   Plot2->cd();
   Plot2->SetSelected(Plot2);
}
