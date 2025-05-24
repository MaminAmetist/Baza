"""
Задание 2
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример: Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def about_person(**kwargs):
    name, year_of_birth, city, email, phone = (kwargs['name'], kwargs['year_of_birth'], kwargs['city'],
                                               kwargs['email'], kwargs['phone'])
    return f'{name} {year_of_birth} года рождения, проживает в городе {city}, email: {email}, телефон: {phone}'


ivan = {'name': 'Иван Иванов',
        'year_of_birth': '1846',
        'city': 'Москва',
        'email': 'jackie@gmail.com',
        'phone': '01005321456'}

print(about_person(**ivan))
