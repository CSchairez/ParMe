import datetime
from .db_init import db

# we import the db instance here from db_init therefore that means we can inherit from it in N files
# class Test(db.Model):

#     __tablename__ = "test"
    
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     registered_on = db.Column(db.DateTime, nullable=False)
#     admin = db.Column(db.Boolean, nullable=False, default=False)

#     def __init__(self, admin=False):
#         self.registered_on = datetime.datetime.now()
#         self.admin = admin
