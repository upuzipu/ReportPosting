import os

from src.api.adminitmo import AdminITMO
from src.api.google_sheets import SheetsManager
from src.model.flow import FlowManager
from src.model.disciplines import Discipline

sheets = SheetsManager(FlowManager())

# data = sheets.read_sheet('1Nwc84JbeQtKfMDDsyrh1k_tiG5hvju-mmadN9uNsQoU')
# print(data)
# sheets.write_to_google_sheets("1omRSaYjAc0Dy4l7XQT7WoIWlyfVzRsaQE2Uw0CNlB8Q", data)
admin = AdminITMO()
# admin.post_students([335042, 247920], 2028)
data = [{'ФИО': 'Новиков Егор Романович', 'Ссылка на вк': 'vk.com/upuzipu', 'ИСУ': '335042', 'Группа': 'P34111',
         'Место': 1},
        {'ФИО': 'Кирпиченко Даниил Александрович', 'Ссылка на вк': 'vk.com/ko1lness', 'ИСУ': '247920',
         'Группа': 'K34212', 'Место': 2}]
admin.post_result(data, 2028, "2024-10-26", "DEADLOCK")
