from src.utils import get_list_vacancies
from src.class_abstractfile import AbstractFile
from src.class_vacancy import Vacancy
import json
import os


class JsonFile(AbstractFile):
    """Класс для работы с объектами вакансий в JSON-файле"""

    def __init__(self, file_path):
        super().__init__(file_path)

    @staticmethod
    def vacancy_to_json(vacancy):
        return vacancy.__dict__

    @staticmethod
    def json_to_vacancy(json_vacancy):
        return Vacancy(json_vacancy['name'], json_vacancy['salary'], json_vacancy['area'], json_vacancy['url'])

    def write_vacancies(self, vacancies_list):
        """ Записывет список вакансий """
        vacancies = [self.vacancy_to_json(vacancy) for vacancy in vacancies_list]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        """ Добавляет вакансию, если файл уже существует.
        Если отсутствует - создает файл и записывает данные """
        vacancies = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                vacancies = json.load(f)
        except FileNotFoundError:
            pass
        vacancies.append(self.vacancy_to_json(vacancy))
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies_by_criteria(self, criterias: list) -> list:
        """ Получает список экземпляров класса Vacancy по заданному критерию"""
        list_get_vacancies = []
        with open(self.file_path, "r", encoding="utf-8") as f:
            vacancies = json.load(f)
        if not criterias:
            return get_list_vacancies(vacancies)
        else:
            for vacancy in vacancies:
                if any(criteria.lower() in str(value).lower() for value in vacancy.values() for criteria in criterias):
                    list_get_vacancies.append(self.json_to_vacancy(vacancy))
        return list_get_vacancies

    def delete_vacancy(self, name):
        """ Удаляет вакансию по названию"""
        with open(self.file_path, "r", encoding="utf-8") as f:
            vacancies = json.load(f)
        updated_vacancies = [vacancy for vacancy in vacancies if vacancy.get('name') != name]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(updated_vacancies, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    path = os.path.join(data_dir, "vacancies.json")

    vacancy_1 = Vacancy("Тест1")
    js_file = JsonFile(path)
    # js_file.add_vacancy(vacancy_1)
    js_file.delete_vacancy("Тест1")
