#!/usr/bin/python3
"""amenities views module"""


from flask import request, abort, jsonify
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity


@app_views.route('amenities/', methods=['GET'], strict_slashes=False)
def get_all_amenities():
    """gets all amenities"""
    themAmenities = []
    amenities = storage.all(Amenity).values()
    for amenity in amenities:
        themAmenities.append(amenity.to_dict())
    return jsonify(themAmenities)


@app_views.route('amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_by_id(amenity_id):
    """gets amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route("/amenities/<amenity_id>", methods=['DELETE'],
                 strict_slashes=False)
def del_amenity(amenity_id):
    """deletes an amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/amenities", strict_slashes=False, methods=['POST'])
def post_amenity():
    """enables users to send HTML form data to server"""
    amenity_data = request.is_json
    if not amenity_data:
        abort(400)
    if "name" not in amenity_data:
        abort(400, description="Missing Name")

    amenity_data = Amenity(**amenity_data)
    amenity_data.save()
    return jsonify(amenity_data.to_dict()), 201
