"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. Решите используя sys.argv и argparse
"""

from argparse import ArgumentParser


def calculate_salary(output, hourly_rate, award):
    return int(args.output) * int(args.hourly_rate) + int(args.award) * (int(args.output) * int(args.hourly_rate)) / 100


parser = ArgumentParser(description="Принимаем строку с параметрами")

parser.add_argument("-output", type=int, default=20)
parser.add_argument("-hourly_rate", type=int, default=500)
parser.add_argument("-award", type=int, default=10)

args = parser.parse_args()

print(f'Выработка в часах: {args.output}')
print(f'Ставка в час: , {args.hourly_rate}')
print(f'Премия: , {args.award}')
print(calculate_salary(args.output, args.hourly_rate, args.award))
