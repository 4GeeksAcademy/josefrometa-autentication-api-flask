"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode
import os
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)

def set_password(password, salt):
    return generate_password_hash(f"{password}{salt}")


def check_password(hash_password, password, salt):
    return check_password_hash(hash_password, f"{password}{salt}")


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }

#     return jsonify(response_body), 200


# signup a new user
@api.route('/signup', methods=['POST'])
def create_user():
    body = request.json
    email = body.get("email")
    password = body.get("password")
    is_active = body.get("is_active")

    if email is None or password is None:
        return jsonify({"Message":"You should fill all the request data"}), 400
    
    check_email = User.query.filter_by(email=email).first()

    if check_email is not None:
        return jsonify({"Message":"User already exist"})


    salt = b64encode(os.urandom(32)).decode("utf-8")
    password = set_password(password, salt)
    
    new_user = User(email = email, password = password, salt = salt)


    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"Message":"User created"}), 201
    except Exception as error:
        db.session.rollback()
        return jsonify({"Message":f"{error}"}), 500


# Login a user
@api.route('/login', methods=['POST'])
def login():
    body = request.json
    email = body.get("email")
    password = body.get("password")

    user = User.query.filter_by(email=email).one_or_none()

    if email is None or password is None:
        return jsonify({"message":"You need email and password"}), 400
    else:
            if check_password(user.password, password, user.salt):
                token = create_access_token(identity={
                    "user_id":user.id,
                })
                return jsonify({"token":token}), 200
            else:
                return jsonify({"message":"Bad credentials"}), 400

# List all the created users
@api.route('/users', methods=['GET'])
def get_users_list():
     users = User.query.all()
     user_list = []
     for item in users:
         user_list.append(item.serialize())
     return jsonify(user_list), 200 

# List a user that has a valid token
@api.route("/user", methods=["GET"])
@jwt_required()
def get_all_users():
   
    users = User.query.all()
    return jsonify(list(map(lambda item: item.serialize(), users)))

# List a user by id
@api.route("/user/<int:theid>", methods=["GET"])
def get_one_user(theid=None):
    user = User.query.get(theid)
    if user is None:
        return jsonify({"message":"user not found"}), 404
    return jsonify(user.serialize())
    