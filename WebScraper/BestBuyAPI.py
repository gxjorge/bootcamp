__author__ = 'Marcio'

import WebScraper


#apiKey="ekv953kjxe8nknnrqsw6c2rv"

### ALL REFRIGERATORS (NEED LOOP IN PAGE)
#http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name&pageSize=100&page=5&apiKey=ekv953kjxe8nknnrqsw6c2rv&format=json
#http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page=5&apiKey=ekv953kjxe8nknnrqsw6c2rv&format=json

###detail review (need a list of reviews)
##http://api.bestbuy.com/v1/reviews(sku%20in(9037473))?format=json&apiKey=ekv953kjxe8nknnrqsw6c2rv&show=id,sku,title,comment,rating

#url = "http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page=5&apiKey="+apiKey+"&format=xml"
#url = "http://api.walmartlabs.com/v1/feeds/items?apiKey={"+apiKey+"}&categoryId=3944"

#bbsoup = len(WebScraper.getSoup(url))


#print(len(WebScraper.getSoup(url)))


apiKey="ekv953kjxe8nknnrqsw6c2rv"
page=1
bbSoupList=[]
productList=[]
productDic={}

url = "http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page="+str(page)+"&apiKey="+apiKey+"&format=xml"

while len(getSoup(url).findAll("sku")) > 0:
    bbSoupList.append(getSoup(url))
    print(page, len(getSoup(url).findAll("sku")))
    page += 1
    url = "http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page="+str(page)+"&apiKey="+apiKey+"&format=xml"

for soup in bbSoupList:
    productList.extend(soup.findAll("product"))

for product in productList:
    productDic[product.find("sku").getText()] = product.find("sku").getText()



