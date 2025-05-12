def filter_by_keywords(vacancies: list, keywords: list) -> list:
    """Функция фильтрации вакансий по ключевым словам"""
    filtered = []
    for v in vacancies:
        name = v.name.lower() if v.name else ""
        experience = v.experience.lower() if v.experience else ""
        if any(w in name or w in experience for w in keywords):
            filtered.append(v)
    return filtered


def filter_by_salary(vacancies: list, min_salary=0, max_salary=1_000_000) -> list:
    """Фильтрация по диапазону зарплат"""
    filtered = [
        v for v in vacancies
        if isinstance(v.salary, int) and min_salary <= v.salary <= max_salary
    ]
    return filtered


def sort_by_salary(vacancies: list, reverse=True) -> list:
    """Сортировка вакансий по зарплате"""
    return sorted(
        [v for v in vacancies if isinstance(v.salary, int)],
        key=lambda v: v.salary,
        reverse=reverse
    )


def top_n_vacancies(vacancies: list, n: int) -> list:
    """Получение топ-N вакансий"""
    sorted_vac = sort_by_salary(vacancies)
    return sorted_vac[:n]
