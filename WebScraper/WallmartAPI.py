__author__ = 'Jorge.GarciaXimenez'


import JsonHandler
import json



text = readjsonFromFile('walmart')

d = json.loads(text)
print( d['glossary']['title'])



"""
import WebScraper
apiKey="6x2nnn3a6dg7fpr7pk8rydxx"

url = "http://api.walmartlabs.com/v1/search?query=fridge&format=json&categoryId=4044_90548_90791&apiKey=6x2nnn3a6dg7fpr7pk8rydxx"

json = WebScraper.getSoup(url).getText()
file = open('walmart', 'w')

file.write(str(json))
file.close()

print(json)

"""

