from flask import Flask
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import dotenv
import sys
import os

# Blueprints
from .api.auth.auth import auth

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    create_db(app)

    return app

def create_db(app):
    app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
    app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

    print('Connected to MySQL database')
    
    mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)


'''
Files named __init__.py are used to mark directories on disk as Python package directories. If you have the files.
This file in our case will be the root file for the server side. It will hook up all our blue prints,
and be the source of running our flask app with 'flask run' 
'''