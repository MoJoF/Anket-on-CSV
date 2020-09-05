# Микробиблиотека для записи данных в файл Excel
# Разработано Ecclezio

import csv

# Метод, переводит двумерный массив в одномерный для удобства занесения данных
# в .csv файл.
# Первый аргумент list1 принимает двумерный массив
# Второй аргумент list2 принимает пустой массив

def from_arr_2x_to_arr_1x(list1, list2):
    for i in list1:
        list2.append(','.join(i))

# Метод записывает данные в csv файл.
# Первый аргумент list принимает в себя одномерный массив который получается
# при вызове функции from_arr_2x_to_arr_1x.
# Второй аргумент принимает строку с название файла и расширение
# Пример: 'result.csv'

def write_file(list, title):
    with open(title, 'w', newline='',) as f:
        writer = csv.writer(f, delimiter=',')
        for row in list:
            writer.writerow(row.split(','))
