import sys


from CRABClient.UserUtilities import config

config = config()

config.JobType.pluginName   = 'Analysis'
config.JobType.outputFiles  = ['muonNtuple_test_MC.root', 'DQMIO.root']

config.Data.unitsPerJob     = 100
config.Data.totalUnits      = 100000
#config.Data.splitting       = 'LumiBased'
config.Data.splitting       = 'EventAwareLumiBased'
#config.Data.splitting       = 'Automatic'

config.Data.useParent       = True #!!!!
#config.Data.useParent       = False #!!!!

config.Site.storageSite     = 'T2_US_Purdue'
config.JobType.numCores     = 1
config.JobType.maxMemoryMB  = 5000
config.JobType.allowUndistributedCMSSW = True
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

tag = "muonHLTtest_Run2_DYJets_IOorOI"
#tag = "muonHLTtest_Run2_DYJets_1HBd"
#tag = "muonHLTtest_Run2_TTToSemiLeptonic_default"
#tag = "muonHLTtest_Run2_TTTo2L2Nu_default"
#tag = "muonHLTtest_Run2_QCD_default"
#tag = "muonHLTtest_Run2_DYJets_0HB_0HBd_0HLIP_0HLMuS"

config.General.workArea   = tag
config.Data.outLFNDirBase = '/store/user/dkondrat/' + tag


config.JobType.psetName    = 'HLTCfg2018MC_Mu_IOorOI.py'
config.General.requestName = tag
config.General.transferLogs = True

config.Data.inputDataset ='/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DR-FlatPU28to62NZS_102X_upgrade2018_realistic_v15-v1/AODSIM'
#config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18DR-PUPoissonAve32_102X_upgrade2018_realistic_v15_ext2-v1/AODSIM'
#config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18DR-PUPoissonAve32_102X_upgrade2018_realistic_v15_ext2-v1/AODSIM'
#config.Data.inputDataset = '/QCD_Pt-20toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18DR-PUPoissonAve32_102X_upgrade2018_realistic_v15-v1/AODSIM'
#config.Data.inputDataset ='/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISpring18DR-NZSPU40to70_100X_upgrade2018_realistic_v10-v1/AODSIM'

#config.Data.inputDataset ='/DYJetsToMuMu_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DR-PUPoissonAve32_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW'
#config.Data.inputDataset ='/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-FlatPU28to62NZS_102X_upgrade2018_realistic_v15-v1/MINIAODSIM'

#config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'

config.Data.outputDatasetTag   = tag

