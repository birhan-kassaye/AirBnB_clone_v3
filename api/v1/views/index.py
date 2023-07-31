#!/usr/bin/python3
""" index """
from api.v1.views import app_views
from flask import jsonify
import models
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ returns a JSON """
    return jsonify({"status": "OK"})

@app_views.route("/stats", strict_slashes=False)

def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
