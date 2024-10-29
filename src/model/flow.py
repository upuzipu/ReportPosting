import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


class FlowManager:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets',
                       'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('../src/config/credentials.json', self.scopes)

    def get_service(self):
        httpAuth = self.creds.authorize(httplib2.Http())
        return build('sheets', 'v4', http=httpAuth)
