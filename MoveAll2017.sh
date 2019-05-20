#!/usr/bin/bash

hadd SMHTT2017SelectionConfigs/DY.root SMHTT2017SelectionConfigs/DY_?.root
rm SMHTT2017SelectionConfigs/DY_?.root
mv SMHTT2017SelectionConfigs/DY.root $1/DY.root
mv SMHTT2017SelectionConfigs/Data_0.root $1/Data.root
mv SMHTT2017SelectionConfigs/EWKZLL_0.root $1/EWKZLL.root
mv SMHTT2017SelectionConfigs/EWKZNuNu_0.root $1/EWKZNuNu.root
mv SMHTT2017SelectionConfigs/Embedded_0.root $1/Embedded.root
mv SMHTT2017SelectionConfigs/ST_tW_antitop_0.root $1/ST_tW_antitop.root
mv SMHTT2017SelectionConfigs/ST_tW_top_0.root $1/ST_tW_top.root
mv SMHTT2017SelectionConfigs/ST_t_antitop_0.root $1/ST_t_antitop.root
mv SMHTT2017SelectionConfigs/ST_t_top_0.root $1/ST_t_top.root
mv SMHTT2017SelectionConfigs/TTTo2L2Nu_0.root $1/TTTo2L2Nu.root
mv SMHTT2017SelectionConfigs/TTToHadronic_0.root $1/TTToHadronic.root
mv SMHTT2017SelectionConfigs/TTToSemiLeptonic_0.root $1/TTToSemiLeptonic.root
mv SMHTT2017SelectionConfigs/VBF_0.root $1/VBF.root
mv SMHTT2017SelectionConfigs/WHMinus_0.root $1/WHMinus.root
mv SMHTT2017SelectionConfigs/WHPlus_0.root $1/WHPlus.root
mv SMHTT2017SelectionConfigs/WW_0.root $1/WW.root
mv SMHTT2017SelectionConfigs/WZ_0.root $1/WZ.root
hadd SMHTT2017SelectionConfigs/W.root SMHTT2017SelectionConfigs/W_?.root
rm SMHTT2017SelectionConfigs/W_?.root
mv SMHTT2017SelectionConfigs/W.root $1/W.root
mv SMHTT2017SelectionConfigs/ZH_0.root $1/ZH.root
mv SMHTT2017SelectionConfigs/ZZ_0.root $1/ZZ.root
mv SMHTT2017SelectionConfigs/ggH_0.root $1/ggH.root