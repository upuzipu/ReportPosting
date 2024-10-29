from googleapiclient.http import MediaFileUpload

from src.helpers import convert_to_array_of_dicts, get_all_values
from src.model.flow import FlowManager
import pandas as pd


class SheetsManager:

    def __init__(self, flow: FlowManager):
        self.service = flow.get_service()

    def read_sheet(self, spreadsheet_id: str):
        doc_info = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheet_name = doc_info.get('sheets')[0].get('properties').get('title')
        sheet_properties = doc_info.get('sheets')[0].get('properties')
        num_rows = sheet_properties.get('gridProperties').get('rowCount')
        num_cols = sheet_properties.get('gridProperties').get('columnCount')
        range_name = f"{sheet_name}!A1:{chr(64 + num_cols)}{num_rows}"
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_name).execute()
        values = result.get('values', [])
        result_dict = convert_to_array_of_dicts(values)
        return result_dict

    def write_to_google_sheets(self, spreadsheet_id: str, data: list):
        df = pd.DataFrame(data)
        sheet = self.service.spreadsheets()
        value_range_body = {
            "majorDimension": "ROWS",
            "values": df.values.tolist(),
        }
        range_name = 'Лист1!B2:F'
        request = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_name, body=value_range_body,
                                        valueInputOption='USER_ENTERED')
        request.execute()
