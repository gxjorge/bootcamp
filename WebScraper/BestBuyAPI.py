__author__ = 'Marcio'
import WebScraper

apiKey="ekv953kjxe8nknnrqsw6c2rv"

### ALL REFRIGERATORS (NEED LOOP IN PAGE)
#http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name&pageSize=100&page=5&apiKey=ekv953kjxe8nknnrqsw6c2rv&format=json
#http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page=5&apiKey=ekv953kjxe8nknnrqsw6c2rv&format=json

###detail review (need a list of reviews)
##http://api.bestbuy.com/v1/reviews(sku%20in(9037473))?format=json&apiKey=ekv953kjxe8nknnrqsw6c2rv&show=id,sku,title,comment,rating

url = "http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page=5&apiKey="+apiKey+"&format=json"
#url = "http://api.walmartlabs.com/v1/feeds/items?apiKey={"+apiKey+"}&categoryId=3944"

json = WebScraper.getSoup(url)
print(json)