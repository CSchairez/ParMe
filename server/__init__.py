from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    from . import models, routes
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

    # Connect to AWD RDS instance
    db.init_app(app)
    models.init_app(app)
    routes.init_app(app)

    return app


if __name__=='__main__':
    app = create_app()
    app.run(debug=True)