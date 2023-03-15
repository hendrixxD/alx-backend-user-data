#!/usr/bin/env python3
""" basic flask app """

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """ basic flask app"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    """ main """
    app.run(host="0.0.0.0", port="5000")
