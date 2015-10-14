__author__ = 'Jorge.GarciaXimenez'

import re
import string
from nltk.corpus import stopwords
import sklearn
import pandas as pd

def getData(file):
    textLines = []
    textWords = []
    with open(file, "r") as ins:
        for line in ins:
            textLines.append(line)
            textWords.append(line.split())
    wordTemp = []
    lineTemp = []
    print(len(textLines))
    for line in textWords:
        l1=""
        for word in line:
            if not "label" in word:
                numberTemp = re.match('.*?([0-9]+)$', word).group(1)
                temp = word.replace("_"," ")
                temp = temp.replace(numberTemp,"")
                numberTemp = int(numberTemp)
                for c in string.punctuation:
                    temp= temp.replace(c,"")
                #print (temp)
                wordTemp.append(temp)
                for count in range(1,numberTemp):
                     l1 =l1+" "+temp
        lineTemp.append(l1)


    cachedStopWords = stopwords.words("english")
    temp = lineTemp
    lineTemp = []
    for l in temp:
        l = ' '.join([word for word in l.split() if word not in cachedStopWords])
        lineTemp.append(l)
    print (len(lineTemp))
    return (lineTemp)

"""
textLines = []
textWords = []
with open("Data/trainingReviews/positive.review", "r") as ins:
    for line in ins:
        textLines.append(line)
        textWords.append(line.split())
wordTemp = []
lineTemp = []
print(len(textLines))
for line in textWords:
    l1=""
    for word in line:
        if not "label" in word:
            numberTemp = re.match('.*?([0-9]+)$', word).group(1)
            temp = word.replace("_"," ")
            temp = temp.replace(numberTemp,"")
            numberTemp = int(numberTemp)
            for c in string.punctuation:
                temp= temp.replace(c,"")
            #print (temp)
            wordTemp.append(temp)
            for count in range(1,numberTemp):
                 l1 =l1+" "+temp
    lineTemp.append(l1)


cachedStopWords = stopwords.words("english")
temp = lineTemp
lineTemp = []
for l in temp:
    l = ' '.join([word for word in l.split() if word not in cachedStopWords])
    lineTemp.append(l)
print (len(lineTemp))
print (lineTemp)
"""
positiveRev = "Data/trainingReviews/positive.review"
negativeRev = "Data/trainingReviews/negative.review"
positiveData = getData(positiveRev)
negativeData = getData(negativeRev)
trainLabel =[1]*1000 +[0]*1000
trainData = positiveData +negativeData
print(trainLabel)


print(trainData)
vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(min_df=2,
                             max_df = 0.8,
                             sublinear_tf=True,
                             use_idf=True)
#trainVectors = vectorizer.fit_transform(trainData)
#test_vectors = vectorizer.transform(test_data)
trainD = trainData[0:990]+trainData[1000:1990]
trainV = vectorizer.fit_transform(trainD)
#trainV = trainVectors[0:900]+trainVectors[1000:1900]
trainL = trainLabel[0:990]+trainLabel[1000:1990]
testL = trainLabel[990:1000]+trainLabel[1990:]
testD = trainData[990:1000]+trainData[1990:]
testV = vectorizer.transform(testD)
#testV = trainVectors[900:1000]+trainVectors[1900:]
print (len(trainD))
print (len(testD))
classifier_rbf = sklearn.svm.SVC()
classifier_rbf.fit(trainV, trainL)
prediction_rbf = classifier_rbf.predict(testV)
print (prediction_rbf)
