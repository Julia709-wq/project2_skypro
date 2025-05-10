from src.utils import (filter_by_keywords, filter_by_salary, sort_by_salary,
                       top_n_vacancies)


def test_filter_by_keywords(sample_vacancies):
    result = filter_by_keywords(sample_vacancies, ["разработчик"])
    assert len(result) == 2

def test_filter_by_salary(sample_vacancies):
    result = filter_by_salary(sample_vacancies, 100000, 160000)
    assert len(result) == 2

def test_filter_by_salary_none(sample_vacancies):
    result = filter_by_salary(sample_vacancies)
    assert len(result) == 4

def test_sort_by_salary(sample_vacancies):
    sorted_vacs = sort_by_salary(sample_vacancies)
    assert sorted_vacs[0].name == "Аналитик данных"
    assert sorted_vacs[3].name == "Менеджер"

def test_top_n_vacancies(sample_vacancies):
    result = top_n_vacancies(sample_vacancies, 10)
    assert len(result) == 4
