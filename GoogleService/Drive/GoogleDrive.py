from __future__ import print_function
import pickle, shutil, os.path, io, os

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']

class GoogleAPI:

    def __init__(self, credentials_path, token_path):
        self.connection = self.connect(credentials_path, token_path)
    
    @staticmethod
    def connect(self, credentials_path='./credentials.json', token_path='./token.pickle'):
        creds = None
        if os.path.exists(token_path):
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)
        return service
    
    def createFolder(self, title):
        file_metadata = {
            'name': title,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.connection.files().create(body=file_metadata,fields='id').execute()

    def downloadChilds(self, fileID, output_file_path):
        request = self.connection.files().get_media(fileId=fileID)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

        # The file has been downloaded into RAM, now save it in a file
        fh.seek(0)
        with open(output_file_path, 'wb') as f:
            shutil.copyfileobj(fh, f, length=131072)

    def SearchFile(self, q):
        page_token = None
        found_files = []
        while True:
            response = self.connection.files().list(q=q,
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=page_token).execute()
            for file in response.get('files', []):
                found_files.append([file.get('name'), file.get('id')])
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return found_files

    def find_folder(self, folder_name):
        q_folder = "name contains '%s' and mimeType= 'application/vnd.google-apps.folder'" % folder_name
        folders = self.SearchFile(q_folder)
        folder_name = folders[0][0]
        folder_id = folders[0][1]
        return folders
    
    def find_childs(self, folder_id):
        q_child = "'%s' in parents" % folder_id
        childs = self.SearchFile(q_child)
        return childs
    
    def download_folder_content(self, folder_name):
        folder_id = self.find_folder(folder_name)[0][1]
        childs = self.find_childs(folder_id)
        
        for index, child in enumerate(childs):
            child_id = child[1]
            output_path = './%s' % child[0]
            self.downloadChilds(child_id, output_path)




