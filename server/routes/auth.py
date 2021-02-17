
import os
from flask import Flask, Blueprint, request, redirect, url_for, session, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, create_refresh_token, jwt_refresh_token_required,
    get_raw_jwt
)
import datetime
import bcrypt
from bcrypt import hashpw, checkpw
import jwt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from .helpers import get_admins
from dotenv import load_dotenv


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
        user_email = request.json["email"]
        user_pass = request.json["password"]

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

        # this is bugged
        if os.getenv("REQ_CODE") == "True":
            if user.password == bcrypt.hashpw(user_pass.encode('UTF_8'), user.password.encode('UTF_8')).decode():
                
                access_token = create_access_token(identity={'email':user_email})
                return jsonify({
                    '_id': user.user_id,
                    'name': user.name,
                    'email': user.email,
                    'isAdmin': user.admin,
                    'token': access_token
                })       
        else: 
            if bcrypt.checkpw(user_pass, user.password):
                access_token = create_access_token(identity={'email':user_email})
                return jsonify({
                    '_id': user.user_id,
                    'name': user.name,
                    'email': user.email,
                    'isAdmin': user.admin,
                    'token': access_token
                })
            else:
                return jsonify({"msg" : 'Invalid credentials'}), 400
        return "here"

    except AttributeError:
        return jsonify({"msg": "Please enter an email and password"}), 400

@auth.route('/register', methods=['POST'])
def register():
    try:
        # pull out the username and the email
        user_email = request.json["email"]
        user_pass = request.json["password"]
        user_name = request.json["name"]

        # If there is no name/email/pw return 400
        if not user_name:
            return jsonify({'msg':'Please enter your name'}), 400
        if not user_email:
            return jsonify({"msg" : 'Missing email'}), 400
        if not user_pass:
            return jsonify({"msg" : 'Missing password'}), 400

        # Check if this users email is an admin elligible email
        isAdmin = get_admins(user_email)

        # hash the entered password with bcrypt
        pass_hash = bcrypt.hashpw(user_pass.encode('utf-8'), bcrypt.gensalt())

        # Use the user model to create a new instance of a user and then put them in the DB
        user = User(user_name, user_email, pass_hash, isAdmin)


        # Create JWT with a payload of the users email
        access_token = create_access_token(identity={'email':user_email})

        # Add the user to the db and commit the changes
        db.session.add(user)
        db.session.commit()

        # return that the user and token
        return jsonify({
            '_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'isAdmin': user.admin,
            'token': access_token,
        }), 200

    # if the user already exists
    except IntegrityError:
        db.session.rollback()
        return jsonify({"msg" : 'User already exists'}), 400
    
    # if the user forgot / did not enter and email or password
    except AttributeError:
        return jsonify({"msg" : 'Provide an Email and Password'}), 400

