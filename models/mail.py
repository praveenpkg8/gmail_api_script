import uuid
from models import Base
from sqlalchemy import Column, String, DateTime


class Mail(Base):

    __tablename__ = "mail"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    sender = Column(String)
    receiver = Column(String)
    subject = Column(String)
    to = Column(String)
    time_received = Column(DateTime)

