import time

#---------------Домашнее задание--Задание №1-----------------
# guests = []
# guests_count = 0
# while True:
#     x = input('Введите имя гостя: ')
#     if x == 'всё':
#         break
#     guests.append(x)
#     guests_count +=1
#
#
# print(' '.join(guests))
# print('Количество гостей: ', guests_count)

#---------------Домашнее задание--Задание №2-----------------

# x = input('Введите строку: ')
# list_of_symbols = []
# count_of_symbols = 0
# count_of_unique_symbols = 0
#
#
# for i in x:
#     list_of_symbols.append(i)
#     count_of_symbols += 1
#
# unique_symbols = set(list_of_symbols)
# for i in unique_symbols:
#     count_of_unique_symbols += 1
#
# print('Количество символов: ', count_of_symbols )
# print('Количество уникальных символов: ', count_of_unique_symbols)

#---------------Домашнее задание--Задание №3-----------------
# list = ['a','b','a','c','g','d','g','e','f','g','i','v']
# unique_list = set(list)
# print(unique_list)
# new_list = []
#
# for i in unique_list:
#     new_list.append(i)
#     new_list.sort()
# print(new_list)

#---------------Домашнее задание--Задание №4-----------------
# list = ['Ратушный','Высоцкая','Иванова','Щепетков','Климчук']
# set_list = set(list)
# copy_list = list
# print(list)
#
# while True:
#     x = input('Введите имя: ')
#     if x in set_list:
#         set_list.remove(x)
#         print('Проверка...')
#         time.sleep(1)
#         print('Входите!')
#     else:
#         print('Проверка...')
#         time.sleep(0.5)
#         if x not in set_list and x in copy_list:
#             print('Вы не можете войти. Гость с такой фамилией уже есть!')
#         elif x not in set_list:
#             print('Вас нет в списке!')
#             break














