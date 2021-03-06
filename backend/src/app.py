import os
import datetime
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pycoingecko import CoinGeckoAPI
import json

from .auth import verify_jwt

# Load dotenv files
load_dotenv()

from .util import db
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
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401
    return json.dumps(cg.get_coins_list())

# WATCHLIST

@app.route('/watchlist/<portfolio_id>', methods=['GET'])
@cross_origin()
def get_watchlist(portfolio_id):
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401

    return json.dumps(db.get_watchlist(portfolio_id))

@app.route('/watchlist/<portfolio_id>/<coin_id>', methods=['POST'])
@cross_origin()
def post_watching(portfolio_id, coin_id):
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401

    return json.dumps(db.post_watching(portfolio_id, coin_id))

@app.route('/watchlist/<id>', methods=['DELETE'])
@cross_origin()
def delete_watching(id):
    # TODO: BROKEN
    return db.delete_watching(id)

# PURCHASES

@app.route('/purchases/<portfolio_id>', methods=['GET'])
@cross_origin()
def get_purchases(portfolio_id):
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401
    return json.dumps(db.get_purchases(portfolio_id), default=str)

@app.route('/purchases/<portfolio_id>/<coin_id>/<amount>', methods=['POST'])
@cross_origin()
def post_purchase(portfolio_id, coin_id, amount):
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401
    purch_price = cg.get_price(coin_id, "cad")[coin_id]["cad"]
    print(purch_price)
    return db.post_purchase(portfolio_id, coin_id, purch_price, amount)

# ORDERS

@app.route('/orders/<portfolio_id>', methods=['GET'])
@cross_origin()
def get_orders(portfolio_id):
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401
    return json.dumps(db.get_orders(portfolio_id), default=str)

@app.route('/orders/<portfolio_id>/<coin_id>/<amount>/<time>', methods=['POST'])
@cross_origin()
def post_order(portfolio_id, coin_id, amount, time):
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401
    time_obj = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
    return db.post_order(portfolio_id, coin_id, amount, time_obj)

@app.route('/orders/<order_id>', methods=['DELETE'])
@cross_origin()
def delete_order():
    # TODO: BROKEN
    return ""

# PORTFOLIOS

@app.route('/portfolios/<user_id>', methods=['GET'])
@cross_origin()
def get_portfolios(user_id):
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401
    return json.dumps(db.get_portfolios(user_id))

@app.route('/portfolios/<user_id>/<name>', methods=['POST'])
@cross_origin()
def post_portfolio(user_id, name):
    # jwt = verify_jwt()

    # if jwt == False:
    #     return "Unauthorized", 401
    
    # user_id, name
    id = db.post_portfolio(user_id, name)
    return(id)

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

