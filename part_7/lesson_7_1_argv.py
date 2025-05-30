"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. Решите используя sys.argv и argparse
"""
# python lesson_7_1_argv.py 10 500 10

from sys import argv


def calculate_salary(output, hourly_rate, award):
    return int(output) * int(hourly_rate) + int(award) * (int(output) * int(hourly_rate)) / 100


script_name, output, hourly_rate, award = argv

print(f'Выработка в часах: {output}')
print(f'Ставка в час: , {hourly_rate}')
print(f'Премия: , {award}')
print(calculate_salary(output, hourly_rate, award))
