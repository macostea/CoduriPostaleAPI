from flask import Flask
from flask_restful import Api
from .controllers import CodeController
import os

app = Flask(__name__)
api = Api(app)

current_dir = os.path.dirname(os.path.abspath(__file__))
code_controller = CodeController(os.path.join(current_dir, "data/infocod-cu-siruta-mai-2016.xlsx"))

import rozipcode.routes
