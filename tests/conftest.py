import pytest
import os

from src.class_vacancy import Vacancy
from src.class_jsonfile import JsonFile


@pytest.fixture()
def vacancy1():
    return Vacancy(name='Тест', salary=None, area='Тест', url='test@test.test')


@pytest.fixture()
def vacancy2():
    return Vacancy(name='Тест2', salary={'from': 70000, 'to': None, 'currency': 'RUR', 'gross': False}, area='Тест2',
                   url='test2@test.test')


@pytest.fixture()
def vacancy3():
    return Vacancy(name='Тест3', salary={'from': None, 'to': 110000, 'currency': 'RUR', 'gross': True}, area='Тест3',
                   url='test3@test.test')


@pytest.fixture()
def vacancy4():
    return Vacancy(name='Тест4', salary={'from': 50000, 'to': 50000, 'currency': 'RUR', 'gross': True}, area='Тест4',
                   url='test4@test.test')


@pytest.fixture()
def data():
    data = [{'id': '101219641', 'premium': False, 'name': 'Python developer (Junior)', 'department': None,
             'has_test': False, 'response_letter_required': False,
             'area': {'id': '22', 'name': 'Владивосток', 'url': 'https://api.hh.ru/areas/22'},
             'salary': {'from': 50000, 'to': 50000, 'currency': 'RUR', 'gross': True},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Владивосток', 'street': 'проспект 100 лет Владивостоку', 'building': '155',
                         'lat': 43.179069, 'lng': 131.91874, 'description': None,
                         'raw': 'Владивосток, проспект 100 лет Владивостоку, 155', 'metro': None, 'metro_stations': [],
                         'id': '12414444'}, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-06-04T08:03:23+0300', 'created_at': '2024-06-04T08:03:23+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=101219641',
             'branding': {'type': 'MAKEUP', 'tariff': None}, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/101219641?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/101219641', 'relations': [],
             'employer': {'id': '9311920', 'name': 'DNS Технологии', 'url': 'https://api.hh.ru/employers/9311920',
                          'alternate_url': 'https://hh.ru/employer/9311920', 'logo_urls': None,
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9311920',
                          'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Знание основных концепций <highlighttext>Python</highlighttext>. Опыт написания сервисов на Flask и FastAPI (коммерческий или учебный). Опыт работы с базами данных (коммерческий...',
            'responsibility': 'Разработка новых и поддержка существующих Api и web-приложений на FastAPI / Flask. Работа в PostgreSQL. Написание телеграм ботов. '},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '101287743', 'premium': False, 'name': 'Стажер IT направления',
             'department': {'id': 'mts-3776-main', 'name': '«МТС» '}, 'has_test': False,
             'response_letter_required': False,
             'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': 70000, 'to': None, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Москва', 'street': 'Панкратьевский переулок', 'building': '12/12', 'lat': 55.771874,
                         'lng': 37.63588, 'description': None, 'raw': 'Москва, Панкратьевский переулок, 12/12',
                         'metro': None, 'metro_stations': [], 'id': '709808'}, 'response_url': None,
             'sort_point_distance': None, 'published_at': '2024-06-04T18:52:13+0300',
             'created_at': '2024-06-04T18:52:13+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=101287743',
             'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/101287743?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/101287743', 'relations': [],
             'employer': {'id': '3776', 'name': 'МТС', 'url': 'https://api.hh.ru/employers/3776',
                          'alternate_url': 'https://hh.ru/employer/3776',
                          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1077164.png',
                                        '240': 'https://img.hhcdn.ru/employer-logo/5929286.png',
                                        '90': 'https://img.hhcdn.ru/employer-logo/5929285.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3776',
                          'accredited_it_employer': True, 'trusted': True}, 'snippet': {
                'requirement': 'Знаешь SQL или PostgreSQL. Готов учиться новому. Мы хотели бы видеть интересующегося и трудолюбивого сотрудника, разделяющего ценности команды и одинаково...',
                'responsibility': 'В разработке lowcode функций (FaaS) на языке Golang. Займешься настройкой маппинга IT-систем. Будешь лидировать собственные проекты по оптимизации и...'},
             'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
             'accept_incomplete_resumes': True, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
             'employment': {'id': 'probation', 'name': 'Стажировка'}, 'adv_response_url': None, 'is_adv_vacancy': False,
             'adv_context': None}]
    return data


@pytest.fixture()
def list_vacancies():
    list_vacancies = [Vacancy(name=f'Python developer (Junior)', salary={'from': 50000, 'to': None, 'currency': 'RUR', 'gross': False}, area=f'Владивосток', url=f'https://hh.ru/vacancy/101219641'), Vacancy(name='Стажер IT направления', salary={'from': 70000, 'to': 70000, 'currency': 'RUR', 'gross': True}, area=f'Москва', url=f'https://hh.ru/vacancy/101287743')]
    return list_vacancies


@pytest.fixture()
def n():
    return 1


@pytest.fixture()
def file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, "test_vacancies.json")
    return file_path


@pytest.fixture()
def js_file(file_path):
    js_file = JsonFile(file_path)
    return js_file


@pytest.fixture()
def criteria():
    criteria = ["Стажер", "Москва"]
    return criteria

