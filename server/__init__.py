from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from .extensions import db

def create_app():

    app = Flask(__name__)
    
    app.register_blueprint(auth, url_prefix="/api/auth")

    db.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)