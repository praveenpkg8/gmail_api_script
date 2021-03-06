import json
import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    "https://mail.google.com/",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels"
]


def get_encrypted_credentials():

    file_path = os.path.join(os.path.abspath("."), 'credentials.json')
    cred_file = open(file_path, 'rb')
    cred = cred_file.read()
    return json.loads(cred)


def get_access_token():

    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            file_path = os.path.join(os.path.abspath("."), 'credentials.json')
            flow = InstalledAppFlow.from_client_secrets_file(
                file_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def load_input_data():
    file_path = os.path.join(os.path.abspath("."), "input.json")
    input_file = open(file_path, "rb")
    input_data = json.load(input_file)
    input_file.close()
    return input_data.get('predicate')
