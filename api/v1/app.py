#!/usr/bin/python3
"""Flask module"""
from os import *
from flask import Flask
from models import storage
from api.v1.views import app_views


host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')


app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(host=getenv(host or '0.0.0.0'), port=(port or 5000), threaded=True, debug=True)

@app.teardown_appcontext
def tear_down(exception):
    storage.close()