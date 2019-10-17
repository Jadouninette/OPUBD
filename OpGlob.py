# -*- coding: utf-8 -*-

def OpGlob(ScoreTotal, PertinenceSorted,nbMot):#récupère le score total 
    A = float(0.6)
    Lambda = float(0.2) 
    Score= float(0)
    Score = A*PertinenceSorted + (1-A)*ScoreTotal+ Lambda
    Score = 2*Score/nbMot
    return (Score)