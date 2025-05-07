"""
Задание 1.

По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""

number = int(input('Дай целое неотрицательное число: '))
factorial = number

while number > 1:
    factorial = factorial * (number - 1)
    number -= 1
print(factorial)

