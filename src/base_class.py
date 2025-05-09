from abc import ABC, abstractmethod

class Base(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_data(self):
        pass


