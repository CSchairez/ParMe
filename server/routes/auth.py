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

# User model to create new user records for our user table, and round records for round table.
# Import the schemas to output into serializable json

from ..models.round import Round, RoundSchema
from ..models.user import User, UserSchema

# Our db object from SQLAlchemys
from ..models.db_init import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])    # prefixed with /api/auth
def login():
    try:
        # pull out the username and the email
        user_email = request.json.get("email", None)
        user_pass = request.json.get("password", None)

        # If there is no email or password return 400 
        if not user_email:
            return jsonify({"msg" : 'Missing email'}), 400
        if not user_pass:
            return jsonify({"msg" : 'Missing password'}), 400

        # else the email and password was entered. Let's query the DB and see if this user indeed EXISTS
        user = User.query.filter_by(email=user_email).first()

        # if we could not find a user with that email, return a user not found
        if not user:
            return jsonify({"msg" : 'User not found'}), 400

        # else, they were found so now compare the hashed saved password in the DB to the password the user entered
        # if the password is correct, create a auth token and then send back that user logged in fine and the token, else, return some 400 res
        if bcrypt.checkpw(user_pass.encode('utf-8'), user.password):
            access_token = create_access_token(identity={'email':user_email})
            return jsonify({"msg": f'{user.name} logged in', "access_token": access_token}) 
        else:
            return jsonify({"msg" : 'Invalid credentials'}), 400

    except AttributeError:
        return jsonify({"msg": "Please enter an email and password"})

@auth.route('/register', methods=['POST'])
def register():
    try:
        # pull out the username and the email
        user_email = request.json.get("email", None)
        user_pass = request.json.get("password", None)
        user_name = request.json.get("name", None)

        # If there is no name/email/pw return 400
        if not user_name:
            return jsonify({'msg':'Please enter your name'}), 400
        if not user_email:
            return jsonify({"msg" : 'Missing email'}), 400
        if not user_pass:
            return jsonify({"msg" : 'Missing password'}), 400

        # hash the entered password with bcrypt
        pass_hash = bcrypt.hashpw(user_pass.encode('utf-8'), bcrypt.gensalt())

        # Use the user model to create a new instance of a user and then put them in the DB
        user = User(user_name, user_email, pass_hash)

        # Create JWT with a payload of the users email
        access_token = create_access_token(identity={'email':user_email})

        # Add the user to the db and commit the changes
        db.session.add(user)
        db.session.commit()

        # return that the user was added fine and also the access token to be stored in Local Storage
        return jsonify({"msg": f'{user_name} added successfully', "access_token": access_token}), 200

    # if the user already exists
    except IntegrityError:
        db.session.rollback()
        return jsonify({"msg" : 'User already exists'}), 400
    
    # if the user forgot / did not enter and email or password
    except AttributeError:
        return jsonify({"msg" : 'Provide an Email and Password'}), 400

        