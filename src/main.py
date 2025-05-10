from src.hh import HeadHunterAPI
from src.vacancies import Vacancy

# подключение и получение данных
hh_api = HeadHunterAPI()
data = hh_api.get_data('python')
vacancy = Vacancy("a", 3000, "e", 'j')
# преобразование в список объектов
obj_list = Vacancy.to_object_list(vacancy, data)
print(obj_list)
