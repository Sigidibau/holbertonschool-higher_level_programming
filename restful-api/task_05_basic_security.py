#!/usr/bin/python3

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from flask import request
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

app = Flask(__name__)
auth = HTTPBasicAuth()


app.config["JWT_SECRET_KEY"] = 'super secret'
jwt = JWTManager(app)

users = {
    "John": generate_password_hash("hello"),
    "Suasan": generate_password_hash("bye")
}


@ auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@ app.route('/basic-protected',  methods=["GET"])
@ auth.login_required
def login_required():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    acces_token = create_access_token(identity=username)
    return jsonify(acces_token=acces_token)


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify("JWT Auth: Access Granted"), 200


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin():
    current_admin = get_jwt_identity()
    if users is not admin:
        return ({"error": "Admin access required"}), 403
    else:
        return ({"Admin Access: Granted"})
