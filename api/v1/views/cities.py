#!/usr/bin/python3
"""city views module"""


from flask import Flask, request, abort, jsonify
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=['GET'], strict_slashes=False)
def get_all_cities(state_id):
    """get all cities"""
    themCities = []
    state = storage.get(State, state_id)
    if state is None or state.cities is None:
        abort(404)
    for city in state.cities:
        themCities.append(city.to_dict())
    return themCities


@app_views.route("/cities/<city_id>", methods=['GET'], strict_slashes=False)
def city_by_id(city_id):
    """get city by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return city.to_dict()

@app_views.route("/cities/<city_id>", methods=['DELETE'], strict_slashes=False)
def del_city(city_id):
    """deletes city by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    else:
        city.delete()
        storage.save()
        return {}, 200
