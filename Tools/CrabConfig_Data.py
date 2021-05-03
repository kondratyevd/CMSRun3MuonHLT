import sys


from CRABClient.UserUtilities import config

config = config()

config.JobType.pluginName   = 'Analysis'
config.JobType.outputFiles  = ['muonNtuple.root']#, 'DQMIO.root']muonNtupleDataIOIter2.root

config.Data.unitsPerJob     = 50
#config.Data.totalUnits      = 500000
config.Data.splitting       = 'LumiBased'
#config.Data.splitting       = 'Automatic'

config.Data.useParent       = True #!!!!
#config.Data.useParent       = False #!!!!

config.Site.storageSite     = 'T2_US_Purdue'
config.JobType.numCores     = 1
config.JobType.maxMemoryMB  = 2500
config.JobType.allowUndistributedCMSSW = True

#config.Data.lumiMask ='https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
#config.Data.lumiMask ='https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
#config.Data.lumiMask ='/afs/cern.ch/user/k/kplee/public/MuonTriggerPaper/JSON/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON_Last5invfb.txt'

config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'


from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

tag = "muonHLTtest_Run2_SingleMuonD_default"



config.General.workArea   = tag
config.Data.outLFNDirBase = '/store/user/dkondrat/' + tag



config.JobType.psetName    = 'HLTCfg2018Data_Mu_test.py'

config.General.requestName = tag

#config.Data.inputDataset = '/SingleMuon/Run2018B-17Sep2018-v1/AOD'
config.Data.inputDataset = '/SingleMuon/Run2018D-12Nov2019_UL2018-v4/AOD'

config.Data.outputDatasetTag   = tag
