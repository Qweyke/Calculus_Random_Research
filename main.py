"""Исследование Random-функции, создать большой массив псевдослучайных чисел,
узнать сколько раз повторяются первые 5 чисел в таком же порядке (псевдопериод),
посчитать мат.ожидание, дисперсию.
Сформировать Случайную величину с наперед заданными значениями и их вероятностями (задание дискретной СВ)"""

import random


"""Нахождение кол-ва повторений 5 первых элементов в массиве, при помощи срезов"""
def find_occurrences(rand_arr, first_bunch):
    a, b = 0, 5
    count = 0
    while b <= len(rand_arr):
        next_five = rand_arr[a:b]
        if next_five == first_bunch:
            count += 1
        a += 1
        b += 1
    return count


def math_expectation(rand_arr, n):  # математическое ожидание
    #  Сумма всех элементов СВ, деленная на их кол-во
    return sum(rand_arr) / n


def math_dispersion(rand_arr, n): # математическая дисперсия
    #  Сумма квадратов разности значений элементов и мат. ожидания
    expec = math_expectation(rand_arr, n)
    sum = 0
    for digit in rand_arr:
        sum += (digit - expec)**2
    return sum / n


a, b = 0, 9
n = 100000
random_arr = [random.randint(a, b) for i in range(n)]
first_five = random_arr[:5]
print("Первые 5 цифр:", first_five)

print("Частота появления первых 5 чисел:", find_occurrences(random_arr, first_five))
print("Математическое ожидание = ", math_expectation(random_arr, n))

math_disp = math_dispersion(random_arr, n)
print("Математическая дисперсия = ", math_disp)
print("Стандартное отклонение = ", math_disp ** (-1/2))

digit_arr = [0, 1, 2, 3, 4]  # задаем массив чисел
probability = [0.1, 0.2, 0.3, 0.25, 0.15]  # задаем массив вероятностей для этих чисел
dispers_random = random.choices(digit_arr, probability, k=n)  # распределяем

print("Математическое ожидание для дискретного массива = ", math_expectation(dispers_random, n))

math_disp = math_dispersion(dispers_random, n)
print("Математическая дисперсия для дискретного = ", math_disp)
print("Стандартное отклонение для дискретного = ", math_disp ** (-1/2))

