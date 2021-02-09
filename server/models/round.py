import datetime
from .db_init import db
from sqlalchemy import ForeignKey

class Round(db.Model):

    __tablename__ = "round"
    
    round_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course = db.Column(db.String(25), unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    played_on = db.Column(db.DateTime, nullable=False)
    golfer_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, course, score, golfer_id):
        self.course = course
        self.score = score
        self.played_on = datetime.datetime.now()
        self.golfer_id = golfer_id