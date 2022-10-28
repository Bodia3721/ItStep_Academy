#---------------Домашнее задание--Задание №1-----------------
# x = input('Введите строку: ')
# print(x[::-1])

#---------------Домашнее задание--Задание №2-----------------
# x = input('Введите строку: ')
# count_num = 0
# count_lett = 0
#
# for i in x:
#     if i.isdigit():
#         count_num += 1
#     elif i.isalpha():
#         count_lett +=1
# print('Количество цифр: ', count_num)
# print('Количество букв: ', count_lett)

#---------------Домашнее задание--Задание №3-----------------
# x = input('Введите строку: ')
# y = input('Введите символ: ')
# count_symbol = 0
#
# for i in x:
#     if i == y:
#         count_symbol +=1
# print(f'В строке {count_symbol} символов')

#---------------Домашнее задание--Задание №4-----------------
# x = input('Введите строку: ')
# text_list = set(x.split())
# word = input('Введите слово для поиска: ')
# count_word = 0
#
# for i in text_list:
#     if word in text_list:
#         count_word += 1
# print('Количество слова в строке: ', count_word)

#---------------Домашнее задание--Задание №5-----------------
x = input('Введите строку: ')
word = input('Введите слово для поиска: ')
change = input('Введите слово для замены: ')

print(x.replace(word, change))


