from flask import Flask
from flask_restful import Resource, Api, reqparse

import os
import sys

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

sys.path.append(os.path.join(sys.path[0],"endpoints"))
sys.path.append(os.path.join(sys.path[0],"helpers"))

from endpoints.candlestick import Candlestick

app = Flask(__name__)
api = Api(app)

api.add_resource(Candlestick, "/create")

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)