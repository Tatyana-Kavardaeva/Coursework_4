import pytest

from src.utils import get_list_vacancies, sort_by_salary, top_list_vacancies
from src.class_vacancy import Vacancy


def test_get_list_vacancies(data):
    assert get_list_vacancies(data) == [Vacancy(name=f'Python developer (Junior)', salary={'from': 50000, 'to': None, 'currency': 'RUR', 'gross': False}, url=f'https://hh.ru/vacancy/101219641'),
                                        Vacancy(name=f'Стажер IT направления', salary={'from': 70000, 'to': 70000, 'currency': 'RUR', 'gross': True}, area=f'Москва', url=f'https://hh.ru/vacancy/101287743')]


def test_sort_by_salary(list_vacancies):
    assert sort_by_salary(list_vacancies) == [Vacancy(name=f'Стажер IT направления', salary={'from': 70000, 'to': 70000, 'currency': 'RUR', 'gross': True}, area=f'Москва', url=f'https://hh.ru/vacancy/101287743'),
                                              Vacancy(name=f'Python developer (Junior)', salary={'from': 50000, 'to': None, 'currency': 'RUR', 'gross': False}, area=f'Владивосток', url=f'https://hh.ru/vacancy/101219641')]


def test_top_list_vacancies(list_vacancies, n):
    assert len(top_list_vacancies(list_vacancies, n)) == n
