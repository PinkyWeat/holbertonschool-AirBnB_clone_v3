#!/usr/bin/python3
"""index module"""
from api.v1.views import app_views
import json


@app_views.route('/status')
def status():
    return {"Status": "OK"}
