__author__ = 'Jorge.GarciaXimenez'
import pandas as pd
import time


# Scrape reviews from BestBuy API.

api_key="ekv953kjxe8nknnrqsw6c2rv"

# Import CSV file into a pd

reviewsPanda = pd.read_excel("Export_Products.xlsx")

SKU = reviewsPanda["sku"]

SKU_1 = SKU[0:99]
SKU_2 = SKU[99:199]
SKU_3 = SKU[199:500]

SKU_input1 = ','.join(map(str, SKU_1))
SKU_input2 = ','.join(map(str, SKU_2))
SKU_input3 = ','.join(map(str, SKU_3))

# Construct Call to reviews Page

api_url = "http://api.bestbuy.com/v1/reviews(sku%20in("+SKU_input1+"))?format=json&apiKey="+api_key+"&pageSize=100&page=1&show=id,sku,comment,rating"
df = pd.read_json(api_url)

maxPages = max(df["totalPages"]) - 2
print(maxPages)
reviews = []

page = 1 # Start Page
#maxPages = 50 # Temporary variable for debugging
while page <= maxPages:
    print(page)
    time.sleep(1)
    api_url = "http://api.bestbuy.com/v1/reviews(sku%20in("+SKU_input1+"))?format=json&apiKey="+api_key+"&pageSize=100&page="+str(page)+"&show=id,sku,comment,rating"
    df = pd.read_json(api_url)
    reviews.append(df["reviews"])
    page += 1

# We will put the different values into a DataFrame

x = 0
q = 1
tot_rev = []
review_l = []
columns = ['SKU', 'Rating', 'Comment', 'Rest']
totalLength = 0

for i in reviews:
    for u in i:
        totalLength += len(i)
        while q <= 3:
            review_l.append(None)
            q += 1
        q = 0
        review_l[0] = u['sku']
        review_l[1] = u['rating']
        review_l[2] = u['comment']
        tot_rev.append(review_l)
        review_l = []

newDf = pd.DataFrame(tot_rev, columns=columns)
newDf.to_excel("Export_Reviews.xlsx")

