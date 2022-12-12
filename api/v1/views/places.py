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


@app_views.route("/cities/<city_id>/places",
                 strict_slashes=False, methods=['POST'])
def post_places(city_id):
    """enables users to send HTML form data to server"""
    city = storage.get(City, city_id)
    new_place = request.get_json()

    if city is None:
        abort(404)
    if new_place is None:
        abort(400, description="Not a JSON")

    if "name" not in new_place:
        abort(400, description="Missing name")

    if "user_id" not in new_place:
        abort(400, description="Missing user_id")

    if storage.get(User, new_place['user_id']) is None:
        abort(404)

    new_place['city_id'] = city_id
    new_place = Place(**new_place)
    new_place.save()
    return jsonify(new_place.to_dict()), 201
