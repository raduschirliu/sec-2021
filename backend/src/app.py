import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS, cross_origin

# Load dotenv files
load_dotenv()


# Initialize Flask
port = int(os.getenv('PORT', 8000))
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

# Hello world
@app.route("/")
@cross_origin
def hello_world():
    return "hello world"

# Run Flask app
if __name__ == '__main__':
    app.run(port=port, threaded=True)
