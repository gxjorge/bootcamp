__author__ = 'Jorge.GarciaXimenez'


import WebScraper

fridgeLinkList = []
url = "http://www.walmart.com/search/?query=fridge"
baseUrl = "http://www.walmart.com/"
soup = WebScraper.getSoup(url)
#print (soup)
soup = soup.findAll("h4")
print (len(soup))
anchorList = []
for elem in soup:
    anchorList.append(elem.findAll("a"))
#soup = soup.findAll("a")
anchorList.pop(0)
#print (anchorList)
print(anchorList)
for i in range(0,len(anchorList)-1):
    a = anchorList[i][0]['href']
    fridgeLinkList.append(a)

#fridgeLinkList = WebScraper.listOfLinksFromAnchors(fridgeLinkList)
print (fridgeLinkList)

#WebScraper.listOfLinksFromAnchors(anchorList,baseUrl)