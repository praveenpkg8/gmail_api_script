import datetime

from models.mail import Mail

from apiclient import errors


class MailService:

    @classmethod
    def list_message(cls, service, user_id, total_mails=50):

        try:
            response = service.users().messages().list(
                userId=user_id,
                maxResults=10
            ).execute()
            messages = []
            if "messages" in response:
                messages.extend(response["messages"])

            total_count = 10
            while "nextPageToken" in response:
                page_token = response["nextPageToken"]
                response = service.users().messages() \
                    .list(
                    userId=user_id,
                    maxResults=10,
                    pageToken=page_token
                ).execute()
                if total_count == total_mails:
                    break
                total_count += 10
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
                _mail['sender'] = head.get('value')
            if head.get('name') == 'Subject':
                _mail['subject'] = head.get('value')
            if head.get('name') == 'To':
                _mail['receiver'] = head.get('value')
            if head.get('name') == 'Date':
                date_str = head.get('value')
                date_str_updated = date_str.split()[:5]
                date_str_updated = " ".join(date_str_updated)
                date_time_obj = datetime.datetime.strptime(date_str_updated, "%a, %d %b %Y %H:%M:%S")
                _mail['time_received'] = date_time_obj.strftime('%s')

        return _mail

    @classmethod
    def update_mail_in_database(cls, service, user_id="me", ):
        mail_list = MailService.list_message(service, user_id)
        for mail in mail_list:
            mail_id = mail.get('id')
            mail = MailService.get_mail(
                service=service,
                user_id="me",
                mail_id=mail_id
            )
            _mail = MailService.parse_mail(mail)
            Mail.create_mail(_mail)
