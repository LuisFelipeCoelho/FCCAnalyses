#Mandatory: List of processes
processList = {
    'mgp8_pp_tt_HT_200_2000_5f_84TeV':{},
    'mgp8_pp_tt_HT_2000_100000_5f_84TeV':{},
    'mgp8_pp_tth_5f_84TeV':{},
    'mgp8_pp_tttt_5f_84TeV':{},
    'mgp8_pp_ttw_5f_84TeV':{},
    'mgp8_pp_ttww_5f_84TeV':{},
    'mgp8_pp_ttwz_5f_84TeV':{},
    'mgp8_pp_ttz_5f_84TeV':{},
    'mgp8_pp_ttzz_5f_84TeV':{},
    }

###Input directory where the files produced at the pre-selection level are
inputDir   = "outputs/FCChh/ttHH/"
outputDir  = "outputs/FCChh/ttHH/analysis_final/"

###Link to the dictonary that contains all the cross section informations etc...
#procDict = "FCCee_procDict_fcc_tmp.json"
procDict = '/eos/experiment/fcc/hh/utils/FCCDicts/FCChh_procDict_fcc_v07_II.json'
#How to add a process that is not in the official dictionary:
#procDictAdd={
#"mgp8_pp_tthh_lambda100_5f": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.1164, "kfactor": 1.0, "matchingEfficiency": 1.0},
#}

# Expected integrated luminosity
intLumi = 30e+06  # pb-1

# Whether to scale to expected integrated luminosity
doScale = True

#Number of CPUs to use
#nCPUS = 2

#produces ROOT TTrees, default is False
doTree = True

saveTabular = True

# Optional: Use weighted events
do_weighted = True 

# Define new variables
defineList = {
    "n_lep" : "n_el+n_mu",
}

cutList = {"sel_1L": "n_lep == 1",
           "sel_2L": "n_lep == 2"}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
  "b1_pT":{"name":"b1_pt","title":"pT_{b1} [GeV]","bin":50,"xmin":0.,"xmax":200.},
  "b2_pT":{"name":"b2_pt","title":"pT_{b2} [GeV]","bin":50,"xmin":0.,"xmax":200.},
  "b3_pT":{"name":"b3_pt","title":"pT_{b3} [GeV]","bin":50,"xmin":0.,"xmax":200.},
  "n_jets" : {"name":"n_jets","title":"Number Jets","bin":10,"xmin":0,"xmax":10},
  "n_lep" : {"name":"n_lep","title":"Number Leptons","bin":10,"xmin":0,"xmax":10},
  "n_bjets_loose" : {"name":"n_bjets_loose","title":"Number loose b-jets","bin":10,"xmin":0,"xmax":10},
  "n_bjets_medium" : {"name":"n_bjets_medium","title":"Number medium b-jets","bin":10,"xmin":0,"xmax":10},
  "MET" : {"name":"MET","title":"MET","bin":40,"xmin":0,"xmax":1000},
  "el1_pt" : {"name":"el1_pt","title":"Leading Electron pT","bin":40,"xmin":0,"xmax":200},
  "mu1_pt" : {"name":"mu1_pt","title":"Leading Muon pT","bin":40,"xmin":0,"xmax":200},
}
