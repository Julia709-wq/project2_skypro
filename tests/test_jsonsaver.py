import json

def test_add_vacancy(json_saver, vac1, sample_json_file):
    json_saver.add_vacancy(vac1)

    with open(sample_json_file, "r", encoding='utf-8') as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["name"] == "Аналитик данных"

def test_delete_vacancy(json_saver, vac1, sample_json_file):
    json_saver.delete_vacancy(vac1)

    with open(sample_json_file, "r", encoding='utf-8') as file:
        data = json.load(file)

    assert len(data) == 0

def test_get_vacancy(json_saver, sample_vacancies, sample_json_file):
    for vac in sample_vacancies:
        json_saver.add_vacancy(vac)

    result = json_saver.get_vacancy({"name": "разработчик"})

    assert len(result) == 2