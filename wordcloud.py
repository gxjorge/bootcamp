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

productsBestbuy = pd.read_excel("Data/Data_Bestbuy2.xlsx", encoding= 'utf-16')

cachedStopWords = stopwords.words("english")
temp = []
wordList = []
sentimentList = []
commentList = productsBestbuy["Comment"]
i = 0
print(commentList.shape)
for comment in commentList:
    try:
        comment = comment.lower()
        for c in string.punctuation:
            comment = comment.replace(c," ")

        for word in cachedStopWords:
            if word in comment:
                comment = comment.replace(" "+word+" "," ")

        #temp = ' '.join([word for word in temp.split() if word not in cachedStopWords])
        temp = comment.split()
        sentiment =[]

        sentiment = [productsBestbuy["Sentiment Analysis"][i] for elem in range(len(temp))]
        #print(temp)
        wordList = wordList +temp
        sentimentList = sentimentList + sentiment
    except:
        pass
    print(i)
    i+=1
#wordList =[word for word in wordList if len(word)>2]

print(len(wordList))
print(len(sentimentList))
s1 = pd.Series(wordList, name='wordList')
s2 = pd.Series(sentimentList, name='sentimentList')

new = pd.concat([s1, s2], axis=1)
new["lengthWord"] = [len(word) for word in wordList]
new = new[new.lengthWord > 2]
del new["lengthWord"]
print(len(new.wordList))
print(len(new.sentimentList))
new.to_excel("Data/wordcloud.xlsx", encoding= 'utf-16')
"""
new = pd.read_excel("Data/wordcloud.xlsx", encoding= 'utf-16')

wordsPos = new[new.sentimentList=="pos"]
wordsNeg = new[new.sentimentList=="neg"]
countPos = list(Counter(wordsPos.wordList))
countNeg = list(Counter(wordsNeg.wordList))

i=0
dict = {}
print(new.describe())
for word in new["wordList"]:
    sent = 0
    print(word,new.sentimentList[i])
    if new.sentimentList[i]=="neg":
        sent = -1
    else:
        sent = 1
    if word in dict.keys():
        dict[word] = dict[word] + sent
    else:
        dict[word] =  sent
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
"""