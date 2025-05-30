"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. Решите используя sys.argv и argparse
"""

from argparse import ArgumentParser

parser = ArgumentParser(description="Принимаем строку с параметрами")

parser.add_argument("-output", type=int, default=20)
parser.add_argument("-hourly_rate", type=int, default=500)
parser.add_argument("-award", type=int, default=10)

args = parser.parse_args()
salary = int(args.output) * int(args.hourly_rate) + int(args.award) * (int(args.output) * int(args.hourly_rate)) / 100

print("выработка в часах:", args.output)
print("ставка в час:", args.hourly_rate)
print("премия:", args.award)
print(salary)
