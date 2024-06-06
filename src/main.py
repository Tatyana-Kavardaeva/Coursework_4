from src.class_headhunterapi import HeadHunterAPI
from src.utils import get_list_vacancies, sort_by_salary, top_list_vacancies
from src.class_jsonfile import JsonFile
import os


def user_interaction():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, "vacancies.json")
    # Создаем экземпляр классса HeadHunterAPI
    url_1 = "https://api.hh.ru/vacancies"
    hh_api = HeadHunterAPI(url_1)

    while True:
        # Получаем ключевое слово от пользователя для парсинга вакансий c hh.ru
        user_keyword = input("Введите поисковый запрос: ")
        # Парсим вакансии по запросу пользователя и формируем список экземпляров класса вакансии
        list_vacancies = get_list_vacancies(hh_api.get_vacancies(user_keyword))
        # Записываем список вакансий в файл vacancies.json
        js_file = JsonFile(file_path)
        js_file.write_vacancies(list_vacancies)
        # Получаем дополнительную информацию от пользователя
        user_filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
        # Фильтруем список вакансий по ключевым словам
        filter_list = js_file.get_vacancies_by_criteria(user_filter_words.split(', '))
        if len(filter_list) == 0:
            print("Вакансии не найдены")
            user_input = input("Хотите продолжить поиск? (да/нет)").lower()
            if user_input == "нет":
                print("Поиск завершен")
                break
            elif user_input == "да":
                print()
                continue
            else:
                print("Ваш ответ не найден, начните поиск вакансий заново")
                continue
        else:
            print(f"По вашему запросу найдено {len(filter_list)} вакансий")
            # Запрашиваем у пользователя количество вакансий для вывода в топ-лист по зарплате
            user_n = input("Введите количество вакансий для вывода в топ N по заработной плате: ")
            print()
            # Сортируем вакансии по зарплате
            sort_list = sort_by_salary(filter_list)
            # Формируем топ-лист
            top_list = top_list_vacancies(sort_list, user_n)
            if top_list == "Невозможно осуществить выборку. Количество вакансий должно быть числом":
                print(top_list)
            else:
                vacancies_strings = [str(vacancy) for vacancy in top_list]
                top_list = '\n'.join(vacancies_strings)
                print(top_list)

        print("Поиск вакансий завершен")
        break


if __name__ == "__main__":
    user_interaction()
