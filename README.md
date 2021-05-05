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
HLTCfg2018MC_Mu.py        # IOFromL2 runs on muons that fail OI
HLTCfg2018MC_Mu_IOorOI.py # IOFromL2 runs independently from OI
```

## New developments:

- New type of hit-based seeds: a doublet-like seed. A seed is created only if after updating a TSOS with one compatible hit, there is another compatible hit found on the adjacent layer (going from outside in). The seed is then created using both hits. [Implementation](https://github.com/kondratyevd/CMSRun3MuonHLT/blob/23ff9cf2708aedffa480ea282d41d683ac40d3ba/TSG/TSGForOIFromL2.cc#L531). Number of doublet-like hit-based seeds to  create per L2 muon can be set with a dedicated [parameter](https://github.com/kondratyevd/CMSRun3MuonHLT/blob/23ff9cf2708aedffa480ea282d41d683ac40d3ba/Tools/HLTCfg2018MC_Mu.py#L6143).
- Hitless seeds created from different L2 trajectories are now counted by two different [parameters](https://github.com/kondratyevd/CMSRun3MuonHLT/blob/23ff9cf2708aedffa480ea282d41d683ac40d3ba/Tools/HLTCfg2018MC_Mu.py#L6145-L6146).
- Run 2 behaviors (conditions when both trajectories are used; veto on hit-based seeds in barrel) can be switched on and off with new [parameters](https://github.com/kondratyevd/CMSRun3MuonHLT/blob/23ff9cf2708aedffa480ea282d41d683ac40d3ba/Tools/HLTCfg2018MC_Mu.py#L6147-L6148).
