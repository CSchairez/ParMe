import datetime
from .db_init import db
from .ma_init import ma
from sqlalchemy.orm import relationship

class User(db.Model):

    __tablename__ = "user"
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    rounds = db.relationship("Round")
    
    
    
    def __init__(self, name, email, password, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.registered_on = datetime.datetime.now()
        self.admin = admin

# flask-marshmallow>=0.12.0 (recommended) not 'ma.ModelSchema'
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True