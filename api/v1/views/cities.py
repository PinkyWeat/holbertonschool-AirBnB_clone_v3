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
    state = storage.get(State, state_id)
    if state is None or state.cities is None:
        abort(404)

    cities = storage.get(State, state_id).cities
    themCities = []
    for city in cities:
        themCities.append(city.to_dict())
    return jsonify(themCities)


@app_views.route("/cities/<city_id>", methods=['GET'], strict_slashes=False)
def city_by_id(city_id):
    """get city by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())

@app_views.route("/cities/<city_id>", methods=['DELETE'], strict_slashes=False)
def del_city(city_id):
    """deletes city by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return ({}), 200

@app_views.route("/states/<state_id>/cities", methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """enables users to send HTML form data to server"""
    state = storage.get(State, state_id)
    c_info = request.get_json()

    if state is None:
        abort(404)
    if c_info is None:
        abort(400, description="Not a JSON")
    if "name" not in c_info:
        abort(400, description="Missing Name")
    
    c_info['state_id'] = state_id
    c_info = City(**c_info)
    c_info.save()
    return jsonify(c_info.to_dict()), 201