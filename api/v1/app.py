#!/usr/bin/python3
"""Flask module"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
                port=int(getenv('HBNB_API_PORT', '5000')), threaded=True)

@app.teardown_appcontext
def tear_down(exception):
    storage.close()