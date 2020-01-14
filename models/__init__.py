import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = db.create_engine('sqlite:///mail.sqlite')
connection = engine.connect()