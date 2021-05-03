# CMS Run 3 Muon HLT
## Muon HLT developments for Run3

Based on https://github.com/JanFSchulte/muonHLTPaper_10_2_6

### Setup
```shell
cmsrel CMSSW_10_2_6
cd CMSSW_10_2_6/src
cmsenv

git cms-init
git cms-addpkg RecoMuon/TrackerSeedGenerator

git clone git@github.com:kondratyevd/CMSRun3MuonHLT.git

cp -r CMSRun3MuonHLT/TSG/* RecoMuon/TrackerSeedGenerator/plugins/

scram b -j 10
```

### Configs
Located under `CMSRun3MuonHLT/Tools/`. 

When running over CRAB, use AODSIM datasets and `useParent=True`.

```shell
# Configs
HLTCfg2018MC_Mu.py
```


