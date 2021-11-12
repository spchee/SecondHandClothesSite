# GET https://webapi.depop.com/api/v2/search/products/?what=cat&itemsPerPage=24&country=gb&currency=GBP
import requests
import json
from Products import Product

class DepopAPI:
    def __init__(self):
        self.itemsPerPage = 100
        self.country = 'gb'
        self.currency = 'GBP'

    def get(self, search, priceMin = 0, priceMax = 9999,):
        url = f"https://webapi.depop.com/api/v2/search/products/?what={search}&itemsPerPage={self.itemsPerPage}&country={self.country}&currency={self.currency}&priceMax={priceMax}&priceMin={priceMin}"
        
        response = requests.get(url)
        return response.json()

    def newItem(self, item: dict):
        if item["status"] == "ONSALE":

            url = "https://www.depop.com/products/" + item["slug"]
            price = item["price"]["priceAmount"] #+ item["price"]["nationalShippingCost"]

            # get item["slug"] and replace the dashes with spaces
            name = item["slug"].replace("-", " ")
            images = []
            for image in item["preview"].values():
               images.append(image)

            item = Product(name, price, url, images)
            return item
                
    def generateItems(self, search):
        items = []
        for item in self.get(search)["products"]:
            items.append(self.newItem(item))
        return items



