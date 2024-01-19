# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у 
# вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом 
# функции должен быть кортеж, содержащий длины полуосей 
# эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения. Подсказка: проще всего 
# будет найти эллипс в два шага: сначала вычислить самую 
# большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площадь. Гарантируется, что самая далекая 
# планета ровно одна

# from random import randint

# from math import pi


# planets = [(randint(1,5), randint(1,5)) for _ in range(10)]
# print(planets)

# planets = set(filter((lambda x: x[0] != x[1]), planets))

# print(max(planets, key = lambda x: x[0]*x[1]))


# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.

# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristics, values):
#     return len(set(map(characteristics, values))) < 2

# a = list('12345678')

# print(same_by(lambda x: x.isdigit(), a))


# print_operation_table

# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

# Пример

# На входе:


# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:


# 1 2 3
# 2 4 6 
# 3 6 9




# def print_operation_table(operation, num_rows=9, num_columns=9):
#     if num_rows > 1 and num_columns > 1:
#         for i in range(num_columns):
#             if i < num_columns -1:
#                 print(i + 1, end=' ')
#             else:
#                 print(i + 1, end='\n')

#         for i in range(1, num_rows):
#             print(i + 1, end=' ')
#             for j in range(1, num_columns):
#                 if j < num_columns-1:
#                     print(operation(i + 1 , j + 1 ), end=' ')
#                 else:
#                     print(operation(i + 1 , j + 1 ), end='\n')
#     else:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
# print_operation_table(lambda x, y: x-y, 2, 2)


# def print_operation_table(operation, num_rows=9, num_columns=9):
#     if num_rows > 1 and num_columns > 1:
#         # for i in range(num_columns):
#         #     if i < num_columns -1:
#         #         print(i + 1, end=' ')
#         #     else:
#         #         print(i + 1, end='\n')

#         for i in range(num_rows):
#             # print(i + 1, end=' ')
#             for j in range(num_columns):
#                 if j < num_columns-1:
#                     print(operation(i + 1 , j + 1 ), end=' ')
#                 else:
#                     print(operation(i + 1 , j + 1 ), end='\n')
#     else:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
# print_operation_table(lambda x, y: x*y, 3, 3)


# Винни Пух

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

# Пример
# На входе:
# 
# На выходе:
# Парам пам-пам

def count_syllables(word):  
    vowels = 'ауоыиэёйя'
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count


def WinniethePooh(stroka) -> str:
    phrases = stroka.split(' ')
    # print(phrases)
    if len(phrases) <= 1:
        return 'Количество фраз должно быть больше одной!'
    syllables = [] 
    for phrase in phrases:
        syllables.append(count_syllables(phrase))
        # print(syllables)
    if len(set(syllables)) != 1:
        return 'Пам парам'
    return 'Парам пам-пам'




# stroka = 'по-русски говорят'
stroka = 'со-лнце-гре-ет ве-сной'
print(WinniethePooh(stroka))