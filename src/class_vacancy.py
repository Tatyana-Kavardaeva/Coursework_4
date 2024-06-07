

class Vacancy:
    """Формирует экземпляры вакансий по указанным параметрам"""
    name: str  # название вакансии
    url: str  # ссылка на вакансию
    salary_min: int  # минимальная зарплата
    salary_max: int  # максимальная зарплата

    def __init__(self, name='', salary=None, snippet=None, area=None, url=None):
        self.name = name
        self.url = url if url else 'не указана'
        self.currency = ''
        self.salary_min = 0
        self.salary_max = 0
        if salary is None or salary == 'Зарплата не указана':
            self.salary = 'Зарплата не указана'
            self.salary_min = 0
            self.salary_max = 0
        elif isinstance(salary, dict):
            self.salary = salary
            self.salary_min = salary['from'] if salary['from'] else 0
            self.salary_max = salary['to'] if salary['to'] else 0
            self.currency = salary['currency'] if salary['currency'] else ''

        if isinstance(snippet, str):
            self.snippet = snippet
        elif isinstance(snippet, dict):
            self.snippet = snippet['requirement']
        elif not snippet:
            self.snippet = "не указаны"

        if isinstance(area, str):
            self.area = area
        elif isinstance(area, dict):
            self.area = area['name']
        elif not area:
            self.area = "не указан"

    def __repr__(self):
        return f"Vacancy(name=f'{self.name}', salary_min={self.salary_min}, salary_max={self.salary_max}, " \
               f"snippet='{self.snippet}', currency=f'{self.currency}', area=f'{self.area}', url=f'{self.url}')"

    def __str__(self):
        if self.salary_min == 0 and self.salary_max == 0:
            return f'Название вакансии: {self.name}\n' \
                   f'Зароботная плата: не указана\n' \
                   f'Требования: {self.snippet}\n'\
                   f'Город: {self.area}\n' \
                   f'Ссылка на вакансию: {self.url}\n'
        elif self.salary_min == 0:
            return f'Название вакансии: {self.name}\n' \
                   f'Зароботная плата: до {self.salary_max} {self.currency}\n' \
                   f'Требования: {self.snippet}\n' \
                   f'Город: {self.area}\n' \
                   f'Ссылка на вакансию: {self.url}\n'
        elif self.salary_max == 0:
            return f'Название вакансии: {self.name}\n' \
                   f'Зароботная плата: от {self.salary_min} {self.currency}\n' \
                   f'Требования: {self.snippet}\n' \
                   f'Город: {self.area}\n' \
                   f'Ссылка на вакансию: {self.url}\n'
        else:
            return f'Название вакансии: {self.name}\n' \
                   f'Зароботная плата: от {self.salary_min} до {self.salary_max} {self.currency}\n' \
                   f'Требования: {self.snippet}\n' \
                   f'Город: {self.area}\n' \
                   f'Ссылка на вакансию: {self.url}\n'

    def __gt__(self, other):
        """Сравнивает вакансии по минимльной зарплате"""
        if self.salary_min == 0 or other.salary_min == 0:
            return "Зарплата не указана"
        elif self.salary_min > other.salary_min:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.salary_min == 0 or other.salary_min == 0:
            return "Зарплата не указана"
        elif self.salary_min == other.salary_min:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.salary_min == 0 or other.salary_min == 0:
            return "Зарплата не указана"
        elif self.salary_min < other.salary_min:
            return True
        else:
            return False


if __name__ == "__main__":
    vacancy1 = Vacancy(name='Тест', salary=None, area='Тест', url='test@test.test')
    vacancy2 = Vacancy(name='Тест2', salary={'from': 70000, 'to': None, 'currency': 'RUR', 'gross': False},
                       area='Тест2', url='test2@test.test')

    print(str(vacancy1))
    print(vacancy1.__eq__(vacancy2))
