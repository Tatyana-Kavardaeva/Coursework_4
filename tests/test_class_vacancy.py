import pytest


def test_vacancy_init(vacancy1):
    assert vacancy1.name == 'Тест'
    assert vacancy1.salary == 'Зарплата не указана'
    assert vacancy1.snippet == 'Тест'
    assert vacancy1.area == 'Тест'
    assert vacancy1.url == 'test@test.test'
    assert vacancy1.salary_min == 0
    assert vacancy1.salary_max == 0
    assert vacancy1.currency == ''


def test_vacancy_salary(vacancy2, vacancy3, vacancy4):
    assert vacancy2.salary == {'from': 70000, 'to': None, 'currency': 'RUR', 'gross': False}
    assert vacancy2.salary_min == 70000
    assert vacancy2.salary_max == 0
    assert vacancy2.currency == 'RUR'

    assert vacancy3.salary == {'from': None, 'to': 110000, 'currency': 'RUR', 'gross': True}
    assert vacancy3.salary_min == 0
    assert vacancy3.salary_max == 110000
    assert vacancy3.currency == 'RUR'

    assert vacancy4.salary == {'from': 50000, 'to': 50000, 'currency': 'RUR', 'gross': True}
    assert vacancy4.salary_min == 50000
    assert vacancy4.salary_max == 50000
    assert vacancy4.currency == 'RUR'


def test_vacancy_str(vacancy1, vacancy2, vacancy3, vacancy4):
    assert str(vacancy1) == f'Название вакансии: Тест\n' \
                            f'Зароботная плата: не указана\n' \
                            f'Требования: Тест\n' \
                            f'Город: Тест\n' \
                            f'Ссылка на вакансию: test@test.test\n'

    assert str(vacancy2) == f'Название вакансии: Тест2\n' \
                            f'Зароботная плата: от 70000 RUR\n' \
                            f'Требования: Тест2\n'\
                            f'Город: Тест2\n' \
                            f'Ссылка на вакансию: test2@test.test\n'

    assert str(vacancy3) == f'Название вакансии: Тест3\n' \
                            f'Зароботная плата: до 110000 RUR\n' \
                            f'Требования: Тест3\n'\
                            f'Город: Тест3\n' \
                            f'Ссылка на вакансию: test3@test.test\n'

    assert str(vacancy4) == f'Название вакансии: Тест4\n' \
                            f'Зароботная плата: от 50000 до 50000 RUR\n' \
                            f'Требования: Тест4\n'\
                            f'Город: Тест4\n' \
                            f'Ссылка на вакансию: test4@test.test\n'


def test_vacancy_eq(vacancy1, vacancy2, vacancy3, vacancy4):
    assert vacancy1.__eq__(vacancy2) == "Зарплата не указана"
    assert vacancy2.__eq__(vacancy4) is False


def test_vacancy_lt(vacancy1, vacancy2, vacancy3, vacancy4):
    assert vacancy1.__lt__(vacancy2) == "Зарплата не указана"
    assert vacancy2.__lt__(vacancy4) is False


def test_vacancy_gt(vacancy1, vacancy2, vacancy3, vacancy4):
    assert vacancy1.__gt__(vacancy2) == "Зарплата не указана"
    assert vacancy2.__gt__(vacancy4) is True
