from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
from urllib.error import HTTPError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']

class GmailService:
    def __init__(self, credentials_path, token_path):
        self.connection = self.connect(credentials_path, token_path)

    def connect(self, credentials_path, token_path):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)

        # If there are no (valid) credentials available, let the user log in.]
        if not creds: # or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_path, 'w') as token:
                token.write(creds.to_json())

        service = build('gmail', 'v1', credentials=creds)
        return service

    def getLabels(self):
        # Call the Gmail API
        results = self.connection.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])
    
    def createMessage(self, sender, to, subject, message_text):
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        msg = MIMEText(message_text)
        message.attach(msg)
        return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('utf-8')}


    def createMessageHtml(self, sender, to, subject, msgHtml, msgPlain):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to
        msg.attach(MIMEText(msgPlain, 'plain'))
        msg.attach(MIMEText(msgHtml, 'html'))
        return {'raw': base64.urlsafe_b64encode(msg.as_string().encode('utf-8')).decode('utf-8')}

    def sendMail(self, user_id, message):
        """Send an email message.

        Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            message: Message to be sent.

        Returns:
            Sent Message.
        """
        try:
            message = (self.connection.users().messages().send(userId=user_id, body=message)
                    .execute())
            print('Message Id: %s' % message['id'])
            return message

        except HTTPError as error:
            print('An error occurred: %s' % error)
