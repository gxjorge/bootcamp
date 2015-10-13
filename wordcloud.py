__author__ = 'Jorge.GarciaXimenez'

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pandas as pd
from nltk.corpus import stopwords
import re
import string
import math

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
                comment.replace(word,"")
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

print(len(wordList))
print(len(sentimentList))
s1 = pd.Series(wordList, name='wordList')
s2 = pd.Series(sentimentList, name='sentimentList')
new = pd.concat([s1, s2], axis=1)
new.to_excel("Data/wordcloud.xlsx")
