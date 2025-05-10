from abc import ABC, abstractmethod

class BaseAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def connect_(self, params: dict):
        pass

    @abstractmethod
    def get_data(self, keyword: str):
        pass
