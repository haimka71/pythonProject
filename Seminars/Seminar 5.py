# Задача №1:
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные: 'ываабвавб лепотабв это абвцукен абвабвгкруто ываы круто'
from pydoc import text

import txt as txt


# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')

######### с использованием filter (просто для сравнения)

# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# lst = list(filter(lambda x: 'абв' not in x, txt.split(' ')))
# print(f'Результат: {" ".join(lst)}')

####################################################################################

# Задача №2:
# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте, как наделить бота "интеллектом"


############### вариант человек против человека:
#
# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # очередность хода
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

##################### вариант человек против бота c "интеллектом" - как вариант "интеллекта"
# - бот берет произвольное количество конфет:

# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
#
# def bot_calc(value):
#     k = randint(1,29)
#     while value-k <= 28 and value > 29:
#         k = randint(1,29)
#     return k
#
# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # очередность хода
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

##########################################################################

# Задача #3.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

#################
# Проба с объяснением, просто  для себя разобраться...

# Кодирование длин серий (RLE) в Python – это очень простая форма сжатия данных,
# в которой поток данных предоставляется в качестве входных данных (например, «AAABBCCCC»),
# а выходными данными является последовательность отсчетов последовательных значений данных в строке
# (например, « 3A2B4C «).
# Источник: https://tonais.ru/osnovy/kodirovanie-dlin-seriy-rle-python



def coding(txt):  # функция кодирования
    count = 1
    res = ''
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt) - 2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):     # функция декодирования вариант 1
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res



# def decoding(txt):  # функция декодирования вариант 2
#  number= ''
#  res = ''
#  for i in range(len(txt)):
#         if not txt[i].isalpha(): # The isalpha() method returns True if all the characters are alphabet letters (a-z)
#             number += txt[i]
#         else:
#             res += (txt[i] * int(number))
#             # res.append(txt[i] * int(number))
#             number = ''
#             # number += i
#  return ''.join(res)



# def decoding(file):           # функция декодирования вариант 3 (семинар)
#   txt = open(file).read()
#   lenth = 0
#   wt_txt = ''
#   while lenth < len(txt):
#      amount = ''
#      key = ''
#      while txt[lenth].isdigit():
#        amount += txt[lenth]
#        lenth +=1
#        key += txt[lenth]
#        wt_txt += int(amount)*key
#        lenth +=1
#   with open('file111.txt','w+') as rd:
#        text.write(f'{wt_txt}')

# decoding('file111.txt')


s = input("Введите текст для кодировки (без пробелов и разделителей): ")  # с вводом вручную
# s= open('file.txt').read()                                                  #  чтение из file.txt
print(f"Текст до кодировки: {s}")

print(f"Текст после кодировки: {coding(s)}")
with open('file111.txt', 'w+') as rd:                                       # записали в file111.txt
    rd.write(coding(s))

# print(f'Текст после декодировки: {decoding(coding(s))}')

sum = open('file111.txt').read()
print(f'Текст после дешифровки: {decoding(sum)}')
with open('file 222.txt', 'w+') as rd:                             # записали результат дешифровки в file222.txt
    rd.write(decoding(sum))









# print(f"Текст после дешифровки: {decoding(coding(s))}")
# with open('file111.txt','r') as rd:
#  s1=list(map(int,rd.read().split(' ')))
# print(f"Текст после дешифровки: {decoding(coding(s1))}")
# print(f"Текст после кодировки: {coding(s)}")









# def decode(txt):
#  result=[]
#  for item in txt:
#     result.append(item[0]*item[1])
#     return " ".join(result)

# with open('file111.txt','r') as rd:
#  sum=list(map(str,rd.read().split(' ')))
#  # sum = open('file111.txt').read()
# print(f"Текст после дешифровки: {decoding(sum)}")

############# Вариант с char, надо разбираться
# def rle_encode(data): encoding = '' prev_char = '' count = 1
# if not data: return '' for char in data:
# #	If the prev and current characters
# #	don't match...
# if char != prev_char:
# #	... then add the count and character
# #	to our encoding if prev_char:
# encoding += str(count) + prev_char count = 1 prev_char = char
# else:
# #	Or increment our counter
# #	if the characters do match
# 	count += 1
# else:
# 	# Finish off the encoding
# 	encoding += str(count) + prev_char ret encoding
######################