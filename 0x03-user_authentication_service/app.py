#!/usr/bin/env python3
""" basic flask app """

from auth import Auth
from flask import (
    Flask,
    jsonify,
    request
)

app = Flask(__name__)

AUTH = Auth


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """ basic flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ registers a new user"""

    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    """ main """
    app.run(host="0.0.0.0", port="5000")
