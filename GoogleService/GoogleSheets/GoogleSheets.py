from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class GoogleSheetsService:

    
    def __init__(self, credentials_path, token_path):
        self.connection = self.connect(credentials_path, token_path)


    def connect(self, credentials_path='./credentials.json', token_path='./token.pickle'):
        creds = None
        if os.path.exists(token_path):
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)

            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        return service.spreadsheets()


    def read(self, sheetID, range):
        try:
            result = self.connection.values().get(spreadsheetId=sheetID, range=range, valueRenderOption='FORMATTED_VALUE').execute()
            values = result.get('values', [])
            if not values:
                return []

            else:
                return values

        except Exception as e:
            raise e


    def write(self, sheetID, range, value_matrix, major_dimension='ROWS'):

        value_range_body = {
            'majorDimension': major_dimension,
            'values': value_matrix,
        }

        self.connection.values().update(
            spreadsheetId=sheetID,
            valueInputOption='USER_ENTERED',
            range=range,
            body=value_range_body,
        ).execute()


