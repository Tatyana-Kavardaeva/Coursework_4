from src.class_vacancy import Vacancy
import os


def get_list_vacancies(data_vacancies) -> list:
    """Формирует список экземпляров класса Vacancy"""
    # hh_api = HeadHunterAPI("https://api.hh.ru/vacancies")
    list_vacancies = []
    for vacancy in data_vacancies:
        vacancy_ob = Vacancy(vacancy.get('name'), vacancy.get('salary'), vacancy.get('snippet'),
                             vacancy.get('area'), vacancy.get('alternate_url'))
        list_vacancies.append(vacancy_ob)
    return list_vacancies


def sort_by_salary(vacancies: list) -> list:
    """ Сортирует список вакансий по минимальной зарплате от наибольшего значения к наименьшему"""
    sorted_vacancies = sorted(vacancies, key=lambda x: x.salary_min, reverse=True)
    return sorted_vacancies


def top_list_vacancies(vacancies: list, n: int) -> str:
    """ Формирует список топ N вакансий"""
    try:
        vacancies = vacancies[:int(n)]
        return vacancies
    except TypeError:
        return "Невозможно осуществить выборку. Количество вакансий должно быть числом"
    except ValueError:
        return "Невозможно осуществить выборку. Количество вакансий должно быть числом"


if __name__ == "__main__":
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
            {'id': '99030444', 'premium': False, 'name': 'Data Scientist (Senior)',
             'department': {'id': '4649269-4649269-bigdata', 'name': 'ГК Иннотех | Большие данные'},
             'has_test': False, 'response_letter_required': False,
             'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
             'salary': None, 'type': {'id': 'open', 'name': 'Открытая'},
             'address': None, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-05-15T12:09:23+0300', 'created_at': '2024-05-15T12:09:23+0300',
             'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=99030444',
             'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True,
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/99030444?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/99030444', 'relations': [],
             'employer': {'id': '4649269', 'name': 'Т1', 'url': 'https://api.hh.ru/employers/4649269',
                          'alternate_url': 'https://hh.ru/employer/4649269',
                          'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6590382.png',
                                        '90': 'https://img.hhcdn.ru/employer-logo/6590381.png',
                                        'original': 'https://img.hhcdn.ru/employer-logo-original/1242487.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4649269',
                          'accredited_it_employer': True, 'trusted': True},
             'snippet': {'requirement': 'Основы машинного обучения и методов анализа данных. Основы стандартного стека: '
                                        '<highlighttext>python</highlighttext> + sklearn, pandas, numpy, '
                                        'scipy, matplotlib и т.д. ',
                         'responsibility': 'О проекте: Департамент анализа данных и моделирования создан в 2019 году '
                                           'для стратегического развития функции анализа данных в ВТБ. '},
             'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'},
             'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
             'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'},
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

    list_vacancies = [Vacancy(name=f'Python developer (Junior)', salary={'from': 50000, 'to': 50000, 'currency': 'RUR', 'gross': True}, snippet='Знание основных концепций <highlighttext>Python</highlighttext>. Опыт написания сервисов на Flask и FastAPI (коммерческий или учебный). Опыт работы с базами данных (коммерческий...', area=f'Владивосток', url=f'https://hh.ru/vacancy/101219641'), \
                      Vacancy(name=f'Data Scientist (Senior)', salary='Зарплата не указана', snippet='Основы машинного обучения и методов анализа данных. Основы стандартного стека: <highlighttext>python</highlighttext> + sklearn, pandas, numpy, scipy, matplotlib и т.д. ', area=f'Москва', url=f'https://hh.ru/vacancy/99030444'),
                      Vacancy(name=f'Стажер IT направления', salary={'from': 70000, 'to': None, 'currency': 'RUR', 'gross': False}, snippet='Знаешь SQL или PostgreSQL. Готов учиться новому. Мы хотели бы видеть интересующегося и трудолюбивого сотрудника, разделяющего ценности команды и одинаково...', area=f'Москва', url=f'https://hh.ru/vacancy/101287743')]
    # print(get_list_vacancies(data))
    sort_by_salary(list_vacancies)
    l_t = top_list_vacancies(list_vacancies, 3)
    for l in l_t:
        print(l)
    # for i in data:
    #     print(i['snippet']['requirement'])
