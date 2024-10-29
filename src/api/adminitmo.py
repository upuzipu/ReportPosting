from typing import List, Any, Dict

import requests

from src.model.disciplines import Discipline
from src.helpers import getPlaceId, response_exception


class AdminITMO:
    BASE_URL = "https://admin.itmo.ru/api/admin-sport"
    TOKEN = "TOKEN"
    def __init__(self):
        self.session = requests.Session()

    def post_students(self, students: List[int], competition_id: int):
        result = self.session.post(
            url=f"{self.BASE_URL}/competitions/{competition_id}/students",
            json=students,
            headers={"Authorization": self.TOKEN}
        )
        response_exception(result)
        return result.json()

    def post_result(self, students: List[Dict[str, Any]], competition_id: int,
                    date: str, discipline_name: str):
        for student in students:
            result = self.session.post(
                url=f"{self.BASE_URL}/competitions/{competition_id}/students/{student['ИСУ']}/results",
                json={
                    'date': date,
                    'discipline_id': Discipline[discipline_name].value,
                    'competition_place_id': int(getPlaceId(int(student['Место'])))
                },
                headers={"Authorization": self.TOKEN}
            )
            response_exception(result)
