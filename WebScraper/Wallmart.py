__author__ = 'Jorge.GarciaXimenez'


import WebScraper

fridgeLinkList = []
baseUrl = "http://www.walmart.com/"
urlSearch = "http://www.walmart.com/search/?query="
# http://www.walmart.com/search/?query=fridge&cat_id=4044_90548_90791&typeahead=frid
query = "fridge"
url = urlSearch+query


soup = WebScraper.getSoup(url)
#print (soup)
numberOfPages = soup.findAll("ul", {"class": "paginator-list"})
numberOfPages = numberOfPages[0].findAll("a")[-1].getText()
print(numberOfPages)
priceList = []
priceSoup = soup.findAll("span", {"class": "price price-display"})
print(priceSoup)
for ps in priceSoup:
    #print(ps.getText())
    priceList.append(ps.getText())

#print(priceSoup.findAll("span", {"class": "sup"}).getText())

print()
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
    a = WebScraper.fixLink(a,baseUrl)
    fridgeLinkList.append(a)


print (fridgeLinkList)
WebScraper.listOfsoupFromlinks(fridgeLinkList)



#WebScraper.listOfLinksFromAnchors(anchorList,baseUrl)