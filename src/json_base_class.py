from abc import ABC, abstractmethod
from src.vacancies import Vacancy


class JsonBase(ABC):
    """Абстрактный класс для работы с файлом"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """Абстрактный метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def get_vacancy(self, filters: dict):
        """Абстрактный метод для получения вакансии из файла"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """Абстрактный метод для удаления вакансии из файла"""
        pass
