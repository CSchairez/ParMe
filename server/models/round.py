import datetime
from .db_init import db
from sqlalchemy import ForeignKey
from .ma_init import ma

class Round(db.Model):

    __tablename__ = "round"
    
    round_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(25), unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    played_on = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, course_name, score, user_id):
        self.course_name = course_name
        self.score = score
        self.played_on = datetime.datetime.now()
        self.user_id = user_id

# flask-marshmallow>=0.12.0 (recommended) not 'ma.ModelSchema'
class RoundSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Round
        load_instance = True