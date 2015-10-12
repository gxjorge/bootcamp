__author__ = 'Jorge.GarciaXimenez'


import pandas as pd


apiKey="6x2nnn3a6dg7fpr7pk8rydxx"


startP = 1 # do same for three pages
max_products = 1
totprod = []
intprod = []


while startP <= max_products:

    api_key = apiKey
    url = "http://api.walmartlabs.com/v1/search?query=fridges&format=xml&categoryId=4044_90548_90791&apiKey="+ api_key +"&numItems=25&start="+ str(startP)
    print(url)
    df = pd.read_html(url)
    #g = pd.read_json(str(t))
    print (startP)
    if (startP == 1 ):
        max_products = df['totalResults'][0]
        print(max_products)
    startP=+25
    #print(df)
    # Load in Panda
    dd = pd.DataFrame(df)
    print (dd)
    products = dd["products"]
    #print(products[0])
    # Create list with all columns
    #columns=['SKU', 'Manufacturer', 'Model', 'Price', 'Reviews', 'Color', 'Savings', 'Best Selling Rank','Review', 'Screen Size Class', 'HDMI Ports', 'Product Weight', 'USB Ports', 'Network', 'Speaker Output','Product Depth', 'Electricity Use', 'Display Type', '3D', 'Screen Size', 'Refresh Rate', 'Resolution']
    """
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

"""
