#!/usr/bin/python3
"""review views module"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


@app_views.route("/places/<place_id>/reviews", methods=['GET'], strict_slashes=False,)
def get_reviews(place_id):
    """gets all reviews"""
    place = storage.get(Place, place_id)
    themReviews = []
    if place is None:
        abort(404)
    for rev in place.reviews:
        themReviews.append(rev.to_dict())
    return jsonify(themReviews)


@app_views.route("/reviews/<review_id>", methods=['GET'], strict_slashes=False)
def get_reviews(review_id):
    """get places by id"""
    review = storage.get(Review, review_id)
    if review_id is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route("/reviews/<review_id>", strict_slashes=False, methods=['DELETE'])
def del_review(review_id):
    """deletes reviews by id"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200
