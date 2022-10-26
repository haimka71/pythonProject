# Задача №1: Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# number = int(input("Введите число: "))
# d = {i : 3*i + 1 for i in range(1,number+1)}
# print(f"Итоговая последовательность: {d}")

##################################################################################

# Задача №2: Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# import random
# def write_file(number):
#     with open('file333.txt', 'w+') as data:
#         for i in range(number):
#             data.write(f"{random.randrange(0, 2*number)}\n")
#
# def read_file():
#     with open('file333.txt', 'r') as data:
#         indexes = list(map(int,data.readlines()))
#     return indexes
#
# # оптимизация
#
# n = int(input("Введите число N: "))
# lst_number = [i for i in range(-n, n+1)]
# write_file(n)
# lst_index = read_file()
# result = 1
# for i in range(len(lst_index)):
#     result *= lst_number[lst_index[i]]
# print(f"Результат равен = {result}")


#############################################################################
# Задача №3: Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
# number = int(input("Введите число: "))
# lst = []
# for i in range(number):
#     lst.append((-3)**i)
# print(f"Итоговая последовательность: {lst}")
# print(f"Итоговая последовательность: {lst}")
#
# # улучшение
#
# lst = [(-3)**i for i in range(number)]
# print(f"Итоговая последовательность после применения list comprehension: {lst}")
