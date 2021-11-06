import os
import datetime
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pycoingecko import CoinGeckoAPI
import json

from auth import verify_jwt

# Load dotenv files
load_dotenv()

from util import db
db.create_users_table()
db.create_portfolios_table()
db.create_purchases_table()
db.create_orders_table()
db.create_watched_table()

# Initialize Flask
port = int(os.getenv('PORT', 8000))
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

cg = CoinGeckoAPI()

@app.route("/")
@cross_origin()
def index():
    return "hello world"

# COINLIST

@app.route('/coinlist', methods=['GET'])
@cross_origin()
def get_coinlist():
    return json.dumps(cg.get_coins_list())

# WATCHLIST

@app.route('/watchlist/<portfolio_id>', methods=['GET'])
@cross_origin()
def get_watchlist(portfolio_id):
    return json.dumps(db.get_watchlist(portfolio_id))

@app.route('/watchlist', methods=['POST'])
@cross_origin()
def post_watching():
    # portfolio id, coin id in body
    return ""

@app.route('/watchlist', methods=['DELETE'])
@cross_origin()
def delete_watching():
    # watching id in body
    return ""

# PURCHASES

@app.route('/purchases/<portfolio_id>', methods=['GET'])
@cross_origin()
def get_purchases():
    return ""

@app.route('/purchase', methods=['POST'])
@cross_origin()
def post_purchase():
    # portfolio id, coin_id, amount bought
    return ""

# ORDERS

@app.route('/orders/<portfolio_id>', methods=['GET'])
@cross_origin()
def get_orders():
    return ""

@app.route('/orders', methods=['POST'])
@cross_origin()
def post_order():
    # portfolioid, coin id, amount bought
    return ""

@app.route('/orders/<order_id>', methods=['DELETE'])
@cross_origin()
def delete_order():
    return ""

# PORTFOLIOS

@app.route('/portfolios/<user_id>', methods=['GET'])
@cross_origin()
def get_portfolios(user_id):
    return json.dumps(get_portfolios(user_id))

@app.route('/portfolios', methods=['POST'])
@cross_origin()
def post_portfolio():
    # jwt = verify_jwt()

    # # if jwt == False:
    # #     return "Unauthorized", 401
    
    # # user_id, name
    # data = request.json
    # id = post_portfolio(data['user_id'], data['name'])
    # return(id)
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

