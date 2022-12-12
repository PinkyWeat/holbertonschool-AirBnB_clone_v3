#!/usr/bin/python3
"""amenities views module"""


from flask import Flask, request, abort, jsonify
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City
from models.amenity import Amenity

@app_views.route('amenities/', methods=['GET'], strict_slashes=False)
def get_all_amenities():
    """gets all amenities"""
    themAmenities = []
    amenities = storage.all(Amenity).values()
    for amenity in amenities:
        themAmenities.append(amenity.to_dict())
    return jsonify(themAmenities)

@app_views.route('amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_by_id(amenity_id):
    """gets amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())

