from flask import Flask, jsonify, request
from functools import wraps
import re
from server import app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization').split(' ')[1] # token is sent like: Authorization: Bearer kjvnernveorvneovenv where the jibberish
        if not token:
            return jsonify({'message':'Missing token'}), 403
        try:
            data = jwt.decode(token, app.config['MY_SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is missing or invalid'})

        return f'(*args, **kwargs)