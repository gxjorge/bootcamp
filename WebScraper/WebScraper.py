__author__ = 'Jorge.GarciaXimenez'

import requests
import bs4

#fix link: from a base url and a partial it is going to create the complete url
def fixLink(url, baseUrl):
    if url.startswith('http://'):
        return url
    else:
        if url.startswith("/"):
            url = url[1:]
        return baseUrl + url

#Give a list of anchors and returns the correspondant soup elements
def listOfLinksFromAnchors(listAnchor,baseurl):
    soupList = []
    for aSoup in listAnchor:
        url = aSoup["href"]
        url = fixLink(url, baseurl)
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text)
        soupList.append(soup)
    return soupList

#GetSoup from a url
def getSoup(url):
    r= requests.get(url)
    soup = bs4.BeautifulSoup(r.text)
    return soup

#findAll elemenents from a soup elem
def getAllElems(soupElem,elem,argument=None,argumentValue=None):
    output = soupElem.findAll(elem, {"argument": "argumentValue"})
    #example : tableSoup1 = soup.findAll("div", {"id": "B"})
    return output

#findAll elemenents from a soup elem
def getElems(soupElem,elem,argument=None,argumentValue=None):
    output = soupElem.find(elem, {"argument": "argumentValue"})
    #example : tableSoup1 = soup.findAll("div", {"id": "B"})
    return output

#r = requests.get(url, headers={"User-Agent": "Moz"})