
def test_init_vacancy(vac1):
    """Проверка инициализации объекта класса Vacancy"""
    assert vac1.name == "Аналитик данных"
    assert vac1.salary == 200_000
    assert vac1.link == "some url"
    assert vac1.experience == "Python, ML, statistics"


def test_init_vacancy_none_salary(vac1_with_none_salary):
    """Проверка инициализации объекта класса Vacancy с неуказанной зарплатой"""
    assert vac1_with_none_salary.salary == 0


def test_repr(vac1):
    """Проверка работы магического метода __repr__"""
    result = vac1.__repr__()
    assert result == ("Название вакансии: Аналитик данных\nЗарплата: 200000\n"
                      "Ссылка: some url\nТребуемый опыт работы: Python, ML, statistics")


def test_salary_comparison(vac1, vac2, vac3):
    """Проверка сравнения зарплат"""
    assert vac1 > vac2
    assert vac2 == vac3
    assert vac3 < vac1
