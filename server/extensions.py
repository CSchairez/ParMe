from flask_sqlalchemy import SQLAlchemy
import pymysql
db = SQLAlchemy()
db = pymysql.connect(host='database-1.cx8lvdttf77k.us-west-1.rds.amazonaws.com', user='admin', password='1qaz!2wsx!qwe#2', database='parme')