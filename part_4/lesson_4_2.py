"""
Задача 2.

Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""

lst_txt = 'a a a b c a a d c d d'.split()
lst_new = []
dict_new = {}
for i in lst_txt:
    if i not in dict_new:
        dict_new[i] = 0
        lst_new.append(i)
    else:
        dict_new[i] += 1
        lst_new.append(f'{i}_{dict_new[i]}')

print(lst_new)
