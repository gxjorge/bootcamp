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
resultBestbuy["Details: Freezer Capacity"] = resultBestbuy["Details: Freezer Capacity"].astype(float)
#resultBestbuy["Details: Freezer Capacity"] = resultBestbuy["Details: Freezer Capacity"].fillna(0)

resultBestbuy["Details: Height To Top Of Refrigerator"] = resultBestbuy["Details: Height To Top Of Refrigerator"].str.replace(" inches","")
resultBestbuy["Details: Height To Top Of Refrigerator"] = resultBestbuy["Details: Height To Top Of Refrigerator"].astype(float)
#resultBestbuy["Details: Height To Top Of Refrigerator"] = resultBestbuy["Details: Height To Top Of Refrigerator"].fillna(0)
ice = []
water = []
sparkling = []
for item in resultBestbuy["Details: Thru-The-Door Dispenser"]:
    if "water" in str(item).lower():
        water.append(1)
    else:
        water.append(0)
    if "ice" in str(item).lower():
        ice.append(1)
    else:
        ice.append(0)
    if "sparkling" in str(item).lower():
        sparkling.append(1)
    else:
        sparkling.append(0)
resultBestbuy["Details: Water Dispenser"] = water
resultBestbuy["Details: Ice Dispenser"] = ice
resultBestbuy["Details: Sparkling Water Dispenser"] = sparkling
resultBestbuy.to_excel("Data/Data_Bestbuy.xlsx")
print(resultBestbuy.columns.values)

for col in resultBestbuy.columns.values:
    if(col!='Comment' and col!='shortDescription'):
        print(col)
        print(collections.Counter(resultBestbuy[col]))
"""
plt.bar(resultBestbuy["salePrice"], resultBestbuy["Rating"])

plt.bar(resultBestbuy["salePrice"], resultBestbuy["manufacturer"])
plt.scatter(resultBestbuy["salePrice"], resultBestbuy["dollarSavings"])
plt.scatter(resultBestbuy["salePrice"], resultBestbuy["percentSavings"])
plt.scatter(resultBestbuy["salePrice"], resultBestbuy["bestSellingRank"])
plt.scatter(resultBestbuy["salePrice"], resultBestbuy["customerReviewCount"])
plt.bar(resultBestbuy["salePrice"], resultBestbuy["customerReviewAverage"])
plt.bar(resultBestbuy["salePrice"], resultBestbuy["color"])
plt.bar(resultBestbuy["salePrice"], resultBestbuy["inStoreAvailabilityText"])
plt.bar(resultBestbuy["salePrice"], resultBestbuy["onlineAvailabilityText"])

plt.show()



productsWalmart = pd.read_excel("WebScraper/Export_Products_Walmart.xlsx")
#print(productsWalmart.head())
reviewsWalmart = pd.read_excel("WebScraper/Export_Reviews_Walmart.xlsx")
#print(reviewsWalmart.head())
resultWalmart = pd.merge(reviewsWalmart, productsWalmart, how='left', left_on="itemid", right_on="itemid")
#print(resultWalmart.head())

print(resultWalmart.columns.values)
resultWalmart.to_excel("Data/Data_Walmart.xlsx")
#resultWalmart["upc"] = resultWalmart["upc"].astype(int)


#NO matching between the different upc
resultWalmart["upc"] = resultWalmart["upc"].str.replace("60NJbWDy0586","0")
resultWalmart["upc"] = resultWalmart["upc"].str.replace("68NJaVEe0005","0")
#resultWalmart["upc"] = resultWalmart["upc"].astype(int)
l1 = set(resultBestbuy["upc"])
l2 = set(resultWalmart["upc"])
print(l1)

l2 = [int(x) for x in l2]
print(l2)


print(list(l1.intersection(l2)))
"""