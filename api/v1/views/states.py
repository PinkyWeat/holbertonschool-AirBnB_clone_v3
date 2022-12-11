#!/usr/bin/python3
"""states views module"""


from flask import Flask, request, abort, jsonify
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """gets all states"""
    themStates = []
    for state in storage.all(State).values():
        themStates.append(state.to_dict())
    return jsonify(themStates)

@app_views.route('/states/<s_id>', methods=['GET'], strict_slashes=False)
def get_state(s_id=None):
    """if no state id is given four o four error, else prints the state"""
    if storage.get(State, s_id) is None:  # id given not found
        abort(404)
    # if id is not none then it can get it
        return jsonify(storage.get(State, s_id).to_dict())

@app_views.route("/states/<state_id>", methods=['DELETE'], strict_slashes=False)
def del_state(s_id):
    """deletes state"""
    if storage.get(State, s_id) is None:
        abort(404)
    storage.get(State, s_id).delete()
    storage.save()
    return ({}), 200
