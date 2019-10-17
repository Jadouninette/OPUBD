# -*- coding: utf-8 -*-
"""
Created on Tue May 29 19:12:03 2018

@author: Jadouninette
"""

# -*- coding: utf-8 -*-

"""
@authors: Sandy Basileu / Florian Peixoto / Jade Petot / Johann Schaber
"""

import nltk
import pylab
import numpy as np
from nltk.corpus import sentiwordnet as swn
from pylab import *
import nltk # Import NLTK for tokenize, corpus and stem
import os # Import OS for the directory of the documents
from nltk.corpus import wordnet as wn # Import Wordnet (same as Sentiwordnet)
from nltk.stem import WordNetLemmatizer # Import function of Lemmatizer (for singular nouns, infinitive verb....)
from nltk.stem import PorterStemmer
from gensim.summarization.bm25 import get_bm25_weights
import pprint
import glob

wnl = WordNetLemmatizer() # Call the function lemmatize, to singularize the nouns and to keep the infinitives

Pathdir = "C:/Users/jadouninette/Desktop/Corpus/" # Select the directory of the files we want to compare -- Need to be changed before running the program

os.chdir(Pathdir) 

Corpus_pdf = glob.glob('*.pdf')

for l in range(len(Corpus_pdf)): # Convert every PDF File into TXT File
    PathFile = os.path.join(Pathdir,Corpus_pdf[l])
    getPDFContent(PathFile) 

Corpus = glob.glob('*.txt')

#Corpus = ["AnalyzingUsageSocialMediaonElderlyMalaysia.txt","BehavioralExperimentsSmallSocietiesSocialMediaFacebookExpressionsAnchoredRelationships.txt","DetectionGenre.txt","ESWC2015.txt","Genre.txt","PracticalGuidetoSentimentAnalysis.txt","S172088.txt","s40537-015-0015-2.txt","sentiment-analysis-in-tripadvisor.txt","sentiment-e-commerce.txt"] # Names of the files, saved in the previous directory

    
Request = input("What is your request ? ") # Ask for the request
print("La requete saisie ",end='') 
print("est: ",end='')
print(Request) # Print the request
print("""\n""")

    
Request = Request.lower()  # The request is converted into lowercase letters 
Request = Request.split()  # The request is splited
unwanted ={'.',',','?','!','(',')','\n','<','>','//','@',':',';','“'}
Request = [i for i in Request if i not in unwanted]
    
PertiGlobal = []

(Request,PertiGlob,Affichage,ScoreTotal,Length) = Pertinence(Corpus,Request) # Function to determine the pertinence of each text

print(Length)

for i in range(len(Length)):
    PertiGlobal.append(PertiGlob[i] / Length[i])

OccurenceVect = [[PertiGlob[i], Corpus[i]] for i in range(len(PertiGlob))] # Concatenate the Corpus and the Pertinence of the texts
OccurenceSorted = Tri_ins(PertinenceVect) # Sort the Vector 
print(OccurenceSorted) # Print it (the first one is the most relevant file)

print('''\n''')
print("The most occurent file is ",end='')
print(OccurenceSorted[0][1],end='')
print(" with ",end='')
print(OccurenceSorted[0][0],end='')
print(" occurences of the requested words")


for l in range(len(Corpus)):
    PertiGlobal.append(OpGlob(ScoreTotal[i],PertiGlob[i],Length[i]))


PertinenceVect = [[PertiGlobal[i], Corpus[i]] for i in range(len(PertiGlob))] # Concatenate the Corpus and the Pertinence of the texts
PertinenceSorted = Tri_ins(PertinenceVect) # Sort the Vector 
print(PertinenceSorted) # Print it (the first one is the most relevant file)

OpinionVect = [[ScoreTotal[i], Corpus[i]] for i in range(len(PertiGlob))] # Concatenate the Corpus and the Pertinence of the texts
OpinionSorted = Tri_ins(OpinionVect)
print(OpinionSorted)

print('''\n''')
print("The most relevant file is ",end='')
print(PertinenceSorted[0][1],end='')
print(" with ",end='')
print(PertinenceSorted[0][0])


print('''\n''')
print("The file which has the highest opinion carrier is ",end='')
print(OpinionSorted[0][1],end='')
print(" with the value of ",end='')
print(OpinionSorted[0][0])



