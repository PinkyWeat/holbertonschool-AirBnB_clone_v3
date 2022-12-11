#!/usr/bin/python3
"""Flask module"""
import os
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


try:
    host = os.getenv('HBNB_API_HOST')
except Exception:
    host = '0.0.0.0'
try:
    port = os.getenv('HBNB_API_PORT')
except Exception:
    port = 5000


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


@app.errorhandler(404)
def four_o_four(e):
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    app.run(host=host, port=port,
            threaded=True, debug=True)
