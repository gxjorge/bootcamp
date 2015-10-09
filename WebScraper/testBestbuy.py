__author__ = 'Jorge.GarciaXimenez'

import requests
import pandas as pd
import numpy as np
import math
import json
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from scipy.stats.stats import pearsonr

apiKey="ekv953kjxe8nknnrqsw6c2rv"
page=9 ### colocar 1 --- 9 test
url = "http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page="+str(page)+"&apiKey="+apiKey+"&format=xml"


page = 0 # do same for three pages
max_pages = 1
totprod = []
intprod = []


while page <= max_pages:
    page += 1
    api_key = apiKey
    show = "sku,bestSellingRank,categoryPath.name,color,condition,customerReviewAverage,customerReviewCount,description,details.name,details.value,dollarSavings,features.feature,freeShipping,frequentlyPurchasedWith.sku,inStoreAvailabilityText,longDescription,manufacturer,modelNumber,name,onlineAvailability,onlineAvailabilityText,onSale,percentSavings,preowned,regularPrice,salePrice,shipping,shippingCost,shortDescription,sku,type,upc,url"
    #show = "sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount"

    sort = "bestSellingRank.asc"
    filter = "&pageSize=100&format=json&page="+str(page)
    url = "https://api.bestbuy.com/v1/products((categoryPath.id=abcat0901000))?apiKey=" + api_key + "&sort=" + sort + "&show=" + show + filter
    print(url)

    #t = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id=abcat0101000))?apiKey=g82m86t7tdzw2mau9qvtud9b&sort=bestSellingRank.asc&show=bestSellingRank,categoryPath.name,color,condition,customerReviewAverage,customerReviewCount,description,details.name,details.value,dollarSavings,features.feature,freeShipping,frequentlyPurchasedWith.sku,inStoreAvailabilityText,longDescription,manufacturer,modelNumber,name,onlineAvailability,onlineAvailabilityText,onSale,percentSavings,preowned,regularPrice,salePrice,shipping,shippingCost,shortDescription,sku,type,upc,url&pageSize=100&format=json")
    df = pd.read_json(url)
    #g = pd.read_json(str(t))
    print (page)
    if (page == 1 ):
        max_pages = df['totalPages'][0]
        print(max_pages)
    #print(df)
    # Load in Panda
    dd = pd.DataFrame(df)

    products = dd["products"]
    #print(products[0])
    # Create list with all columns
    #columns=['SKU', 'Manufacturer', 'Model', 'Price', 'Reviews', 'Color', 'Savings', 'Best Selling Rank','Review', 'Screen Size Class', 'HDMI Ports', 'Product Weight', 'USB Ports', 'Network', 'Speaker Output','Product Depth', 'Electricity Use', 'Display Type', '3D', 'Screen Size', 'Refresh Rate', 'Resolution']

    columns =  ['upc','url','sku','name','modelNumber','manufacturer','salePrice','shippingCost','dollarSavings',
                'percentSavings','bestSellingRank','customerReviewCount','customerReviewAverage','color',
                'inStoreAvailabilityText','onlineAvailabilityText','description','shortDescription','longDescription',
                'Details: Temperature Control Type','Details: Refrigerator Capacity', 'Details: Number Of Doors',
                'Details: Freezer Compartment', 'Details: ENERGY STAR Certified', 'Details: Humidity-Controlled Crisper',
                'Details: Refrigerator Type', 'Details: Thru-The-Door Dispenser','Details: Freezer Capacity',
                'Details: Height To Top Of Refrigerator', 'Details: Water Filtration','Details: Ice Maker', 'Details: pricematch']
    #print(len(columns))
    # Initialize 2 dictionaries to do the work

    for i in products:
        q = 1
        while q <= 32:
            intprod.append(None)
            q += 1

        intprod[0] = i['upc']
        intprod[1] = i['url']
        intprod[2] = i['sku']
        intprod[3] = i['name']
        intprod[4] = i['modelNumber']
        intprod[5] = i['manufacturer']
        intprod[6] = i['salePrice']
        intprod[7] = i['shippingCost']
        intprod[8] = i['dollarSavings']
        intprod[9] = i['percentSavings']
        intprod[10] = i['bestSellingRank']
        intprod[11] = i['customerReviewCount']
        intprod[12] = i['customerReviewAverage']
        intprod[13] = i['color']
        intprod[14] = i['inStoreAvailabilityText']
        intprod[15] = i['onlineAvailabilityText']
        intprod[16] = i['description']
        intprod[17] = i['shortDescription']
        intprod[18] = i['longDescription']



        for y in i["details"]:
            check = 0
            if y["name"] == "Temperature Control Type":
                intprod[19] = y['value']
            if y["name"] == "Refrigerator Capacity":
                intprod[20] = y['value']
            if y["name"] == "Number Of Doors":
                intprod[21] = y['value']
            if y["name"] == "Freezer Compartment":
                intprod[22] = y['value']
            if y["name"] == "ENERGY STAR Certified":
                intprod[23] = y['value']
            if y["name"] == "Humidity-Controlled Crisper":
                intprod[24] = y['value']
            if y["name"] == "Refrigerator Type":
                intprod[25] = y['value']
            if y["name"] == "Thru-The-Door Dispenser":
                intprod[26] = y['value']
            if y["name"] == "Freezer Capacity":
                intprod[27] = y['value']
            if y["name"] == "Height To Top Of Refrigerator":
                intprod[28] = y['value']
            if y["name"] == "Water Filtration":
                intprod[29] = y['value']
            if y["name"] == "Ice Maker":
                intprod[20] = y['value']
            if y["name"] == "pricematch":
                intprod[21] = y['value']
        totprod.append(intprod)
        intprod = []

#print(totprod)
newDf = pd.DataFrame(totprod, columns=columns)
#print(newDf)
newDf.to_excel("Export_Products.xlsx")
newDf.to_csv("Export_Products.csv")

# Do descriptive stats
#plt.scatter(newDf["Price"], newDf["Screen Size"])
#plt.show()


