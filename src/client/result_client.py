from typing import Any, Dict, List

from src.api.google_sheets import SheetsManager
from src.model.flow import FlowManager
from src.api.adminitmo import AdminITMO


class ResultPostingClient:
    def __init__(self):
        self.flow = FlowManager()
        self.sheets = SheetsManager(self.flow)
        self.admin_itmo = AdminITMO()

    def put_data_in_report(self, spreadsheet_id_form: str, spreadsheet_id_report: str) -> List[Dict[str, Any]]:
        data = self.sheets.read_sheet(spreadsheet_id_form)
        self.sheets.write_to_google_sheets(spreadsheet_id_report, data)
        return data

    def put_data_in_admin(self, competition_id: int, discipline_name: str, data: List[Dict[str, Any]], date: str):
        ISU = []
        for item in data:
            ISU.append(int(item['ИСУ']))
        print(ISU, competition_id)
        self.admin_itmo.post_students(ISU, competition_id)
        self.admin_itmo.post_result(data, competition_id, date, discipline_name)

