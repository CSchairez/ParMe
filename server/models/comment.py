import datetime
from .db_init import db
from .ma_init import ma
from sqlalchemy import ForeignKey

class Comment(db.Model):

    __tablename__ = "comment"

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(155), unique=False, nullable=False)
    commented_on = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)


    def __init__(self, content, user_id):
        self.content = content
        self. commented_on = datetime.datetime.now()
        self.user_id = user_id

# flask-marshmallow>=0.12.0 (recommended) not 'ma.ModelSchema'
class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True