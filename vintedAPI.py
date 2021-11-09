#https://www.vinted.co.uk/api/v2/items?search_text=cats&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&status_ids=&is_for_swap=0&page=1&per_page=24
import requests
import json
from Products import Product

class VintedAPI:
    def __init__(self):
        self.itemsPerPage = 20
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'sec-fetch-dest': 'none',
            'accept': '*/*',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'accept-language': 'en-GB'
        }
        self.session = requests.Session()
        self.set_cookie("http://www.vinted.co.uk")

    def get(self, search, priceMin = 0, priceMax = 9999,):
        url = f"https://www.vinted.co.uk/api/v2/items?search_text={search}&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&status_ids=&is_for_swap=0&page=1&per_page={self.itemsPerPage}"
        
        response = self.session.get(url, headers=self.headers)
        return response.json()
        

    def newItem(self, item: dict):
        if item["can_buy"]:
            title = item["title"]
            url = "https://www.vinted.co.uk" + item["path"]
            price = float(item["price_numeric"]) * 1.05 + 0.7
            images = []
            for image in item["photos"]:
               images.append(image["url"])
            print(images, url, title, price)
            product = Product(title, price, url, images)
            return product


    def generateItems(self, search):
        items = []
        for item in self.get(search)["items"]:
            items.append(self.newItem(item))
        return items

    def set_cookie(self, url):
        """
        Perform a http get request for setting up an initial cookie. Required for Vinted.
        :param url: str
        :return: None
        """
        self.session.get(url)

vinted = VintedAPI()
print(vinted.generateItems("cat"))