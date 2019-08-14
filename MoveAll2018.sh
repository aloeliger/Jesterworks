#!/usr/bin/bash

hadd SMHTT2018SelectionConfigs/DY.root SMHTT2018SelectionConfigs/DY_?.root
rm SMHTT2018SelectionConfigs/DY_?.root
mv SMHTT2018SelectionConfigs/DY.root $1/DY.root
mv SMHTT2018SelectionConfigs/Data_0.root $1/Data.root
mv SMHTT2018SelectionConfigs/EWKZLL_0.root $1/EWKZLL.root
mv SMHTT2018SelectionConfigs/EWKZNuNu_0.root $1/EWKZNuNu.root
mv SMHTT2018SelectionConfigs/Embedded_0.root $1/Embedded.root
mv SMHTT2018SelectionConfigs/ST_tW_antitop_0.root $1/ST_tW_antitop.root
mv SMHTT2018SelectionConfigs/ST_tW_top_0.root $1/ST_tW_top.root
mv SMHTT2018SelectionConfigs/ST_t_antitop_0.root $1/ST_t_antitop.root
mv SMHTT2018SelectionConfigs/ST_t_top_0.root $1/ST_t_top.root
mv SMHTT2018SelectionConfigs/TTTo2L2Nu_0.root $1/TTTo2L2Nu.root
mv SMHTT2018SelectionConfigs/TTToHadronic_0.root $1/TTToHadronic.root
mv SMHTT2018SelectionConfigs/TTToSemiLeptonic_0.root $1/TTToSemiLeptonic.root
mv SMHTT2018SelectionConfigs/VBF_0.root $1/VBF.root
mv SMHTT2018SelectionConfigs/WHMinus_0.root $1/WHMinus.root
mv SMHTT2018SelectionConfigs/WHPlus_0.root $1/WHPlus.root
mv SMHTT2018SelectionConfigs/WW_0.root $1/WW.root
mv SMHTT2018SelectionConfigs/WZ_0.root $1/WZ.root
hadd SMHTT2018SelectionConfigs/W.root SMHTT2018SelectionConfigs/W_?.root
rm SMHTT2018SelectionConfigs/W_?.root
mv SMHTT2018SelectionConfigs/W.root $1/W.root
mv SMHTT2018SelectionConfigs/ZH_0.root $1/ZH.root
mv SMHTT2018SelectionConfigs/ZZ_0.root $1/ZZ.root
mv SMHTT2018SelectionConfigs/ggH_0.root $1/ggH.root
