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
            comment = comment.replace(c,"")

        for word in cachedStopWords:
            if word in comment:
                comment = comment.replace(" "+word+" ","")

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
print(len(new.wordList))
print(len(new.sentimentList))
new.to_excel("Data/wordcloud.xlsx", encoding= 'utf-16')

new = pd.read_excel("Data/wordcloud.xlsx", encoding= 'utf-16')

wordsPos = new[new.sentimentList=="pos"]
wordsNeg = new[new.sentimentList=="neg"]
countPos = list(Counter(wordsPos.wordList))
countNeg = list(Counter(wordsNeg.wordList))

print(Counter(wordsNeg.wordList))
