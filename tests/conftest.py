import pytest

from src.vacancies import Vacancy
from src.JsonSaver import JsonSaver


@pytest.fixture
def sample_vacancies() -> list:
    return [
        Vacancy("Backend разработчик", {'from': 100000, 'to': 150000}, "some url", "Python, Django, API development 1-3 года"),
        Vacancy("Frontend разработчик", {'from': 100000, 'to': 120000}, "some url", "React, JavaScript, CSS"),
        Vacancy("Аналитик данных", {'from': 200000, 'to': 250000}, "some url", "Python, ML, statistics"),
        Vacancy("Менеджер", None, "some url", "")
    ]


@pytest.fixture
def vac1() -> Vacancy:
    return Vacancy("Аналитик данных", {'from': 200000, 'to': 250000}, "some url", "Python, ML, statistics")


@pytest.fixture
def vac1_with_none_salary() -> Vacancy:
    return Vacancy("Аналитик данных", None, "some url", "Python, ML, statistics")


@pytest.fixture
def vac2() -> Vacancy:
    return Vacancy("Frontend разработчик", {'from': 130000, 'to': 150000}, "some url", "React, JavaScript, CSS")


@pytest.fixture
def vac3():
    return Vacancy("Специалист по работе с БД", {'from': 130000, 'to': 140000}, "some url", "SQL, MySQL")


@pytest.fixture
def sample_api_response() -> dict:
    return {
        "items": [
            {"name": "Backend разработчик", "salary": {'from': 100000, 'to': 150000}},
            {"name": "Frontend разработчик", "salary": {'from': 80000, 'to': 100000}}
        ]
    }


@pytest.fixture
def sample_json_file(tmp_path) -> str:
    file_path = tmp_path / "test_vacancies.json"
    file_path.write_text("[]", encoding="utf-8")
    return str(file_path)


@pytest.fixture
def json_saver(sample_json_file) -> JsonSaver:
    return JsonSaver(file_path=sample_json_file)
