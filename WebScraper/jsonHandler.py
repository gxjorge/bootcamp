__author__ = 'Jorge.GarciaXimenez'

import WebScraper

def getjson(url):
    json = WebScraper.getSoup(url).getText()
    return json

def savejson(filePath,json):
    file = open(filePath, 'w')
    file.write(str(json))
    file.close()

def readjsonFromFile(filePath):
    file = open(filePath, 'r')
    r = file.read()
    file.close()
    return r