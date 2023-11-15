"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


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

    password = generate_password_hash(password)

    new_user = User(email = email, password=password, is_active=is_active)



    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"Message":"User created"}), 201
    except Exception as error:
        db.session.rollback()
        return jsonify({"Message":f"{error}"}), 500


@api.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).one_or_none()

    if user is None:
        return jsonify({"Message":"Wrong propperty"}), 400
    else:
        if check_password_hash(user.password, password):
            return jsonify({"Message":"success"}), 200
        else:
            return jsonify({"Message":"Wrong propperty"}), 400
        