#!/usr/bin/env python3
""" Task 6: Setup basic Flask app """
from flask import Flask, jsonify, request, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def begin():
    """ GET route that uses flask.jsonify to return a JSON payload """
    return jsonify({'message': 'Bienvenue'})


@app.route("/users", methods=["POST"])
def users():
    """ Method implements the end-point to register a user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        if AUTH.register_user(email, password):
            return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
