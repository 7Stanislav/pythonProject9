"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class ErrNumber(ValueError):
    pass

my_list = []
while True:
    try:
        value = input('Введите число или "q" для выхода:')
        if value == 'q':
            break
        if not value.isdigit():
            raise ErrNumber(value)
        my_list.append(int(value))
    except ErrNumber as no_num:
        print(no_num, 'не является числом')
print(my_list)
