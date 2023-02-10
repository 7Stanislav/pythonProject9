"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroError(Exception):
    def __init__(self, text):
        self.text = text


def div():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            raise ZeroError("Делить на ноль нельзя!")
        else:
            res = num_1 / num_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except ZeroError as err:
        return err

print(div())
