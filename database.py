from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:password@localhost/mail',
                       echo=True)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)
