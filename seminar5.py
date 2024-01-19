#  Рекурсия
# Ряд Фиббоначчи

# def fib(num):
#     if num in (0,1):
#         return num
#     return fib(num-1) + fib(num-2)

# print(fib(8))



# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – 
# на минимальные. Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

# lst = input("input string").split()
# print(lst)

# def change_journal(lst):
#     maximum = 0
#     minimum = float('inf')
#     for i in lst:
#         if maximum < int(i):
#             maximum = int(i)
#         if minimum > int(i):
#             minimum = int(i)
#     print("max", maximum, "min", minimum)

#     for i in range(len(lst)):
#         if lst[i] == maximum:
#              lst[i]=minimum
#     return lst



# journal = [-1, 3, 1616516165, 3, 4]


# print(change_journal(journal))



#     return lst



# change_journal(lst)

# # Решение в класее

# def change_journal(lst):
#     maximum=0
#     minimum=float('inf')
#     for i in lst:
#         if maximum<i:
#             maximum=i
#         if minimum>i:
#             minimum=i
#     print("max",maximum,"min",minimum)
#     for i in range(len(lst)):
#         if lst[i] == maximum:
#             lst[i]=minimum
#     return lst



# journal = [-1, 3, 1616516165, 3, 4]


# print(change_journal(journal))


#Задача 3
# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым Напоминание: Простое число - это число, 
# которое имеет 2 делителя: 1  и n(само число) Input: 5 Output: yes

# def simple_number(number):
#     for i in range(2, number):
#         if not number % i:
#             return False
#     return True

# print(simple_number(int(input("enter number"))))


# решение в классе
# def is_prime(number: int) -> bool:
#     if number <= 3:
#         return True
#     if not number % 2:
#         return False
#     for i in range(3, int(number**0.5), 2):
#         if not number % i:
#             return False
#     return True


# print(is_prime(17))


# Задача 4

# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и
# использовать циклы (даже для ввода и вывода). Input:    2 -> 3 4 Output: 4 3

# number = 5

# def reverseSort(quantity):
#     if quantity == 0:
#         return ''
#     n = input("Enter your number: ")
#     return reverseSort(quantity - 1) + n + ' '

# print(reverseSort(number))


# Homework


# Возведение в степень

# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

# def expo(a: int, b: int):
#     if b == 0 or a == 1:
#         return 1
#     return a*expo(a, b-1)

# print(expo(3,4))


# Рекурсивная сумма

# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:


# sum(2, 2)
# # 4

def sum(a: int, b: int):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)
    

print(sum(3,15))

    