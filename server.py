import os
from flask import Flask
# from extensions import db
from server.routes.auth import auth
from server.models.user import db
from flask_sqlalchemy import SQLAlchemy
import pymysql

def create_app():

    app = Flask(__name__)

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

    # init db
    db.init_app(app)

    # register all routing blueprints
    app.register_blueprint(auth, url_prefix="/api/auth")

    return app 


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

