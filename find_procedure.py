# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

# Не получается просчитать венрное кол-во файлов на 1 уровне

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
result_list = []


def my_print(lst):
    print('Отсортированный список файлов:')
    for file in lst:
        print(file)
    print('Всего: {0} файлов.'.format(len(lst)))


def get_result_list(some_path, files_lst, st):
    tmp_list = []
    for file in files_lst:
        with open(os.path.join(some_path, file)) as f:
            file_data_list = [word.upper() for word in f.read().split(', ')]  # Список строк файла, которые могут иметь вложенные списки.
            for file_str in file_data_list:
                if st in file_str:
                    tmp_list.append(file)
                    break

    return tmp_list

# def get_result_list(some_path, files_lst, st):
#     tmp_list = []
#     for file in files_lst:
#         with open(os.path.join(some_path, file)) as f:
#             file_data = f.read()
#             if st in file_data:
#                 tmp_list.append(file)
#     return tmp_list


def filtered_list(lst, st):
    """Функция получает список строк и подстроку,
    возвращает новый список, состоящий из элементов
    списка lst,  которые содержат в конце подтроку st.
    """

    return [file for file in lst if file[-len(st):] == st]


def get_path(folder_name):
    """Функция получает на вход название папки и строит до нее путь,
    с условием, что эта папка лежит в той же директории, что
    и запускаемый файл.
    """

    return os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_name)


if __name__ == '__main__':
    migrations_path = get_path(migrations)  # Получим путь до файлов sql
    print('migrations_path:', migrations_path)
    all_files_in_dir = os.listdir(migrations_path)  # Получим список всех файлов в передаваемой директории
    filtered_files_list = filtered_list(all_files_in_dir, '.sql')  # Получим список содержащий только файлы .sql
    while True:
        search_str = input('Введите строку поиска: ').upper()
        print(search_str)
        if search_str == 'QUIT':
            print('Программа завершена.')
            break
        if result_list == []:
            result_list = get_result_list(migrations_path, filtered_files_list,
                                       search_str)  # Получим список имен файлов, которые содержат в себе подстроку search_str
        else:
            result_list = get_result_list(migrations_path, result_list,
                                       search_str)
        my_print(result_list)  # Вывели результат в требуемом формате


