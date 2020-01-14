
from config import get_encrypted_credentials, get_access_token

from services.mail_service import MailService

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

credentials = get_encrypted_credentials()

service = get_access_token()
print(MailService.get_message(service, "me", "16fa1889e1b083b5"))





