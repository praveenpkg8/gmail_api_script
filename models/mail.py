import datetime
from sqlalchemy import Column, String, DateTime

from database import Base, session


class Mail(Base):
    __tablename__ = "mail"

    id = Column(String, primary_key=True)
    sender = Column(String)
    receiver = Column(String)
    subject = Column(String)
    time_received = Column(DateTime)

    @staticmethod
    def create_mail(mail):
        _mail = Mail(
            id=mail.get('id'),
            sender=mail.get('sender'),
            receiver=mail.get('receiver'),
            subject=mail.get('subject'),
            time_received=mail.get('time_received')
        )
        session.add(_mail)
        session.commit()

    @staticmethod
    def query_mail():
        mail = session.query(Mail)
        return mail
