from database import init_db

from config import get_encrypted_credentials, get_access_token

from services.mail_service import MailService

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

credentials = get_encrypted_credentials()

def main():
    service = get_access_token()
    MailService.update_mail_in_database(service, "me")
    # print(MailService.get_message(service, "me", "16fa1889e1b083b5"))
    print("mail service stored in database")


if __name__ == "__main__":
    init_db()
    main()



