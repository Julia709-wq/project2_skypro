import pytest

from src.vacancies import Vacancy


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Backend разработчик", {'from': 100000, 'to': 150000}, "some url", "Python, Django, API development 1-3 года"),
        Vacancy("Frontend разработчик", {'from': 100000, 'to': 120000}, "some url", "React, JavaScript, CSS"),
        Vacancy("Аналитик данных", {'from': 200000, 'to': 250000}, "some url", "Python, ML, statistics"),
        Vacancy("Менеджер", None, "some url", "")
    ]

@pytest.fixture
def vac1():
    return Vacancy("Аналитик данных", {'from': 200000, 'to': 250000}, "some url", "Python, ML, statistics")

@pytest.fixture
def vac1_with_none_salary():
    return Vacancy("Аналитик данных", None, "some url", "Python, ML, statistics")

@pytest.fixture
def vac2():
    return Vacancy("Frontend разработчик", {'from': 130000, 'to': 150000}, "some url", "React, JavaScript, CSS")

@pytest.fixture
def vac3():
    return Vacancy("Специалист по работе с БД", {'from': 130000, 'to': 140000}, "some url", "SQL, MySQL")
