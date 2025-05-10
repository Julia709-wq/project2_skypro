from abc import ABC, abstractmethod


class JsonBase(ABC):
    """Абстрактный класс для работы с файлом"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy(self, filters):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
