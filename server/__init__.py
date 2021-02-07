from flask import Flask
from extensions import db
from routes.auth import auth
import os
import dotenv
import pymysql


def create_app():

    app = Flask(__name__)
    app.register_blueprint(auth)
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

    # Connect to AWD RDS instance
    db = pymysql.connect(host='database-1.cx8lvdttf77k.us-west-1.rds.amazonaws.com', user='admin', password='1qaz!2wsx!qwe#2', database='parme')


    return app, db


if __name__ == '__main__':
    app,db = create_app()
    app.run(debug=True)

