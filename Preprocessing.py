__author__ = 'Jorge.GarciaXimenez'
import pandas as pd
import matplotlib.pyplot as plt
import collections

productsBestbuy = pd.read_excel("WebScraper/Export_Products.xlsx")
#print(productsBestbuy.head())
reviewsBestbuy = pd.read_excel("WebScraper/Export_Reviews.xlsx")
#print(reviewsBestbuy.head())
resultBestbuy = pd.merge(reviewsBestbuy, productsBestbuy, how='left', left_on="SKU", right_on="sku")
#print(resultBestbuy.describe())
#print(resultBestbuy.columns.values)
#print(resultBestbuy.describe())
del resultBestbuy["Rest"]
del resultBestbuy["Details: pricematch"]
del resultBestbuy["Details: Ice Maker"]
del resultBestbuy["description"]
del resultBestbuy["sku"]
del resultBestbuy["url"]
del resultBestbuy["shippingCost"]
#delete some columns because they are not completed
del resultBestbuy["Details: Refrigerator Capacity"]
#print(collections.Counter(resultBestbuy["Details: Refrigerator Capacity"]))
del resultBestbuy["Details: Number Of Doors"]
#print(collections.Counter(resultBestbuy["Details: Number Of Doors"]))
resultBestbuy["Details: Freezer Capacity"] = resultBestbuy["Details: Freezer Capacity"].str.replace(" cubic feet","")
resultBestbuy["Details: Height To Top Of Refrigerator"] = resultBestbuy["Details: Height To Top Of Refrigerator"].str.replace(" inches","")
resultBestbuy.to_excel("Data/Data_Bestbuy.xlsx")
print(resultBestbuy.columns.values)

for col in resultBestbuy.columns.values:
    if(col!='Comment' and col!='shortDescription'):
        print(col)
        print(collections.Counter(resultBestbuy[col]))

plt.scatter(resultBestbuy["Price"], resultBestbuy["Details: Freezer Capacity"])
plt.show()

"""
productsWalmart = pd.read_excel("WebScraper/Export_Products_Walmart.xlsx")
#print(productsWalmart.head())
reviewsWalmart = pd.read_excel("WebScraper/Export_Reviews_Walmart.xlsx")
#print(reviewsWalmart.head())
resultWalmart = pd.merge(reviewsWalmart, productsWalmart, how='left', left_on="itemid", right_on="itemid")
#print(resultWalmart.head())

print(resultWalmart.columns.values)
resultWalmart.to_excel("Data/Data_Walmart.xlsx")

"""