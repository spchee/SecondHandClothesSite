from flask import Flask, render_template, request
from depopAPI import DepopAPI
#from ebayAPI import EbayAPI
from vintedAPI import VintedAPI
import random

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == "GET":
        search = "something"
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
    elif request.method == "POST":
        search = request.form['search']
        items = []


if __name__ == '__main__':
    app.run(debug=True)





