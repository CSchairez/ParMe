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

rounds = Blueprint('rounds', __name__)

# Feed route will show all rounds that have been posted.
# Do not need to be logged in to see feed.
@rounds.route('/feed', methods=['GET'])
def feed():

    round_data = Round.query.all()
    round_schema = RoundSchema(many=True)
    output = round_schema.dump(rounds)
    return jsonify({'round': output}),200

@jwt_required
@rounds.route('/addRound', methods=['POST'])
def add_round():
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

    return jsonify({"msg" : "round added"})
