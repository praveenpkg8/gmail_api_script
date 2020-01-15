import datetime

from models.mail import Mail
from services.label_service import LabelService

from apiclient import errors


class MailService:

    @classmethod
    def list_message(cls, service, user_id, total_mails=100):

        try:
            response = service.users().messages().list(
                userId=user_id,
            ).execute()
            messages = []
            if "messages" in response:
                messages.extend(response["messages"])

            total_count = 100
            while "nextPageToken" in response:
                page_token = response["nextPageToken"]
                response = service.users().messages() \
                    .list(
                    userId=user_id,
                    pageToken=page_token
                ).execute()
                if total_count > total_mails:
                    break
                total_count += 100
                messages.extend(response["messages"])

            return messages
        except errors.HttpError as error:
            print("An error occurred: %s" % error)

    @classmethod
    def get_mail(cls, service, user_id, mail_id):
        try:
            message = service.users().messages().get(userId=user_id, id=mail_id).execute()
            return message
        except errors.HttpError as error:
            print("An error occurred: %s" % error)

    @classmethod
    def parse_mail(cls, mail):
        _mail = dict()
        _mail['id'] = mail.get('id')
        headers = mail.get('payload').get('headers')

        for head in headers:
            if head.get('name') == 'From':
                mail = MailService.parse_mail_id(
                    mail_id=head.get('value')
                )
                _mail['sender'] = mail
            if head.get('name') == 'Subject':
                _mail['subject'] = head.get('value')
            if head.get('name') == 'To':
                mail = MailService.parse_mail_id(
                    mail_id=head.get('value')
                )
                _mail['receiver'] = mail
            if head.get('name') == 'Date':
                date_str = head.get('value')
                date_str_updated = date_str.split()[:5]
                date_str_updated = " ".join(date_str_updated)
                try:
                    date_time_obj = datetime.datetime\
                        .strptime(date_str_updated, "%a, %d %b %Y %H:%M:%S")
                except ValueError:
                    date_time_obj = datetime.datetime.now()
                _mail['time_received'] = date_time_obj

        return _mail

    @classmethod
    def update_mail_in_database(cls, service, total_mail, user_id="me"):
        mail_list = MailService.list_message(service, user_id, total_mail)
        for mail in mail_list:
            mail_id = mail.get('id')
            mail = MailService.get_mail(
                service=service,
                user_id="me",
                mail_id=mail_id
            )
            _mail = MailService.parse_mail(mail)
            Mail.create_mail(_mail)

    @classmethod
    def fetch_mail_by_all_metrics(
            cls,
            sender_mail,
            subject,
            time_received=2
    ):
        date_obj = datetime.datetime.now() - datetime.timedelta(days=time_received)
        Mail.filter_by_all_metrics(
            sender_mail=sender_mail,
            subject=subject,
            time_received=date_obj
        )

    @classmethod
    def fetch_mail_by_any_metrics(
            cls,
            sender_mail,
            subject,
            time_received=2
    ):
        date_obj = datetime.datetime.now() - datetime.timedelta(days=time_received)
        Mail.filter_by_any_metrics(
            sender_mail=sender_mail,
            subject=subject,
            time_received=date_obj
        )

    @classmethod
    def parse_mail_id(cls, mail_id):
        if "<" in mail_id and ">" in mail_id:
            import re
            mail = re.search("<(.*)>", mail_id)
            mail = mail.group(1)
            return mail
        return mail_id.strip()
