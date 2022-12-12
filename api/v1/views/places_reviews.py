#!/usr/bin/python3
"""reviews views module"""


from api.v1.views import app_views
from flask import abort, request, jsonify
from models import storage
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route("/places/<place_id>/reviews",
                 strict_slashes=False, methods=['GET'])
def get_reviews(place_id):
    review = storage.get(Place, place_id)
    themReviews = []
    if review is None:
        abort(404)
    reviews = storage.get(Place, place_id).reviews
    for rev in reviews:
        themReviews.append(rev.to_dict())
    return jsonify(themReviews)

@app_views.route("/reviews/<review_id>", strict_slashes=False, methods=['GET'])
def get_reviews(review_id):
    """get places by id"""
    review = storage.get(Review, review_id)
    if review_id is None:
        abort(404)
    return jsonify(review.to_dict())
