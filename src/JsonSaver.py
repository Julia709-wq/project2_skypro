import json
import os

from src.json_base_class import JsonBase
from src.vacancies import Vacancy


class JsonSaver(JsonBase):
    """Класс для добавления, удаления и получения вакансий из файла"""

    def __init__(self, file_path: str = "vacancies.json"):
        self.__file_path = file_path

        if not os.path.exists(self.__file_path):
            with open(self.__file_path, "w", encoding='utf-8') as f:
                json.dump([], f)

    def __load_data(self):
        """Метод загрузки данных в файл"""
        with open(self.__file_path, "r", encoding='utf-8') as f:
            return json.load(f)

    def __save_data(self, data):
        """Метод сохранения данных в файл"""
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(data, f)

    def __vacancy_to_dict(self, vacancy: Vacancy):
        """Представление вакансии в виде словаря"""
        return {
            "name": vacancy.name,
            "salary": vacancy.salary,
            "link": vacancy.link,
            "experience": vacancy.experience
        }

    def add_vacancy(self, vacancy: Vacancy):
        """Добавление вакансии в файл"""
        data = self.__load_data()
        vacancy_dict = self.__vacancy_to_dict(vacancy)

        if vacancy_dict not in data:
            data.append(vacancy_dict)
            self.__save_data(data)

    def get_vacancy(self, filters):
        """Получение вакансий по фильтрам"""
        data = self.__load_data()
        result = data
        for k, v in filters.items():
            result = [i for i in result if v.lower() in str(i.get(k, "")).lower()]
        return result

    def delete_vacancy(self, vacancy):
        """Удаление конкретной вакансии из файла"""
        data = self.__load_data()
        vacancy_dict = self.__vacancy_to_dict(vacancy)
        new_data = [i for i in data if i != vacancy_dict]

        self.__save_data(new_data)
