from flask import Flask, render_template, request
from depopAPI import DepopAPI
#from ebayAPI import EbayAPI
from vintedAPI import VintedAPI
import random

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == "GET":
        try:
            search = request.form["search-box-form"]
            products = []

            depop = DepopAPI()
            #ebay = EbayAPI()
            vinted = VintedAPI()

            products.extend(depop.generateItems(search))
            print(products)
            #items.extend(ebay.generateItems(search))
            products.extend(vinted.generateItems(search))
            random.shuffle(products)
            print(search)
            products = []

            depop = DepopAPI()
            #ebay = EbayAPI()
            vinted = VintedAPI()
        except:
            products = []
        return render_template('base.html', products=products)
    elif request.method == "POST":
        search = request.form["search-box-form"]
        print(search)
        print(23)
        products = []

        depop = DepopAPI()
        #ebay = EbayAPI()
        vinted = VintedAPI()

        products.extend(depop.generateItems(search))
        print(products)
        #items.extend(ebay.generateItems(search))
        products.extend(vinted.generateItems(search))
        random.shuffle(products)
        return render_template('base.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)





