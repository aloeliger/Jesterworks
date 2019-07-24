#!/usr/bin/bash

hadd SMHTT2016SelectionConfigs/DY.root SMHTT2016SelectionConfigs/DY_?.root
rm SMHTT2016SelectionConfigs/DY_?.root
mv SMHTT2016SelectionConfigs/DY.root $1/DY.root
mv SMHTT2016SelectionConfigs/Data_0.root $1/Data.root
mv SMHTT2016SelectionConfigs/EWKZLL_0.root $1/EWKZLL.root
mv SMHTT2016SelectionConfigs/EWKZNuNu_0.root $1/EWKZNuNu.root
mv SMHTT2016SelectionConfigs/ST_tW_antitop_0.root $1/ST_tW_antitop.root
mv SMHTT2016SelectionConfigs/ST_tW_top_0.root $1/ST_tW_top.root
mv SMHTT2016SelectionConfigs/ST_t_antitop_0.root $1/ST_t_antitop.root
mv SMHTT2016SelectionConfigs/ST_t_top_0.root $1/ST_t_top.root
mv SMHTT2016SelectionConfigs/TT_0.root $1/TT.root
mv SMHTT2016SelectionConfigs/VBF_0.root $1/VBF.root
mv SMHTT2016SelectionConfigs/WHMinus_0.root $1/WHMinus.root
mv SMHTT2016SelectionConfigs/WHPlus_0.root $1/WHPlus.root
mv SMHTT2016SelectionConfigs/WW1L1Nu2Q_0.root $1/WW1L1Nu2Q.root
mv SMHTT2016SelectionConfigs/WZ2L2Q_0.root $1/WZ2L2Q.root
mv SMHTT2016SelectionConfigs/WZJLLLNu_0.root $1/WZJLLLNu.root
hadd SMHTT2016SelectionConfigs/W.root SMHTT2016SelectionConfigs/W_?.root
rm SMHTT2016SelectionConfigs/W_?.root
mv SMHTT2016SelectionConfigs/W.root $1/W.root
mv SMHTT2016SelectionConfigs/ZH_0.root $1/ZH.root
mv SMHTT2016SelectionConfigs/ZZ4L_0.root $1/ZZ4L.root
mv SMHTT2016SelectionConfigs/ggH_0.root $1/ggH.root
