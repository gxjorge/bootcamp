#import requests
#import bs4
import WebScraper

def dataDicBB():
    ##Variables
    apiKey="ekv953kjxe8nknnrqsw6c2rv"
    page=9 ### colocar 1 --- 9 test
    bbSoupList=[]
    productList=[]
    productDic={}
    url = "http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page="+str(page)+"&apiKey="+apiKey+"&format=xml"
    
    while len(WebScraper.getSoup(url).findAll("sku")) > 0:
        bbSoupList.append(WebScraper.getSoup(url))
        #print(page, len(WebScraper.getSoup(url).findAll("sku")))
        page += 1
        url = "http://api.bestbuy.com/v1/products(longDescription=Refrigerator*)?show=sku,name,customerReviewAverage,customerTopRated,color,salePrice,customerReviewCount&pageSize=100&page="+str(page)+"&apiKey="+apiKey+"&format=xml"
    
    for soup in bbSoupList:
        productList.extend(soup.findAll("product"))
    
    for product in productList:
        #print(len(product))
        
        if product.find("color"):
            color=product.find("color").getText()
        else:
            color="none"    
        
        productDic[product.find("sku").getText()] = product.find("sku").getText(),\
        product.find("name").getText(),\
        product.find("customerreviewaverage").getText(),\
        color,\
        product.find("saleprice").getText(),\
        product.find("customerreviewcount").getText()
    
    reviewDic={}       
    for key in productDic:
        soupReview = WebScraper.getSoup("http://api.bestbuy.com/v1/reviews(sku%20in("+key+"))?format=xml&apiKey="+apiKey+"&show=id,sku,title,comment,rating")
        reviewDic[key]=soupReview.findAll("comment")
        #print(key)
    
    return productDic,reviewDic
    

   
dataDicBB()
   
   
    

    