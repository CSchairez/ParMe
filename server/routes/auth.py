from flask import Flask, Blueprint, request, redirect, url_for, session, jsonify
import datetime
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

auth = Blueprint('auth', __name__)

# TESTING ROUTE
@auth.route('/')
def index():
    return jsonify({"message" : "hello world"})


@auth.route('/login', methods=['POST'])    # prefixed with /api/auth
def login():
    # Get the data from the body of the request
    data = request.get_json()

    # pull out the username and the email
    user_email = request.json.get("email", None)
    user_pass = request.json.get("password", None)
    
    
    '''
    Lookup the user in the database using a query ----
        If the user exists, then we need to compare the entered password to the hashed password in the database
            If the PW matches, we want to get the users ID and encode that in a JWT and send the jwt to the client
            to be put in local storage (send it back as a json response like {user_id: the_jwt}). The JWT will be our form of
            auth state being carried about across requests and qerying the DB by that user ID
            Else, return a status code of 404 and a message saying the password was incorrect
        Else, return a bad status and a message saying email does not exist
    '''

    # remove this return after the above algorithm is done
    #return jsonify(user_data)

@auth.route('/register')
def register():
    # Get the data from the body of the request
    data = request.get_json()

    # pull out the username and the email
    user_email = request.json.get("email", None)
    user_pass = request.json.get("password", None)
    user_name = request.json.get("name", None)

    # new_user = User("Michael Chairez", "a.chairezmichael@gmail.com","pass123", True)
    # Do some validation later (joi for NodeJS. See equivalent for flask)

    # hash the entered password with bcrypt
    pass_hash = bcrypt.hashpw(user_pass.encode('utf-8'), bcrypt.gensalt())

    # Use the user model to create a new instance of a user and then put them in the DB
    user = User(user_name, user_email, user_pass, admin=True)

    # Add the user to the db and commit the changes
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"user": new_user})
