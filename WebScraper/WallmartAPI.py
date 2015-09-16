__author__ = 'Jorge.GarciaXimenez'

import WebScraper

apiKey="6x2nnn3a6dg7fpr7pk8rydxx"

url = "http://api.walmartlabs.com/v1/feeds/items?apiKey={"+apiKey+"}&categoryId=3944"

json = WebScraper.getSoup(url)
print(json)