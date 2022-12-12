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
