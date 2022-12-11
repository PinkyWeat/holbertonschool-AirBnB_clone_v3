#!/usr/bin/python3
"""city views module"""


from flask import Flask, request, abort, jsonify
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=['GET'],
                 strict_slashes=False)
def allCity(state_id):
    """list of all city objects"""
    city_list = []
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    for city in state.cities:
        city_list.append(city.to_dict())
    return jsonify(city_list)


@app_views.route("/cities/<city_id>", methods=['GET'], strict_slashes=False)
def city_by_id(city_id):
    """list one city object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return city.to_dict()
