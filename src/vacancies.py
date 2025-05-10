
class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("__name", "__salary", "__link", "__experience")

    def __init__(self, name: str, salary: int, link: str, experience: str):
        self.__name = name
        self.__salary = self.__validate_salary(salary)
        self.__link = link
        self.__experience = experience

    def __validate_salary(self, salary):
        """Метод для валидации зарплаты"""
        if isinstance(salary, dict):
            salary_from = salary.get("from")
            salary_to = salary.get("to")
            return salary_from or salary_to or 0
        elif isinstance(salary, None):
            return 0

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __eq__(self, other):
        return self.__salary == other.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary

    def to_object_list(self, json_data):
        """Метод для преобразования данных в формат списка объектов Vacancies"""
        vacancies_list = []
        for i in json_data:
            name = i.get('name')
            salary = i.get('salary')
            link = i.get('url')
            experience = i.get('snippet', {}).get('requirement', "Не указано")
            vacancies_list.append(Vacancy(name, salary, link, experience))
        return vacancies_list



