# Задача1

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива


import random

len1 = int(input("Enter the length of the first list: "))
len2 = int(input("Enter the length of the second list: "))

lst1 = [random.randint(0, 5) for _ in range(len1)]

lst2 = ([random.randint(0, 5) for _ in range(len2)])
print(lst2)
lst2 = set(lst2)

print(lst2)

print(lst1)

for elem in lst1:
    if elem not in lst2:
        print(elem, end=" ")


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# import random
# len1 = int(input("Enter the length of the first list: "))
# lst = [random.randint(0, 5) for _ in range(len1)]
# count = 0
# for i in range(1, len1-1):
#     if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
#         count+=1
# print(lst)
# print(count)

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# import random

# lst = [random.randint(0,10)for _ in range(int(input('Введите размер: ')))]
# print(lst)
# print(set(lst))

# count = 0
# for item in set(lst):
#     count += lst.count(item)//2
# print(count)


    # Два различных натуральных числа n и m называются
    # дружественными, если сумма делителей числа n
    # (включая 1, но исключая само n) равна числу m и
    # наоборот. Например, 220 и 284 – дружественные числа.

# def sum_dividers(number: int):
#     dividers = set()
#     dividers.add(1)
#     for i in range(2, int(number ** 0.5) + 1):
#         if not number % i:
#             dividers.add(i)
#             dividers.add(number // i)

#     return sum(dividers)


# def find_friendly(max_number: int):
#     for i in range(1, max_number + 1):
#         var = sum_dividers(i)
#         if var <= max_number:
#             if sum_dividers(var) == i:
#                 if i < var:
#                     print(i, var)


# find_friendly(9_999_999)

# # variant 2

# def sum_of_divisors(num: int) -> int:
#     summ = {1}
#     for div in range(2, int(num ** 0.5) + 1):
#         if not num % div:
#             summ.add(div)
#             summ.add(num // div)
#     return sum(summ)

# friendly_dict = {i: sum_of_divisors(i) for i in range(1, 1000000)}

# for number, summ in friendly_dict.items():
#     if number == friendly_dict.get(summ) and number < summ:
#         print(number, summ)



# ДЗ


# Элементы из заданного диапазона

# Инструкция по использованию платформы



# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

# Пример

# На входе:


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# for i in range(0, len(list_1)):
#     if list_1[i] >= min_number and list_1[i] <= max_number:
#         print(i)


# Арифметическая прогрессия

# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , 
# разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример

# На входе:


# a1 = 2
# d = 3
# n = 10


# list_1 = [None]*n
# list_1[0] = a1
# for i in range(1, len(list_1)+1):
#  list_1[i-1] = a1 + (i-1) * d
#  print(list_1[i-1])

# print(list_1)