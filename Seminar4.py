# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()


# string_1 = "a a a b c a a d c d d"
# list_1 = string_1.split()

# count = {}

# for char in list_1:
#     if char in count:
#             print(f"{char}_{count[char]}", end = " ")
#             count[char] += 1

#     else: 
#         count[char] = 1
#         print(f"{char}", end = " ")

# print(count)

# alternative solution

# data = input("Enter your list: ").split()
# dict_counter = {}

# for char in data:
     
# print(f'{char}_{dict_counter.get(char)}', end = " " if char in dict_counter else print(char, end = "")
# dict_counter[char] = dict_counter.get(char, 0) + 1

    

# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# from string import punctuation 

# print(punctuation)

# punctuation = punctuation.replace("'", '')

# input_string = "She sells sea shells on the sea shore. The shells that she sells are sea shells. I'm sure. So if she sells sea shells on the sea shore. I'm sure that the shells are sea shore shells"


# for ch in punctuation:
#     input_string = input_string.replace(ch, " ")


# list_1 = input_string.lower().split()
# print(list_1)
# print(set(list_1))
# print(len(set(list_1)))



# Задача 29 проверить на работоспособность код

# 1 Ваня

# n = int(input())
# max_number = -1
# while n != 0:
#     if max_number < n:
#         max_number = n
#     n = int(input())
# print(max_number)


# Петя:
n = int(input())
max_number = -1
while n > 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number, end = " ") 



# Homework
# Задача 1

# Пересечение двух неупорядоченных наборов целых чисел

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# Пример

# На входе:


# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:
# 3 5

# list_1 = var2.split()

# set_1 = set(var2.split())
# set_2 = set(var3.split())

# z = set_1.intersection(set_2)

# print(" ".join(sorted(z)))


#Homework Задача 2


# Черника

# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет 
# урожайность, которая соответствует количеству ягод на этом кусте.

# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий 
# модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.

# Пример использования На входе:


# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе:


# 19
# current_count = [0]*len(arr)
# n= len(arr)
# for i in range(n):
#     current_count[i] = arr[i] + arr[(i+1)%n] + arr[(i+2)%n]
# print(max(current_count))


# import random

# bushes = [random.randint(1,15) for _ in range(10)]

# print(bushes)

# max_berries = 0
# for i in range(len(bushes)):
#     total = bushes[i-2] + bushes[i-1] + bushes[i]
#     if total > max_berries:
#         max_berries = total

# print(max_berries)