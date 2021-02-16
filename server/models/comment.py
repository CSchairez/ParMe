import datetime
from .db_init import db
from .ma_init import ma
from sqlalchemy.orm import relationship


class Comment(db.Model):

    __tablename__ = 'comment'

    content = db.Column(db.String(125), unique=False, nullable=False)
    commmented_on = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('round.user_id'))