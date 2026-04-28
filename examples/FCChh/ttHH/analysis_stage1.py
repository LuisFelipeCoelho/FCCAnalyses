from argparse import ArgumentParser

# Additional/custom C++ functions, defined in header files
includePaths = ["functions.h"]
include_paths = ["functions.h"]

# Mandatory: Analysis class where the user defines the operations on the
# dataframe.
class Analysis():
    def __init__(self, cmdline_args):
        parser = ArgumentParser(
            description='Additional analysis arguments',
            usage='Provide additional arguments after analysis script path')
        # Parse additional arguments not known to the FCCAnalyses parsers
        # All command line arguments know to fccanalysis are provided in the
        # `cmdline_arg` dictionary.
        self.ana_args, _ = parser.parse_known_args(cmdline_args['unknown'])

        # Mandatory: List of samples (processes) used in the analysis
        self.process_list = {
            # Run over the full statistics and save it to one output file named
            # <outputDir>/<process_name>.root
           #"mgp8_pp_tt_HT_200_2000_5f_84TeV": {'fraction': 1},
           #"mgp8_pp_tt_HT_2000_100000_5f_84TeV": {'fraction': 1},

           # "mgp8_pp_tt_HT_317_502_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tt_HT_502_796_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tt_HT_796_1262_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tt_HT_1262_2000_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tt_HT_2000_3170_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tt_HT_3170_5024_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tt_HT_5024_7962_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tt_HT_7962_12619_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tt_HT_12619_20000_5f_84TeV": {'fraction': 1},

           # #"mgp8_pp_tth_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tttt_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_ttw_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_ttwz_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_ttww_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_ttz_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_ttzz_5f_84TeV": {'fraction': 1},

           # "mgp8_pp_jj_HT_200_2000_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_jj_HT_2000_100000_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_tWZj_5f_84TeV_zee": {'fraction': 1},
           # "mgp8_pp_tZj_5f_84TeV_zeewlep": {'fraction': 1},
           # "mgp8_pp_ww_HT_200_2000_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_ww_HT_2000_100000_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_zz_HT_200_2000_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_zz_HT_2000_100000_5f_84TeV": {'fraction': 1},
           # "mgp8_pp_zjj_4f_84TeV": {'fraction': 1},

           #"mg_ph8_ttHH_1L_82TeV_edm4hep": {'fraction': 1},
           "mg_ph8_ttHH_inclusive_82TeV_edm4hep": {'fraction': 1},
        }

        # Mandatory: Production tag when running over the centrally produced
        # samples (this points to the yaml file for getting sample statistics)
        # self.prod_tag = 'FCCee/spring2021/IDEA/'
        # or Input directory when not running over the centrally produced
        # samples.
        #self.input_dir = "/eos/experiment/fcc/hh/generation/DelphesEvents/fcc_v07/II/"
        self.input_dir = '/eos/home-l/lfaldaul/FCC_samples/Delphes/'

        # Optional: output directory, default is local running directory
        self.output_dir = 'outputs/FCChh/ttHH/'

        # Optional: Use weighted events
        #self.do_weighted = True 

        # Optional: analysis name, default is ''
        # self.analysis_name = 'My Analysis'

        # Optional: number of threads to run on, default is 'all available'
        # self.n_threads = 4

        # Optional: running on HTCondor, default is False
        # self.run_batch = False


    # Mandatory: analyzers function to define the analysis graph, please make
    # sure you return the dataframe, in this example it is dframe2
    def analyzers(self, dframe):
        '''
        Analysis graph.
        '''

        dframe2 = (
            dframe

            #.Alias("MCRecoAssociations1", "MCRecoAssociations")

            # generator event weight
            #.Define("weight",  "EventHeader.weight")

            ## ============  Leptons ============ ###

           .Define("electrons",  "FCCAnalyses::ReconstructedParticle::get(Electron_objIdx.index, ReconstructedParticles)")
           .Define("selpt_el",   "FCCAnalyses::ReconstructedParticle::sel_pt(10.)(electrons)")
           .Define("sel_el_unsort", "FCCAnalyses::ReconstructedParticle::sel_eta(4)(selpt_el)")
           .Define("sel_el",  "AnalysisFCChh::SortParticleCollection(sel_el_unsort)") #sort by pT

           .Define("n_el",  "FCCAnalyses::ReconstructedParticle::get_n(sel_el)")
           .Define("el1_e",  "FCCAnalyses::ReconstructedParticle::get_e(sel_el)[0]")
           .Define("el1_pt",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_el)[0]")
           .Define("el1_eta",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_el)[0]")
           .Define("el1_phi",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_el)[0]")
           .Define("el1_q",  "FCCAnalyses::ReconstructedParticle::get_charge(sel_el)[0]")
           # .Define("el2_e",  "FCCAnalyses::ReconstructedParticle::get_e(sel_el)[1]")
           # .Define("el2_pt",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_el)[1]")
           # .Define("el2_eta",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_el)[1]")
           # .Define("el2_phi",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_el)[1]")

           .Define("muons",  "FCCAnalyses::ReconstructedParticle::get(Muon_objIdx.index, ReconstructedParticles)")
           .Define("selpt_mu",   "FCCAnalyses::ReconstructedParticle::sel_pt(10.)(muons)")
           .Define("sel_mu_unsort", "FCCAnalyses::ReconstructedParticle::sel_eta(4)(selpt_mu)")
           .Define("sel_mu",  "AnalysisFCChh::SortParticleCollection(sel_mu_unsort)") #sort by pT

           .Define("n_mu",  "FCCAnalyses::ReconstructedParticle::get_n(sel_mu)")
           .Define("mu1_e",  "FCCAnalyses::ReconstructedParticle::get_e(sel_mu)[0]")
           .Define("mu1_pt",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_mu)[0]")
           .Define("mu1_eta",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_mu)[0]")
           .Define("mu1_phi",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_mu)[0]")
           .Define("mu1_q",  "FCCAnalyses::ReconstructedParticle::get_charge(sel_mu)[0]")
           # .Define("mu2_e",  "FCCAnalyses::ReconstructedParticle::get_e(sel_mu)[1]")
           # .Define("mu2_pt",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_mu)[1]")
           # .Define("mu2_eta",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_mu)[1]")
           # .Define("mu2_phi",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_mu)[1]")

           #.Filter("n_mu+n_el == 1")

           .Define("nLeptons", "n_mu+n_el")
           .Define("Lep_pt", "mu1_pt+el1_pt")
           .Define("Lep_eta", "mu1_eta+el1_eta")
           .Define("Lep_phi", "mu1_phi+el1_phi")
           .Define("Lep_e", "mu1_e+el1_e")
           .Define("Lep_q", "mu1_q+el1_q")

           # ### ============= Jets ============ ###

           # cluster all reconstructed particles
           .Define("RP_px", "FCCAnalyses::ReconstructedParticle::get_px(ReconstructedParticles)")
           .Define("RP_py", "FCCAnalyses::ReconstructedParticle::get_py(ReconstructedParticles)")
           .Define("RP_pz", "FCCAnalyses::ReconstructedParticle::get_pz(ReconstructedParticles)")
           .Define("RP_e",  "FCCAnalyses::ReconstructedParticle::get_e(ReconstructedParticles)")
           .Define("RP_m",  "FCCAnalyses::ReconstructedParticle::get_mass(ReconstructedParticles)")
           .Define("RP_q",  "FCCAnalyses::ReconstructedParticle::get_charge(ReconstructedParticles)")
           .Define("RP_no",  "FCCAnalyses::ReconstructedParticle::get_n(ReconstructedParticles)")
           .Define("pseudo_jets", "FCCAnalyses::JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)")
           # https://github.com/HEP-FCC/FCCAnalyses/blob/master/addons/FastJet/src/JetClustering.cc
           .Define("clustered_jets", "JetClustering::clustering_antikt(0.5, 0, 20., 0, 0)(pseudo_jets)")
           .Define("jets", "FCCAnalyses::JetClusteringUtils::get_pseudoJets(clustered_jets)")
           .Define("jetconstituents", "FCCAnalyses::JetClusteringUtils::get_constituents(clustered_jets)") # one-to-one mapping to reconstructedparticles
           .Define("jets_pt", "FCCAnalyses::JetClusteringUtils::get_pt(jets)")
           .Define("jets_eta", "FCCAnalyses::JetClusteringUtils::get_eta(jets)")
           .Define("jets_phi", "FCCAnalyses::JetClusteringUtils::get_phi(jets)")
           .Define("jets_e", "FCCAnalyses::JetClusteringUtils::get_e(jets)")
           .Define("jets_truth", "FCCAnalyses::ttHHfunctions::jetTruthFinder(jetconstituents, ReconstructedParticles, Particle)")
           .Define("n_jets",   "jets_pt.size()")
           .Define("HT", "ROOT::VecOps::Sum(jets_pt)") # scalar sum of pT (HT)

           .Filter("n_jets > 4")
           .Filter("HT+mu1_pt+el1_pt > 400")

           .Define("jets_flavour",   "JetTaggingUtils::get_flavour(jets, Particle)")
           .Define("jets_btag_85",      "JetTaggingUtils::get_btag(jets_flavour, 0.85)")
           .Define("jets_btag_77",      "JetTaggingUtils::get_btag(jets_flavour, 0.77)")
           .Define("jets_btag_70",      "JetTaggingUtils::get_btag(jets_flavour, 0.70)")
           .Define("jets_btag_60",      "JetTaggingUtils::get_btag(jets_flavour, 0.60)")

           .Define("jet1_pt", "jets_pt[0]")
           .Define("jet1_eta", "jets_eta[0]")
           .Define("jet1_phi", "jets_phi[0]")
           .Define("jet1_e", "jets_e[0]")
           .Define("jet1_pcbt", "jets_btag_85[0]+jets_btag_77[0]+jets_btag_70[0]+jets_btag_60[0]")
           .Define("jet1_truthLabel", "jets_truth[0]")

           .Define("jet2_pt", "jets_pt[1]")
           .Define("jet2_eta", "jets_eta[1]")
           .Define("jet2_phi", "jets_phi[1]")
           .Define("jet2_e", "jets_e[1]")
           .Define("jet2_pcbt", "jets_btag_85[1]+jets_btag_77[1]+jets_btag_70[1]+jets_btag_60[1]")
           .Define("jet2_truthLabel", "jets_truth[1]")
           
           .Define("jet3_pt", "jets_pt[2]")
           .Define("jet3_eta", "jets_eta[2]")
           .Define("jet3_phi", "jets_phi[2]")
           .Define("jet3_e", "jets_e[2]")
           .Define("jet3_pcbt", "jets_btag_85[2]+jets_btag_77[2]+jets_btag_70[2]+jets_btag_60[2]")
           .Define("jet3_truthLabel", "jets_truth[2]")
           
           .Define("jet4_pt", "jets_pt[3]")
           .Define("jet4_eta", "jets_eta[3]")
           .Define("jet4_phi", "jets_phi[3]")
           .Define("jet4_e", "jets_e[3]")
           .Define("jet4_pcbt", "jets_btag_85[3]+jets_btag_77[3]+jets_btag_70[3]+jets_btag_60[3]")
           .Define("jet4_truthLabel", "jets_truth[3]")
           
           .Define("jet5_pt", "jets_pt[4]")
           .Define("jet5_eta", "jets_eta[4]")
           .Define("jet5_phi", "jets_phi[4]")
           .Define("jet5_e", "jets_e[4]")
           .Define("jet5_pcbt", "jets_btag_85[4]+jets_btag_77[4]+jets_btag_70[4]+jets_btag_60[4]")
           .Define("jet5_truthLabel", "jets_truth[4]")
           
           .Define("jet6_pt", "jets_pt[5]")
           .Define("jet6_eta", "jets_eta[5]")
           .Define("jet6_phi", "jets_phi[5]")
           .Define("jet6_e", "jets_e[5]")
           .Define("jet6_pcbt", "jets_btag_85[5]+jets_btag_77[5]+jets_btag_70[5]+jets_btag_60[5]")
           .Define("jet6_truthLabel", "jets_truth[5]")

           .Define("n_bjets_85", "ROOT::VecOps::Sum(jets_btag_85)")
           .Define("n_bjets_77", "ROOT::VecOps::Sum(jets_btag_77)")

           ### ============= MET ============ ###

           .Define("MET", "FCCAnalyses::ReconstructedParticle::get_pt(MissingET)[0]") #absolute value of MET
           .Define("MET_phi", "FCCAnalyses::ReconstructedParticle::get_phi(MissingET)[0]") #angle of MET

           .Filter("n_bjets_85>=3")
        )

        return dframe2

    # Mandatory: output function, please make sure you return the branch list
    # as a python list
    def output(self):
        '''
        Output variables which will be saved to output root file.
        '''
        branch_list = [
                # Event weights and basic info
                #'weight',
            
                # Electrons
                'n_el', 'el1_pt', 'el1_eta', 'el1_phi', 'el1_e',
            
                # Muons
                'n_mu', 'mu1_pt', 'mu1_eta', 'mu1_phi', 'mu1_e', 
            
                # Lepton
                'nLeptons', 'Lep_pt', 'Lep_eta', 'Lep_phi', 'Lep_e', 'Lep_q',

                # Missing energy
                'MET', 'MET_phi', 
            
                # Jet energy sums
                'HT',
            
                # Jet counts
                'n_jets', 'n_bjets_85', 'n_bjets_77',
            
                # Individual jets (3rd-6th jets)
                'jet1_pt', 'jet1_eta', 'jet1_phi', 'jet1_e', 'jet1_pcbt', 'jet1_truthLabel',
                'jet2_pt', 'jet2_eta', 'jet2_phi', 'jet2_e', 'jet2_pcbt', 'jet2_truthLabel',
                'jet3_pt', 'jet3_eta', 'jet3_phi', 'jet3_e', 'jet3_pcbt', 'jet3_truthLabel',
                'jet4_pt', 'jet4_eta', 'jet4_phi', 'jet4_e', 'jet4_pcbt', 'jet4_truthLabel',
                'jet5_pt', 'jet5_eta', 'jet5_phi', 'jet5_e', 'jet5_pcbt', 'jet5_truthLabel',
                'jet6_pt', 'jet6_eta', 'jet6_phi', 'jet6_e', 'jet6_pcbt', 'jet6_truthLabel',
        ]
        return branch_list


