__author__ = 'Jorge.GarciaXimenez'

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pandas as pd
from nltk.corpus import stopwords
import re
import string
import math
from collections import Counter



new = pd.read_excel("Data/wordcloud.xlsx", encoding= 'utf-16')
"""
wordsPos = new[new.sentimentList=="pos"]
wordsNeg = new[new.sentimentList=="neg"]
countPos = list(Counter(wordsPos.wordList))
countNeg = list(Counter(wordsNeg.wordList))
"""
print(new.sentimentList[1])
i=1
dict = {}
print(new.describe())
for word in new["wordList"]:
    sent = 0
    try:
        #print(word,new.sentimentList[i])
        if new.sentimentList[i]=="neg":
            sent = -1
        else:
            sent = 1
        if word in dict.keys():
            dict[word] = dict[word] + sent
        else:
            dict[word] =  sent
    except:
        pass
    i+=1
#print(dict)
print(len(dict))
cloudWords = []
cloudSent = []
for key in  dict.keys():
    if dict[key]>0:
        #print(key,dict[key])
        for k in range(1,dict[key]):
            cloudWords.append(key)
            cloudSent.append("pos")
    elif dict[key]<0:
        for k in range(1,dict[key]*-1):
            cloudWords.append(key)
            cloudSent.append("neg")
s1 = pd.Series(cloudWords, name='wordList')
s2 = pd.Series(cloudSent, name='sentimentList')
cloud = pd.concat([s1, s2], axis=1)
cloud.to_excel("Data/wordcloud2.xlsx", encoding= 'utf-16')

#print(Counter(wordsNeg.wordList))
