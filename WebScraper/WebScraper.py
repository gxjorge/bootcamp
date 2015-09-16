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

"""
#print(tableSoup1)
countriesB = tableSoup1.findAll("a")
countriesList= []
hrefList=[]
dateList=[]
updateList=[]
summaryList=[]
for columnSoup in countriesB:
    print(columnSoup.getText())
    print(columnSoup.get('href'))
    countriesList.append(columnSoup.getText())
    hrefList.append(columnSoup.get('href'))


linksSoup = countriesB

# Visit all the links, and save their beautifulsoup in a list
soupList = []
for aSoup in linksSoup:
		url = aSoup["href"]
		url = fixLink(url, baseUrl)
		r = requests.get(url)
		soup = bs4.BeautifulSoup(r.text)
		soupList.append(soup)

for page in soupList:
    infos = page.find("div", {"class": "content-block"})
    dates = infos.find("ul")
    for i in dates.findAll("div"):
        i.extract()
    dateList.append(dates.findAll("li")[0].getText())
    updateList.append(dates.findAll("li")[1].getText())
    summaryList.append(infos.findAll("p"))
print(len(countriesList))#+" "+len(hrefList)+" "+len(dateList)+" "+len(updateList)+" "+len(summaryList)+" ")
print(len(hrefList))
print(len(dateList))
print(len(updateList))
print(len(summaryList))
"""