from src.utils import (filter_by_keywords, filter_by_salary, sort_by_salary,
                       top_n_vacancies)


def test_filter_by_keywords(sample_vacancies):
    """Проверка фильтрации вакансий по ключевому слову"""
    result = filter_by_keywords(sample_vacancies, ["разработчик"])
    assert len(result) == 2


def test_filter_by_salary(sample_vacancies):
    """Проверка фильтрации вакансий по указанной зарплате"""
    result = filter_by_salary(sample_vacancies, 100000, 160000)
    assert len(result) == 2


def test_filter_by_salary_none(sample_vacancies):
    """Проверка фильтрации вакансий по указанной зарплате для значений None"""
    result = filter_by_salary(sample_vacancies)
    assert len(result) == 4


def test_sort_by_salary(sample_vacancies):
    """Проверка сортировки вакансий по зарплатам"""
    sorted_vacs = sort_by_salary(sample_vacancies)
    assert sorted_vacs[0].name == "Аналитик данных"
    assert sorted_vacs[3].name == "Менеджер"


def test_top_n_vacancies(sample_vacancies):
    """Проверка получения топ N вакансий"""
    result = top_n_vacancies(sample_vacancies, 10)
    assert len(result) == 4
