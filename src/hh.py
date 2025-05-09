import requests
from src.base_class import Base

class Head(Base):
    """Класс для работы с hh.ru"""

    def get_data(self):
        response = requests.get(
            url="https://api.hh.ru/vacancies"
        ).json()
        return response['items']


hh_api = Head()
print(hh_api.get_data())
