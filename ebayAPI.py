import requests
import json
from Products import Product

class EbayAPI:
    def __init__(self):
        self.maxEntries = 20

    def get(self, search, priceMin = 0, priceMax = 9999,):
        url = f"""https://open.api.ebay.com/shopping?
   callname=FindProducts&
   responseencoding=JSON&
   siteid=0&
   version=967&
   QueryKeywords={search}&
   AvailableItemsOnly=true&
   MaxEntries=2"""

    def newItem(self, item: dict):
        pass
                
    def generateItems(self, search):
        items = []
        for item in self.get(search)["products"]:
            items.append(self.newItem(item))
        return items