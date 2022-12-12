#!/usr/bin/python3
"""review views module"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


@app_views.route("/places/<place_id>/reviews",
                 methods=['GET'], strict_slashes=False,)
def get_all_reviews(place_id):
    """gets all reviews"""
    place = storage.get(Place, place_id)
    themReviews = []
    if place is None:
        abort(404)
    for rev in place.reviews:
        themReviews.append(rev.to_dict())
    return jsonify(themReviews)


@app_views.route("/reviews/<review_id>",
                 methods=['GET'], strict_slashes=False)
def get_reviews(review_id):
    """get places by id"""
    review = storage.get(Review, review_id)
    if review_id is None or review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route("/reviews/<review_id>",
                 strict_slashes=False, methods=['DELETE'])
def del_review(review_id):
    """deletes reviews by id"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/places/<place_id>/reviews",
                 strict_slashes=False, methods=['POST'])
def post_review(place_id):
    """enables users to send HTML form data to server"""
    place = storage.get(Place, place_id)
    new_review = request.get_json()

    if place is None:
        abort(404)
    if new_review is None:
        abort(400, descritpion="Not a JSON")
    if "user_id" not in new_review:
        abort(400, descritpion="Missing user_id")

    user = storage.get(User, body.get('user_id'))
    if user is None:
        abort(404)
    if "text" not in new_review.keys():
        abort(400, description="Missing text")

    new_review['place_id'] = place_id
    new_review = Review(**new_review)
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route("/reviews/<review_id>", methods=['PUT'], strict_slashes=False)
def review_put(review_id):
    """puts updated review instance"""
    review = storage.get(Review, review_id)
    review_data = request.get_json()
    ignore_me = ('id', 'created_at', 'updated_at')

    if review is None:
        abort(404)
    if review_data is None:
        abort(400, description="Not a JSON")
    for key, value in review_data.items():
        if key not in ignore_me:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
