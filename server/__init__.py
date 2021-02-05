from flask import Flask

# Blueprints
from .api.auth.login_routes import auth

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth)

    return app


'''
Files named __init__.py are used to mark directories on disk as Python package directories. If you have the files.
This file in our case will be the root file for the server side. It will hook up all our blue prints,
and be the source of running our flask app with 'flask run' 
'''