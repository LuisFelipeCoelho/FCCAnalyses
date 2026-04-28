import ROOT
from analysis_final import histoList
#import vbf_hww.analysis_config as analysis_config

# global parameters
intLumi        = 30e+06 #in pb-1
ana_tex        = 'ttHH #rightarrow 4b'
delphesVersion = '3.4.2'
energy         = 100
collider       = 'FCC-hh'
inputDir       = 'outputs/FCChh/ttHH/analysis_final/'
formats        = ['png','pdf']
yaxis          = ['log','log']
#stacksig       = ['nostack']
stacksig       = ['stack','nostack']
outdir         = 'outputs/FCChh/ttHH/analysis_final/'
plotStatUnc    = True

#variables = ['n_el','n_mu','n_lep']
variables = histoList.keys()

# rebin = [1, 1, 1, 1, 2] # uniform rebin per variable (optional)

### Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection

selections = {}
selections['ANA'] = ["sel_1L", "sel_2L"]

extralabel = {}
extralabel['sel_1L'] = "1L"
extralabel['sel_2L'] = "2L"

colors = {}
colors['tttt'] = ROOT.kRed
colors['ttbar'] = ROOT.kTeal
colors['ttH'] = ROOT.kBlue
colors['ttW'] = ROOT.kViolet
colors['ttZ'] = ROOT.kViolet-20
colors['ttZZ'] = ROOT.kGreen
colors['ttWW'] = ROOT.kGreen-20
colors['ttWZ'] = ROOT.kOrange

plots = {}
plots['ANA'] = {
        'signal':{'tttt':['mgp8_pp_tttt_5f_84TeV']},
        'backgrounds':{'ttbar':['mgp8_pp_tt_HT_200_2000_5f_84TeV','mgp8_pp_tt_HT_2000_100000_5f_84TeV'],
                    'ttH':['mgp8_pp_tth_5f_84TeV'],
                    'ttW':['mgp8_pp_ttw_5f_84TeV'],
                    'ttZ':['mgp8_pp_ttz_5f_84TeV'],
                    'ttZZ':['mgp8_pp_ttzz_5f_84TeV'],
                    'ttWW':['mgp8_pp_ttww_5f_84TeV'],
                    'ttWZ':['mgp8_pp_ttwz_5f_84TeV']}
        }

legend = {}
legend['tttt'] = 'tttt'
legend['ttbar'] = 'ttbar'
legend['ttH'] = 'ttH'
legend['ttW'] = 'ttW'
legend['ttZ'] = 'ttZ'
legend['ttZZ'] = 'ttZZ'
legend['ttWW'] = 'ttWW'
legend['ttWZ'] = 'ttWZ'
