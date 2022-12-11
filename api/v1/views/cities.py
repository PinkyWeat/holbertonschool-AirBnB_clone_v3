#!/usr/bin/python3
"""city views module"""


from flask import Flask, request, abort, jsonify
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=['GET'], strict_slashes=False)
def cities_index(state_id):
    if storage.get(State, state_id) is None:
        abort(404)

    cities = storage.get(State, state_id).cities
    cities_dict = []
    for city in cities:
        cities_dict.append(city.to_dict())
    return jsonify(cities_dict)


@app_views.route("/cities/<city_id>", methods=['GET'], strict_slashes=False)
def cities_get(city_id):
    if storage.get(City, city_id) is None:
        abort(404)
    return jsonify(storage.get(City, city_id).to_dict())
