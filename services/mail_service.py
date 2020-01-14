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
    def get_message(cls, service, user_id, msg_id):
        try:
            message = service.users().messages().get(userId=user_id, id=msg_id).execute()

            print("Message snippet: %s" % message["snippet"])

            return message
        except errors.HttpError as error:
            print("An error occurred: %s" % error)

