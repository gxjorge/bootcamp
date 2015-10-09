__author__ = 'Jorge.GarciaXimenez'


import pandas as pd

import WebScraper

def getOneProduct(soupItem):

    product = [{"itemid": soupItem.find("itemid").getText(), "name": soupItem.find("name").getText(),
                "msrp": soupItem.find("msrp").getText(), "saleprice": soupItem.find("saleprice").getText(), "upc": soupItem.find("upc").getText(),
                "shortdescription": soupItem.find("shortdescription").getText(), "longdescription": soupItem.find("longdescription").getText(),
                "modelNumber": soupItem.find("modelNumber").getText(), "modelNumber": soupItem.find("modelNumber").getText(),
                "productUrl": soupItem.find("productUrl").getText(), "customerRating": soupItem.find("customerRating").getText()}]
    list = pd.DataFrame(product)
    print(list)

apiKey="6x2nnn3a6dg7fpr7pk8rydxx"
url = "http://api.walmartlabs.com/v1/search?query=fridges&format=xml&categoryId=4044_90548_90791&apiKey=6x2nnn3a6dg7fpr7pk8rydxx"
response = WebScraper.getSoup(url)
response = response.find("searchresponse")
print(response)
items = response.findAll("item")
getOneProduct(items[0])




