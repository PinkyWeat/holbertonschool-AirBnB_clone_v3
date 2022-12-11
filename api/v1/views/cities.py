#!/usr/bin/python3
"""city views module"""


from flask import Flask, request, abort, jsonify
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City


@app_views.route('/states/<s_id>/cities', methods=['GET'], strict_slashes=False)
def get_all_cities(s_id):
    """gets all city"""
    themcity = []
    state = storage.get(State, s_id)

    if state is None:
        abort(404)
    for city in state.cities:
        themcity.append(city.to_dict())
    return jsonify(themcity)


@app_views.route("/cities/<c_id>", methods=['GET'], strict_slashes=False)
def get_city_id(c_id):
    """gets city by id"""
    if storage.get(City, c_id) is None:
        abort(404)
    return jsonify(storage.get(City, c_id).to_dict())
