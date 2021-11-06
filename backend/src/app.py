import os
import datetime
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pycoingecko import CoinGeckoAPI

from .auth import verify_jwt

# Load dotenv files
load_dotenv()

# Initialize Flask
port = int(os.getenv('PORT', 8000))
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

cg = CoinGeckoAPI()

@app.route("/")
@cross_origin
def index():
    return "hello world"

# COINLIST

@app.route('/coinlist', methods=['GET'])
@cross_origin
def get_coinlist():
    return cg.get_coins_list()

# WATCHLIST

@app.route('/watchlist', methods=['GET'])
@cross_origin
def get_watchlist():
    return ""

@app.route('/watchlist/{watched_id}', methods=['GET'])
@cross_origin
def get_watched():
    return ""

@app.route('/watchlist', methods=['POST'])
@cross_origin
def post_watched():
    return ""

@app.route('/watchlist/{watched_id}', methods=['DELETE'])
@cross_origin
def delete_watched():
    return ""

# PURCHASES

@app.route('/purchases', methods=['GET'])
@cross_origin
def get_purchases():
    return ""

@app.route('/purchases/{purchase_id}', methods=['GET'])
@cross_origin
def get_purchase():
    return ""

@app.route('/purchase', methods=['POST'])
@cross_origin
def post_purchase():
    return ""

# ORDERS

@app.route('/orders', methods=['GET'])
@cross_origin
def get_orders():
    return ""

@app.route('/orders/{order_id}', methods=['GET'])
@cross_origin
def get_order():
    return ""

@app.route('/orders', methods=['POST'])
@cross_origin
def post_order():
    return ""

@app.route('/orders/{order_id}', methods=['DELETE'])
@cross_origin
def delete_order():
    return ""

# PORTFOLIOS

@app.route('/portfoilios', methods=['GET'])
@cross_origin
def get_portfolios():
    return ""

# Update user account information
@app.route('/account', methods=['POST'])
@cross_origin()
def update_account():
    jwt = verify_jwt()

    if jwt == False:
        return "Unauthorized", 401

    print(jwt)
    data = request.json
    print(data)

    return "this does nothing!!"

# Run Flask app
if __name__ == '__main__':
    app.run(port=port, threaded=True)
