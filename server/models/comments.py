import datetime
from .db_init import db
from .ma_init import ma
from sqlalchemy import ForeignKey

class Comments(db.Model):

    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(155), unique=False, nullable=False)
    commmented_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, content, user_id):
        self.content = content
        self. commmented_on = datetime.datetime.now()
        self.user_id = user_id

# flask-marshmallow>=0.12.0 (recommended) not 'ma.ModelSchema'
class CommentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comments
        load_instance = True