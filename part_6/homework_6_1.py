"""
Задание 1
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 4
Введите второе число: 4
1.0

Введите первое число: 4
Введите второе число: 0
Пытаетесь делить на 0!

Введите первое число: 4
Введите второе число: g
Пожалуйста, вводите только числа
"""


def division_a_b(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError as exc:
        return exc, 'Пытаетесь делить на 0!', a, b
    except ValueError as exc:
        return exc, 'Пожалуйста, вводите только числа', a, b


a, b = input('Введите первое число: '), input('Введите второе число: ')

print(division_a_b(a, b))
