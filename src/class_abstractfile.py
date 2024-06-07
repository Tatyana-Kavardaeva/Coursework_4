from abc import ABC, abstractmethod


class AbstractFile(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, name):
        pass
