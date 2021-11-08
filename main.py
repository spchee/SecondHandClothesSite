from depopAPI import DepopAPI
from ebayAPI import EbayAPI
from vintedAPI import VintedAPI

search = "something"
items = []

depop = DepopAPI()
ebay = EbayAPI()
vinted = VintedAPI()

items.extend(depop.generateItems(search))
items.extend(ebay.generateItems(search))
items.extend(vinted.generateItems(search))
