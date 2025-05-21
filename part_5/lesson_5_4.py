"""
Задание 4.

Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

решите через и set comprehension
"""

# вариант 1
lst_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# традиционный итератор с функцией add
# set_obj = set()
# for dict_el in lst_obj:
#     for val in dict_el.values():
#         set_obj.add(val)

set_obj = {val for dict_el in lst_obj for val in dict_el.values()}

print(set_obj)
