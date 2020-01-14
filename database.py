from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///mail.db', echo=True)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
