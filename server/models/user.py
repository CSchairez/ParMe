import datetime
from server.extensions import db
class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, email, password, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.registered_on = datetime.datetime.now()
        self.admin = admin
