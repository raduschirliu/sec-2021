import os
import datetime
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS, cross_origin

from .auth import verify_jwt

# Load dotenv files
load_dotenv()

# Initialize Flask
port = int(os.getenv('PORT', 8000))
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route("/")
@cross_origin
def index():
    return "hello world"

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
