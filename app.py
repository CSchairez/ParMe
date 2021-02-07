import os
from flask import Flask
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
    dbUser = os.getenv("MYSQL_USER")
    dbHost = os.getenv("MYSQL_HOST")
    dbPass = os.getenv("MYSQL_PASSWORD")
    dbName = os.getenv("MYSQL_DB")

    # SQLAlchemy connection URI - bugged if using the above vars
    connectionURI = f'mysql://admin:1qaz!2wsx!qwe#2@database-1.cx8lvdttf77k.us-west-1.rds.amazonaws.com/parme'

    print(connectionURI)

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

