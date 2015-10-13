__author__ = 'Jorge.GarciaXimenez'

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pandas as pd
from nltk.corpus import stopwords
import re
import string
import math

def word_feats(words):
    return dict([(word, True) for word in words])
def word_feats2(words):
    return dict([(word, True) for word in words.split()])

def commentCleaning(comentList):
    cachedStopWords = stopwords.words("english")
    temp = []
    i = 0
    for comment in comentList:
        #print(i)
        i+=1
        comment = comment.lower()
        for c in string.punctuation:
            comment = comment.replace(c,"")
        #temp = ' '.join([word for word in temp.split() if word not in cachedStopWords])

        temp.append(word_feats2(comment))
    return temp

productsBestbuy = pd.read_excel("Data/Data_Bestbuy2.xlsx", encoding= 'utf-16')
testData = commentCleaning(productsBestbuy["Comment"])


negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4

trainfeats = negfeats[:int(negcutoff)] + posfeats[:int(poscutoff)]
testfeats = negfeats[int(negcutoff):] + posfeats[int(poscutoff):]
print ('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))
#print(testData[:10])
#print(type(testfeats),type(testfeats[0]), type(testfeats[0][0]))
#print(testfeats[0])
#print (len(testfeats),len(testfeats[0]),len(testfeats[0][0]))
classifier = NaiveBayesClassifier.train(trainfeats)
#print( 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
classifier.show_most_informative_features()

#print( 'accuracy:', nltk.classify.util.accuracy(classifier, testData))
totResults = []
totResultsProbPos = []
totResultsProbNeg = []
for t in testData:
    result = classifier.classify(t)
    totResults.append(result)
    resultProbs = list(classifier.prob_classify(t)._prob_dict.values())
    totResultsProbPos.append(math.exp(resultProbs[0]))
    totResultsProbNeg.append(math.exp(resultProbs[1]))
#print(classifier.prob_classify(testData[0])._prob_dict)
#resultProbs = list(classifier.prob_classify(testData[0])._prob_dict.values())
#for elem in resultProbs:
#    print(math.exp(elem))
productsBestbuy["Sentiment Analysis Probability Positive"] = totResultsProbPos
productsBestbuy["Sentiment Analysis Probability Negative"] = totResultsProbNeg
productsBestbuy["Sentiment Analysis"] = totResults
productsBestbuy.to_excel("Data/Data_Bestbuy2.xlsx")
'''
for j in range(1,100):
    print(productsBestbuy["Comment"][j])
    print(productsBestbuy["Sentiment Analysis"][j])
    '''