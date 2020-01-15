from sqlalchemy import Column, String, DateTime, and_, or_

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
    def filter_by_all_metrics(
            sender_mail,
            subject,
            time_received

    ):
        mail = session.query(Mail).filter(and_(
            Mail.sender.like(sender_mail),
            Mail.subject == subject,
            Mail.time_received > time_received
        )).one()
        print(mail.subject)
        return mail

    @staticmethod
    def filter_by_any_metrics(
            sender_mail,
            subject,
            time_received
    ):
        mail = session.query(Mail).filter(
            Mail.time_received > time_received, or_(
                Mail.sender.like(sender_mail),
                Mail.subject == subject,
            )).one()
        print(mail.subject)
        return mail

    @staticmethod
    def get_labels_by_id(
            id
    ):
        mail = session.query(Mail).get(id)
        return mail.labels
