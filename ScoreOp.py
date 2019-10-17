def ScoreOp(RequestTab):
    
    n = len(RequestTab)
    #Pertinence = float(0) # Param de la formule
    ScoreOpinion = float(0)
    #ScoreLike = int(1)
    NbrMot = int(0)
    #ScorePertinence = int(10)
    #A = float(0.6)
    #Lambda = float(0.2) 
    
    
    for i in range(0,n): # on remplit la matrice avec le score de chaque mot de la requete
    
        posscore = 0;
        negscore = 0;
        
        RQ = nltk.pos_tag(RequestTab)

        RequestWord = swn.senti_synsets(RQ[i][0],'n') # Analyse fonction

        
        for sysnt in RequestWord:
            posscore = posscore+sysnt.pos_score()
            negscore = negscore+sysnt.neg_score()
            
        if posscore - negscore != 0:
            NbrMot += 1

        ScoreOpinion = ScoreOpinion + (posscore - negscore)

    
    if NbrMot == 0: # Avoid division by 0 if there is no opinion word
        NbrMot = 1
    ScoreOpinion = ScoreOpinion / NbrMot
    #print('le score d/opinion est: ',ScoreOpinion,'\r\n')
    #Score = A*ScorePertinence + (1-A)*ScoreOpinion + Lambda * ScoreLike #Coef priority pertinence against opinion (add like score with coefficient to decrease his importance)
    #print('Le score total de la requête est: ',Score)
        
    return(ScoreOpinion)
