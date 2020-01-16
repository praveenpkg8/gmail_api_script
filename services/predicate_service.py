import datetime

from sqlalchemy import and_, or_

from models.mail import Mail


class PredicateService:

    @classmethod
    def all_predicate(cls, config, details):
        mail = Mail.query_mail()

        if config.get('sender') == "CONTAINS" and \
                config.get('subject') == "CONTAINS":
            _mail = PredicateService.contains_sender_and_subject(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('sender') == "CONTAINS":
            _mail = PredicateService.contains_sender(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('subject') == "CONTAINS":
            _mail = PredicateService.contains_subject(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('sender') == "EQUALS" and \
                config.get('subject') == "EQUALS":
            _mail = PredicateService.equals_sender_and_subject(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('sender') == "NOTEQUALS":
            _mail = PredicateService.not_equals_sender(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('subject') == "NOTEQUALS":
            _mail = PredicateService.not_equals_subject(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

    @classmethod
    def contains_sender_and_subject(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                and_(
                    Mail.sender.contains(details.get('sender')),
                    Mail.subject.contains(details.get('subject')),
                    Mail.time_received > days
                )
            ).first()

            return _mail

        else:
            _mail = mail.filter(
                and_(
                    Mail.sender.contains(details.get('sender')),
                    Mail.subject.contains(details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail

    @classmethod
    def contains_sender(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                and_(
                    Mail.sender.contains(details.get('sender')),
                    Mail.subject == details.get('subject'),
                    Mail.time_received > days

                )
            ).first()

            return _mail

        else:
            _mail = mail.filter(
                and_(
                    Mail.sender.contains(details.get('sender')),
                    Mail.subject == details.get('subject'),
                    Mail.time_received < days

                )
            ).first()

            return _mail

    @classmethod
    def contains_subject(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                and_(
                    Mail.sender == details.get('sender'),
                    Mail.subject.contains(details.get('subject')),
                    Mail.time_received > days
                )
            ).first()

            return _mail

        else:
            _mail = mail.filter(
                and_(
                    Mail.sender == details.get('sender'),
                    Mail.subject.contains(details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail


    @classmethod
    def equals_sender_and_subject(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                and_(
                    Mail.sender == details.get('sender'),
                    Mail.subject == (details.get('subject')),
                    Mail.time_received > days
                )
            ).first()
            return _mail

        else:
            _mail = mail.filter(
                and_(
                    Mail.sender == details.get('sender'),
                    Mail.subject == (details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail

    @classmethod
    def not_equals_sender(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                and_(
                    Mail.sender != details.get('sender'),
                    Mail.subject == (details.get('subject')),
                    Mail.time_received > days
                )
            ).first()

            return _mail

        else:
            _mail = mail.filter(
                and_(
                    Mail.sender != details.get('sender'),
                    Mail.subject == (details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail

    @classmethod
    def not_equals_subject(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                and_(
                    Mail.sender == details.get('sender'),
                    Mail.subject != (details.get('subject')),
                    Mail.time_received > days
                )
            ).first()
            return _mail
        else:
            _mail = mail.filter(
                and_(
                    Mail.sender == details.get('sender'),
                    Mail.subject != (details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail

    @classmethod
    def any_predicate(cls, config, details):
        mail = Mail.query_mail()

        if config.get('sender') == "CONTAINS" and \
                config.get('subject') == "CONTAINS":
            _mail = PredicateService.contains_any_sender_and_subject(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('sender') == "CONTAINS":
            _mail = PredicateService.contains_any_sender(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('subject') == "CONTAINS":
            _mail = PredicateService.contains_any_subject(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('sender') == "EQUALS" and \
                config.get('subject') == "EQUALS":
            _mail = PredicateService.equals_any_sender_and_subject(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('sender') == "NOTEQUALS":
            _mail = PredicateService.not_equals_any_sender(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

        elif config.get('subject') == "NOTEQUALS":
            _mail = PredicateService.not_equals_any_subject(
                mail=mail,
                is_lesser=config.get('is_lesser'),
                details=details
            )
            return _mail

    @classmethod
    def contains_any_sender_and_subject(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                or_(
                    Mail.sender.contains(details.get('sender')),
                    Mail.subject.contains(details.get('subject')),
                    Mail.time_received > days
                )
            ).first()

            return _mail

        else:
            _mail = mail.filter(
                or_(
                    Mail.sender.contains(details.get('sender')),
                    Mail.subject.contains(details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail

    @classmethod
    def contains_any_sender(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                or_(
                    Mail.sender.contains(details.get('sender')),
                    Mail.subject == details.get('subject'),
                    Mail.time_received > days

                )
            ).first()

            return _mail

        else:
            _mail = mail.filter(
                or_(
                    Mail.sender.contains(details.get('sender')),
                    Mail.subject == details.get('subject'),
                    Mail.time_received < days

                )
            ).first()

            return _mail

    @classmethod
    def contains_any_subject(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                or_(
                    Mail.sender == details.get('sender'),
                    Mail.subject.contains(details.get('subject')),
                    Mail.time_received > days
                )
            ).first()

            return _mail

        else:
            _mail = mail.filter(
                or_(
                    Mail.sender == details.get('sender'),
                    Mail.subject.contains(details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail

    @classmethod
    def equals_any_sender_and_subject(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                or_(
                    Mail.sender == details.get('sender'),
                    Mail.subject == (details.get('subject')),
                    Mail.time_received > days
                )
            ).first()
            return _mail

        else:
            _mail = mail.filter(
                or_(
                    Mail.sender == details.get('sender'),
                    Mail.subject == (details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail

    @classmethod
    def not_equals_any_sender(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                or_(
                    Mail.sender != details.get('sender'),
                    Mail.subject == (details.get('subject')),
                    Mail.time_received > days
                )
            ).first()

            return _mail

        else:
            _mail = mail.filter(
                or_(
                    Mail.sender != details.get('sender'),
                    Mail.subject == (details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail

    @classmethod
    def not_equals_any_subject(cls, mail, is_lesser, details):
        days = datetime.datetime.now() - datetime.timedelta(details.get('time_received'))
        if is_lesser:
            _mail = mail.filter(
                or_(
                    Mail.sender == details.get('sender'),
                    Mail.subject != (details.get('subject')),
                    Mail.time_received > days
                )
            ).first()
            return _mail
        else:
            _mail = mail.filter(
                or_(
                    Mail.sender == details.get('sender'),
                    Mail.subject != (details.get('subject')),
                    Mail.time_received < days
                )
            ).first()

            return _mail
