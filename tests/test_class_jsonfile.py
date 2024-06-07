import json


def test_write_vacancies(js_file, list_vacancies):
    js_file.write_vacancies(list_vacancies)
    with open(js_file.file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == len(list_vacancies)
        for i, vacancy in enumerate(list_vacancies):
            assert data[i] == vacancy.__dict__


def test_add_vacancy(js_file, vacancy1):
    js_file.add_vacancy(vacancy1)
    with open(js_file.file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 3


def test_delete_vacancy(js_file, vacancy1):
    js_file.delete_vacancy(vacancy1.name)
    with open(js_file.file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 2


def test_get_vacancies_by_criteria(js_file, criteria):
    assert len(js_file.get_vacancies_by_criteria(criteria)) == 1
