from flask import Flask, Blueprint, request, redirect, url_for, session, jsonify
import bcrypt

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.route('/login', methods=['POST'])    # prefixed with /api/auth
def login():
    # Get the data from the body of the request
    data = request.get_json()

    # pull out the username and the email
    user_name = request.json.get("username", None)
    user_pass = request.json.get("password", None)

    # hash the entered password with bcrypt
    pass_hash = bcrypt.hashpw(user_pass.encode('utf-8'), bcrypt.gensalt())
    
    # create a new dictionary of the username and the hashed password
    user_data = {
        "username": user_name,
        "password": pass_hash,
    }

    return jsonify(user_data)