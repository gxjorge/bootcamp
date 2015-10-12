__author__ = 'Jorge.GarciaXimenez'


import pandas as pd
import sys
import WebScraper

def getOneProduct(soupItem,totprod):
    product = ["itemid", "name","msrp", "saleprice", "upc","shortdescription", "longdescription","modelNumber", "productUrl", "customerRating","numReviews"]
    #product.append(None)
    #print(soupItem)
    #for ln in soupItem:
    #    print(ln.name)
    if soupItem.find("itemid") is not None :
        product[0] = soupItem.find("itemid").getText()
    if soupItem.find("name")is not None:
        product[1] = soupItem.find("name").getText()
    if soupItem.find("msrp") is not None:
        product[2] = soupItem.find("msrp").getText()
    if soupItem.find("saleprice") is not None:
        product[3] = soupItem.find("saleprice").getText()
    if soupItem.find("upc") is not None:
        product[4] = soupItem.find("upc").getText()
    if soupItem.find("shortdescription") is not None:
        product[5] = soupItem.find("shortdescription").getText()
    if soupItem.find("longdescription") is not None:
        product[6] = soupItem.find("longdescription").getText()
    #print(soupItem.find("modelNumber"))
    if soupItem.find("modelnumber"):
        product[7] = soupItem.find("modelnumber").getText()
    #print(soupItem.find("productUrl"))
    if soupItem.find("producturl"):
        product[8] = soupItem.find("producturl").getText()
    #print(soupItem.find("customerRating"))
    if soupItem.find("customerrating"):
        product[9] = soupItem.find("customerrating").getText()
    if soupItem.find("numreviews"):
        product[10] = soupItem.find("numreviews").getText()
    totprod.append(product)
    #print(list)

def getOneReview(i,j):
    try:
        print(i)
        review = []
        q=1
        while q <= 9:
            review.append(None)
            q += 1

        review[0] = j

        if i.find("name")is not None:
            review[1] = i.find("name").getText()
        if i.find("overallrating").find("rating").getText() is not None:
            review[2] = i.find("overallrating").find("rating").getText()
        if i.find("reviewtext") is not None:
            review[3] = i.find("reviewtext").getText()
        if i.find("submissiontime") is not None:
            review[4] = i.find("submissiontime").getText()
        if i.find("title") is not None:
            review[5] = i.find("title").getText()
        if i.find("upvotes") is not None:
            review[6] = i.find("upvotes").getText()
        #print(soupItem.find("modelNumber"))
        if i.find("downvotes"):
            review[7] = i.find("downvotes").getText()
        #print(soupItem.find("productUrl"))
        if i.find("reviewer"):
            review[8] = i.find("reviewer").getText()
        print(review)
        totrev.append(review)
        print(totrev)
    except ValueError:
         print("error")
        #print (totrev)

apiKey="6x2nnn3a6dg7fpr7pk8rydxx"
query = "fridges"
categoryId = "4044_90548_90791"

startP = 1 # do same for three pages
max_products = 1
totprod = []
intprod = []
totrev = []
intrev = []

columns = ["itemid", "name","msrp", "saleprice", "upc","shortdescription", "longdescription","modelNumber", "productUrl", "customerRating","numReviews"]
while startP <= max_products:
    print(startP)
    url = "http://api.walmartlabs.com/v1/search?query="+query+"&format=xml&categoryId="+categoryId+"&apiKey="+ apiKey +"&numItems=25&start="+ str(startP)
    response = WebScraper.getSoup(url)
    response = response.find("searchresponse")
    if startP == 1:
        max_products = int(response.find("totalresults").getText())
        #print(max_products)
    print(response)
    items = response.findAll("item")
    for i in items:
        getOneProduct(i,totprod)

    startP=startP+25



newDf = pd.DataFrame(totprod, columns=columns)
#print(newDf)
newDf.to_excel("Export_Products_Walmart.xlsx")
newDf.to_csv("Export_Products_Walmart.csv")


newDf =  pd.read_excel("Export_Products_Walmart.xlsx")
columnsRev = ["itemid", "name","overallRating", "reviewText", "submissionTime","title", "upVotes","downVotes", "reviewer"]
numRev = 1
for j in newDf["itemid"]:
    url = "http://api.walmartlabs.com/v1/reviews/"+str(j)+"?format=xml&apiKey="+ apiKey
    print(url)
    response = WebScraper.getSoup(url)
    response = response.findAll("review")

    if not response is not None:
        print("problem")
    print(numRev)
    numRev=numRev+1

    for i in response:
        getOneReview(i,j)
    print(totrev)
newDf1 = pd.DataFrame(totrev, columns=columnsRev)
#print(newDf)
newDf1.to_excel("Export_Reviews_Walmart.xlsx")
newDf1.to_csv("Export_Reviews_Walmart.csv")