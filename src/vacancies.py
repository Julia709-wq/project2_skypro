class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("_name", "_salary", "_link", "_experience")

    def __init__(self, name: str, salary: int, link: str, experience: str):
        self._name = name
        self._salary = self.__validate_salary(salary)
        self._link = link
        self._experience = experience if experience else "Нет требований"

    @property
    def name(self):
        """Геттер названия вакансии"""
        return self._name

    @property
    def salary(self):
        """Геттер заработной платы"""
        return self._salary

    @property
    def link(self):
        """Геттер ссылки на вакансию"""
        return self._link

    @property
    def experience(self):
        """Геттер опыта работы"""
        return self._experience

    def __repr__(self):
        """Магический метод для вывода информации о вакансии"""
        return f"Название вакансии: {self.name}\nЗарплата: {self._salary}\nСсылка: {self.link}\nТребуемый опыт работы: {self.experience}"

    def __validate_salary(self, salary: int):
        """Метод для валидации зарплаты"""
        if isinstance(salary, dict):
            salary_from = salary.get("from")
            salary_to = salary.get("to")
            return salary_from or salary_to or 0
        else:
            return 0

    def __lt__(self, other):
        """Магический метод для сравнения зарплат (меньше)"""
        return self._salary < other.salary

    def __eq__(self, other):
        """Магический метод для сравнения зарплат (равно)"""
        return self._salary == other.salary

    def __gt__(self, other):
        """Магический метод для сравнения зарплат (больше)"""
        return self._salary > other.salary

    @staticmethod
    def to_object_list(json_data: dict):
        """Метод для преобразования данных в формат списка объектов Vacancies"""
        vacancies_list = []
        for i in json_data:
            name = i.get('name')
            salary = i.get('salary')
            link = i.get('url')
            experience = i.get('snippet', {}).get('requirement', "Не указано")
            vacancies_list.append(Vacancy(name, salary, link, experience))
        return vacancies_list
