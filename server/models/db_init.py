from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

'''
This file will globalize our aqlalcchemy instance object saved in db. We will be able to use this in any
model in this module to allow us to "inherit" from it when designing our models for the database that conform to
the design we made in the ERD
'''