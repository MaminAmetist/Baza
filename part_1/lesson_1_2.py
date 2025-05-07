"""В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.

Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32"""


# count_a = int(input('Введи число учеников класса А: '))
# count_b = int(input('Введи число учеников класса Б: '))
# count_c = int(input('Введи число учеников класса В: '))
# desk_a = count_a // 2 if count_a % 2 == 0 else (count_a // 2 + 1)
# desk_b = count_b // 2 if count_b % 2 == 0 else (count_b // 2 + 1)
# desk_c = count_c // 2 if count_c % 2 == 0 else (count_c // 2 + 1)
# res = desk_a + desk_b + desk_b
# print(res)

# count_desk = 0
# count_student = []
# for i in range(0, 3):
#     count_student.append(int(input(f'Введи число учеников класса {i + 1}: ')))
# for j in count_student:
#     count_desk += j // 2 if j % 2 == 0 else (j // 2 + 1)
# print(count_desk)

A, B, C = 20, 21, 22
print(f'Нужно купить {A // 2 + A % 2 + B // 2 + B % 2 + C // 2 + C % 2} парты')
