import os
from flask import Flask
from flask_cors import CORS

# Database init for global db obj + route imports for blueprints
from server.routes.auth import auth
from server.routes.rounds import rounds
from server.models.db_init import db
from server.models.ma_init import ma
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import (create_access_token, get_jwt_identity, JWTManager, jwt_required, get_raw_jwt)


from dotenv import load_dotenv

def create_app():

    # Load the .env data into a parsable dicctionary with os.getenv
    load_dotenv(verbose=True)  

    # initialize flask app
    app = Flask(__name__)

    # Middlewares
    CORS(app)

    # Configure the DB for this app
    app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
    app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")
    app.config['RDS_MYSQL_URI'] = os.getenv("RDS_MYSQL_URI")
    app.config['MY_SECRET_KEY'] = os.getenv("MY_SECRET_KEY")
    # Saving the URI to the app config + disabling DB changes for performance
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("RDS_MYSQL_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['JWT_SECRET_KEY'] = 'this-is-super-secret'
    app.config['JWT_BLACKLIST_ENABLED'] = False
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']


    jwt = JWTManager(app)

    # register all routing blueprints
    app.register_blueprint(auth, url_prefix="/api/auth")
    app.register_blueprint(rounds, url_prefix="/api/rounds")

    return app 


if __name__ == '__main__':
    
    app = create_app()
    
    # Init DB with our app
    db.init_app(app)
    ma.init_app(app)

    # create all tables from our models in the context of our app (which db is initialized with above)
    with app.app_context():
        db.create_all()
    app.run(debug=True)

