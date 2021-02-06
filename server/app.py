from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dotenv
import sys
import os
import pymysql

# Blueprints
from .api.auth import auth

def create_app():
    
    # New flask instance
    app = Flask(__name__)
    
    # Register all blueprints (custom routing)
    app.register_blueprint(auth, url_prefix='/api/auth')

    # establish SQLAlchemy URI and db connection configs
    create_db(app)

    # Wrap the flask instance with the SQLAlchemy ORM and save to db instance
    db = SQLAlchemy(app)

    return app


def create_db(app):
    
    # Attach the environment DB secrets to the app config
    app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
    app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

    # Put in variables to make the connection string below cleaner
    dbUser = app.config['MYSQL_USER']
    dbHost = app.config['MYSQL_HOST']
    dbPass = app.config['MYSQL_PASSWORD']
    dbName = app.config['MYSQL_DB']

    # SQLAlchemy connection URI
    connectionURI = f'mysql+pymysql://{dbUser}:{dbPass}@{dbHost}/{dbName}'

    # Saving the URI to the app config 
    app.config['SQLALCHEMY_DATABASE_URI'] = connectionURI

    # Some feedback to ensure connection has been made
    print('Connected to MySQL database')

app = create_app()

app.run(debug=True)