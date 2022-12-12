#!/usr/bin/python3
"""places views module"""


from api.v1.views import app_views
from flask import abort, request, jsonify
from models import storage
from models.city import City
from models.user import User
from models.place import Place


@app_views.route("/cities/<city_id>/places",
                 strict_slashes=False, methods=['GET'])
def get_places(city_id):
    """gets all places"""
    city = storage.get(City, city_id)
    themPlaces = []
    if city is None:
        abort(404)
    for place in city.places:
        themPlaces.append(place.to_dict())
    return jsonify(themPlaces)


@app_views.route("/places/<place_id>", strict_slashes=False, methods=['GET'])
def get_places_id(place_id):
    """get places by id"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("/places/<place_id>",
                 strict_slashes=False, methods=['DELETE'])
def del_place(place_id):
    """delete a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({}), 200