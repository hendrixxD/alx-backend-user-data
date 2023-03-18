#!/usr/bin/env python3
""" basic flask app """

from auth import Auth
from flask import (Flask, jsonify, request, redirect)
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

AUTH = Auth()


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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """implements login"""
    try:
        email = request.args.get('email')
        password = request.args.get('password')
    except KeyError:
        abort(400)

    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(401)
    except NoResultFound:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """implement logout"""
    session_id = request.cookies.get('session_id', None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user_id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """validates a user profile"""

    session_id = request.cookies.get('session_id', None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({'email': '{}'}.format(email)), 200
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """reset password token"""
    try:
        email = request.args.get('email')
    except KeyError:
        abort(400)

    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    else:
        return jsonify({"email": email, "reset_token": token})


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """implements updatin of passcode"""

    try:
        email = request.args.get('email')
        reset_token = request.args.get('reset_token')
        new_password = request.args.get('new_password')
    except ValueError:
        abort(403)

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    else:
        return jsonify({"email": email, "message": "Password updated"})


if __name__ == "__main__":
    """ main """
    # app.run(host="0.0.0.0", port="5000")
    app.run()
