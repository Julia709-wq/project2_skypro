from src.hh import HeadHunterAPI
from src.JsonSaver import JsonSaver
from src.utils import (filter_by_keywords, filter_by_salary,
                       top_n_vacancies)
from src.vacancies import Vacancy


def user_interaction():
    """Функция взаимодействия с пользователем"""
    hh_api = HeadHunterAPI()
    json_saver = JsonSaver()

    # поисковый запрос (одно слово)
    keyword = input("Введите поисковый запрос: ")
    raw_vac = hh_api.get_data(keyword)

    # преобразование в список объектов
    vacancies = Vacancy.to_object_list(raw_vac)

    # фильтрация по ключевым словам
    keywords = input("Введите ключевые слова для фильтрации через пробел: ").lower().split(" ")
    if keywords:
        vacancies = filter_by_keywords(vacancies, keywords)

    # фильтрация по зарплате
    while True:
        salary_input = input("Введите диапазон зарплат (например: 100000-150000): ")
        if not salary_input:
            print("Пустой ввод. пропускаем фильтрацию по зарплате.")
            break
        try:
            min_salary, max_salary = map(int, salary_input.replace(" ", "").split('-'))
            vacancies = filter_by_salary(vacancies, min_salary, max_salary)
            break
        except ValueError:
            print("Неверный формат зарплаты. Введите снова: ")

    # топ вакансий
    n = int(input("Введите количество вакансий для отображения: "))
    top_vacancies = top_n_vacancies(vacancies, n)

    # сохранение в файл и вывод
    for vac in top_vacancies:
        print(vac)
        print("---" * 20)
        json_saver.add_vacancy(vac)


user_interaction()
