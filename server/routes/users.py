from flask import Flask, Blueprint, request, redirect, url_for, session, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import datetime
import bcrypt
import jwt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from ..models.round import Round, RoundSchema
from ..models.user import User, UserSchema
from ..models.comment import Comment, CommentSchema


# Model imports to make queries to the DB + the db init
from ..models.round import Round, RoundSchema
from ..models.user import User, UserSchema
from ..models.db_init import db

users = Blueprint('users', __name__)

# Get all the users in the DB
@users.route('/', methods=['GET'])
def all_users():
    try:
        # Use marshmallow to clean up our output from sqlalchemy nicely
        users_data = User.query.all()
        users_schema = UserSchema(many=True)
        output = users_schema.dump(users_data)
        return jsonify({'users': output}), 200

    except:
        return jsonify({"msg": "No users could be found"}), 400

# Accepts a JWT which has a payload of users email. We will decode that on this private route and query the
# DB to see if the user exists. If they do, we will return the users information to the client, else return error
@users.route('/user', methods=['GET'])
@jwt_required
def get_user():   
    try:
        # Filter DB by token (email)
        user_email = get_jwt_identity().get('email')
    
        # Query the user to get their user_id

        users_data = User.query.filter_by(email = user_email).first()
        users_schema = UserSchema(many=False)
        output = users_schema.dump(users_data)
        return jsonify({'users': output}), 200

    except:
        return jsonify({"msg": "User could not be found"}), 400