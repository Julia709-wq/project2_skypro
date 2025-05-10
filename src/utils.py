def filter_by_keywords(vacancies, keywords):
    """Функция фильтрации вакансий по ключевым словам"""
    filtered = []
    for v in vacancies:
        name = v.name.lower() if v.name else ""
        experience = v.experience.lower() if v.experience else ""
        if any(w in name or w in experience for w in keywords):
            filtered.append(v)
    return filtered


def filter_by_salary(vacancies, min_salary=0, max_salary=1_000_000):
    """Фильтрация по диапазону зарплат"""
    filtered = [
        v for v in vacancies
        if isinstance(v.salary, int) and min_salary <= v.salary <= max_salary
    ]
    return filtered


def sort_by_salary(vacancies, reverse=True):
    """Сортировка вакансий по зарплате"""
    return sorted(
        [v for v in vacancies if isinstance(v.salary, int)],
        key=lambda v: v.salary,
        reverse=reverse
    )


def top_n_vacancies(vacancies, n):
    """Получение топ-N вакансий"""
    sorted_vac = sort_by_salary(vacancies)
    return sorted_vac[:n]
