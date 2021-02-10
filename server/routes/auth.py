from flask import Flask, Blueprint, request, redirect, url_for, session, jsonify
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


# Feed route will show all rounds that have been posted.
# Do not need to be logged in to see feed.
@auth.route('/feed', methods=['GET'])
def feed():

    rounds = Round.query.all()
    round_schema = RoundSchema(many=True)
    output = round_schema.dump(rounds)
    return jsonify({'round': output})

@auth.route('/', methods=['POST'])
def index():
    # Get the data from the body of the request
    data = request.get_json()

    # pull out the username and the email
    name = request.json.get("name", None)
    course = request.json.get("course", None)
    score = request.json.get("score", None)
    # Figure out how to query the golfer 

    # Query the user to their associated round.
    new_round = Round(course_name=course, score=score, user_id=1)
    db.session.add(new_round)
    db.session.commit()

    return jsonify({"user" : "round added"})


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

@auth.route('/register', methods=['POST'])
def register():
    try:
        # Get the data from the body of the request
        data = request.get_json()

        # pull out the username and the email
        user_email = request.json.get("email", None)
        user_pass = request.json.get("password", None)
        user_name = request.json.get("name", None)

        # If there is no email or password return 400 
        if not user_email:
            return 'Missing email', 400
        if not user_pass:
            return 'Missing password', 400

        # TODO
        # Check if this user exists in the DB (check by the email)
        # if they do, return a json message for error, else, if they do not, hash the password and insert them

        # hash the entered password with bcrypt
        pass_hash = bcrypt.hashpw(user_pass.encode('utf-8'), bcrypt.gensalt())

        # Use the user model to create a new instance of a user and then put them in the DB
        user = User(user_name, user_email, pass_hash)
        # Add the user to the db and commit the changes
        db.session.add(user)
        db.session.commit()

        return f'Welcome! {user_name}', 200
    except IntegrityError:
        db.session.rollback()
        return 'User already exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format.', 400

    return jsonify({"user": user_name + " added to DB"})
