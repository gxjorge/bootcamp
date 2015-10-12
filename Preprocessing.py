__author__ = 'Jorge.GarciaXimenez'
import pandas as pd
import matplotlib.pyplot as plt

productsBestbuy = pd.read_excel("WebScraper/Export_Products.xlsx")
#print(productsBestbuy.head())
reviewsBestbuy = pd.read_excel("WebScraper/Export_Reviews.xlsx")
#print(reviewsBestbuy.head())
resultBestbuy = pd.merge(reviewsBestbuy, productsBestbuy, how='left', left_on="SKU", right_on="sku")
#print(resultBestbuy.describe())
print(resultBestbuy.columns.values)

resultBestbuy.to_excel("Data/Data_Bestbuy.xlsx")


productsWalmart = pd.read_excel("WebScraper/Export_Products_Walmart.xlsx")
#print(productsWalmart.head())
reviewsWalmart = pd.read_excel("WebScraper/Export_Reviews_Walmart.xlsx")
#print(reviewsWalmart.head())
resultWalmart = pd.merge(reviewsWalmart, productsWalmart, how='left', left_on="itemid", right_on="itemid")
#print(resultWalmart.head())

print(resultWalmart.columns.values)
resultWalmart.to_excel("Data/Data_Walmart.xlsx")