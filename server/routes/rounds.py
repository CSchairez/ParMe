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


# Our db object from SQLAlchemys
from ..models.db_init import db

rounds = Blueprint('rounds', __name__)

# Feed route will show all rounds that have been posted.
# Do not need to be logged in to see feed.
@rounds.route('/feed', methods=['GET'])
def feed():

    round_data = Round.query.all()
    round_schema = RoundSchema(many=True)
    output = round_schema.dump(round_data)
    return jsonify({'round': output}),200


@rounds.route('/addRound', methods=['POST'])
@jwt_required
def add_round():
    # Get the data from the body of the request
    data = request.get_json()

    # Filter DB by token (email)
    user_email = get_jwt_identity().get('email')
    
    # Query the user to get their user_id
    user = User.query.filter_by(email=user_email).first()
    
    
    # Pull out the course name and score
    course = request.json.get("course", None)
    score = request.json.get("score", None)
    
    # Add round to the db
    new_round = Round(course_name=course, score=score, user_id=user.user_id)
    db.session.add(new_round)
    db.session.commit()

    # Jsonify the new round
    round_schema = RoundSchema(many=False)
    output = round_schema.dump(new_round)

    return jsonify({"msg" : output})

@rounds.route('/commentRound', methods=['POST'])
@jwt_required
def comment_round():
    
    # Get the data from the body of the request
    data = request.get_json()
    
    # Filter DB by token (email)
    user_email = get_jwt_identity().get('email')
    
    # Query the user to get their user_id
    user = User.query.filter_by(email=user_email).first()
    
    # Get the content of the comment
    user_content = request.json.get("content", None)

    # Get the round_id they want to comment on
    new_comment = Comment(content=user_content, user_id=user.user_id)

    db.session.add(new_comment)
    db.session.commit()

    return jsonify({'comment': user_content,
                    'user_id': user.user_id}),200
    



