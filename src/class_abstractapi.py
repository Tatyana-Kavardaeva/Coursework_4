from abc import ABC, abstractmethod


class AbstractAPI(ABC):

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_vacancies(self, keyword):
        pass
