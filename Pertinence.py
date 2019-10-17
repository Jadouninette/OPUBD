def Pertinence(Corpus,Request):
    
    PertiGlob = [] # Score for the pertinence of every file
    Words = set(nltk.corpus.words.words())
    
    ScoreTotal = [0]*len(Corpus)
    ScoreParMot = 0
    
    Length = []
    
    RQ = nltk.pos_tag(Request) # Compare each word and see if it's a noun, verb, adj, adv....
    print("La requete tokenizée (avec les caractéristiques) saisie ",end='')
    print(" est: ",end='')
    print(RQ) # Print the request with the characteritsic of each word
    print("""\n""")

    for Q in range(len(RQ)): # Loop, to transform, plural into singular and verbs into infinitves verbs in the request
            if RQ[Q][1] == 'VBP':
                Request[Q] = wnl.lemmatize(Request[Q],pos='v')
            if RQ[Q][1] == 'VBZ':
                Request[Q] = wnl.lemmatize(Request[Q],pos='v')
            if RQ[Q][1] == 'NNS':
                Request[Q] = wnl.lemmatize(Request[Q])
            if RQ[Q][1] == 'NN':
                Request[Q] = wnl.lemmatize(Request[Q])
                
    Affichage = [[[0]*len(Request)]*3]*(len(Corpus))

    for NbrText in range(len(Corpus)): # Main loop, to calculate the occurence of each word of the request in every file
        
        print ("-------------------------------------")
        print ("Le Texte étudié est le numéro ",end='')
        print (NbrText+1)
        
        File = open(Corpus[NbrText],"r",encoding='utf8') # Open the file X (X represents the value of the loop)
        Texte = File.read()
        print("Le texte extrait du fichier numéro ",end='')
        print(NbrText+1,end='')
        print(" est: ",end='')
        print(Texte) # Print the file
        print("""\n""")
    
        File.close()

        
        Texte = Texte.lower() # The text is now into lowercase letters
        unwanted ={'.',',','?','!','(',')','\n','<','>','//','@',':',';','“','[',']','{','}'}

        Chaine = nltk.word_tokenize(Texte)
        Chaine = [i for i in Chaine if i not in unwanted]
        print("La chaine tokenizée et en minuscules, sans ponctuation du fichier numéro ",end='')
        print(NbrText+1,end='')
        print(" est: ",end='')
        print(Chaine) # Print the file tokenized
        print("""\n""")

        Comment = nltk.pos_tag(Chaine)

        for P in range(len(Comment)):  # Loop, to transform, plural into singular and verbs into infinitves verbs in the file
            if Comment[P][1] == 'NN':
                Chaine[P] = wnl.lemmatize(Chaine[P])
            if Comment[P][1] == 'NNS':
                Chaine[P] = wnl.lemmatize(Chaine[P])
            if Comment[P][1] == 'VBP':
                Chaine[P] = wnl.lemmatize(Chaine[P],pos='v')
            if Comment[P][1] == 'VBZ':
                Chaine[P] = wnl.lemmatize(Chaine[P],pos='v')
            if Comment[P][1] == 'VBG':
                Chaine[P] = wnl.lemmatize(Chaine[P],pos='v')
            if Comment[P][1] == 'VBD':
                Chaine[P] = wnl.lemmatize(Chaine[P],pos='v')
            if Comment[P][1] == '':
                Chaine.remove(Chaine[P])

        Comment = nltk.pos_tag(Chaine)
        
        Length.append(len(Chaine))
        
        Pertinence = 0 # Total of occurences
        Indx = []
        Counter = [0 for x in range(len(Request))] # Counter for occurence of each word in the file
        CounterMatrix = []
        IndexTotal = [[0 for x in range(4)] for y in range(len(Request))]
        
        for i in range(len(Request)):
            R = Request[i] # Select a word of the request
            IndexTotal[i][0] = Corpus[NbrText]
            IndexTotal[i][1] = R
            IndexTotal[i][3] = 0
            IndexTotal [i][2] = []
            for l in range(0,len(Chaine)):
                if R == Chaine[l]:
                    Counter[i] = Counter[i] + 1
                    Vecteur = [Chaine[l-1],Chaine[l],Chaine[l+1]]
                    ScoreParMot = ScoreOp(Vecteur)
                    Indx.append(l+1)
                IndexTotal[i][2] = Indx
                IndexTotal[i][3] = Counter[i]
            ScoreTotal[NbrText] += ScoreParMot
            Indx = []
        
        Affichage[NbrText] = IndexTotal

        print("Les occurences de chaque mot de la requête pour le texte ",end='')
        print(NbrText+1,end=''),
        print(" sont: ",end=''),
        print(Counter) # Print the occurence of each word in each file
        
        for l in range(len(Counter)):
            Pertinence += Counter[l]
        if Pertinence == 0:
            ScoreTotal[NbrText] = (ScoreTotal[NbrText] / 1) 
        else:
            ScoreTotal[NbrText] = (ScoreTotal[NbrText] / Pertinence)
        
        PertiGlob.append(Pertinence)
        print("L'occurence totale de la requête pour le texte ",end='')
        print(NbrText+1,end=''),
        print(" est: ",end=''),
        print(Pertinence) # Print the total of the occurences in each file
        print("""\n\n""")
        
        
        pprint.pprint(Affichage)

    return(Request, PertiGlob,Affichage,ScoreTotal, Length)


