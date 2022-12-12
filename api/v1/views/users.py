#!/usr/bin/python3
"""users views module"""
from api.v1.views import app_views
from flask import abort, request, jsonify
from models import storage
from models.user import User


@app_views.route("/users/", strict_slashes=False, methods=['GET'])
def users_index():
    """gets all users"""
    users = storage.all(User)
    themUsers = []
    for user in users:
        themUsers.append(users[user].to_dict())
    return jsonify(themUsers)


@app_views.route("/users/<user_id>", strict_slashes=False, methods=['GET'])
def get_users(user_id):
    """get users by id"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=['DELETE'], strict_slashes=False)
def user_delete(user_id):
    """Delete a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/users", methods=['POST'], strict_slashes=False)
def post_user():
    """enables users to send HTML form data to server"""
    user_data = request.get_json()
    if not user_data:
        abort(400, description="Not a JSON")
    if "name" not in user_data.keys():
        abort(400, description="Missing Name")
    if "email" not in user_data.keys():
        abort(400, description="Missing Email")
    if "password" not in user_data.keys():
        abort(400, description="Missing Password")

    user = User(**user_data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route("/users/<user_id>", methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """puts updated user instance"""
    user = storage.get(User, user_id)
    user_data = request.get_json()
    ignore_me = ('id', 'created_at', 'updated_at')

    if user is None:
        abort(404)
    if user_data is None:
        abort(400, description="Not a JSON")

    for key, value in user_data.items():
        if key not in ignore_me:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
