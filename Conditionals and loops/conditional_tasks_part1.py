# x = int(input('Введите первое число: '))
# y = int(input('Введите второе число: '))
#
# num_lists = []
#
# print('Все числа: ')
# for i in range(x, y+1):
#     num_lists.append(i)
#     print(i, end=',')
#
# print('\nНечетные числа: ')
# for i in num_lists:
#     if i % 2 != 0:
#         print(i, end=',')
#
# print('\nЧетные числа: ')
# for i in num_lists:
#     if i % 2 ==0:
#         print(i, end=',')
#
# print('\nВсе числа в порядке убывания: ')
# for i in num_lists[::-1]:
#     print(i, end=',')

#-----Задача 5------
x = int(input('Введите первое число: '))
a = 0
y = int(input('Введите второе число: '))
b = 0

if x > y:
    a = y
    b = x
else:
    a = x
    b = y

print('Нечетные числа: ')
for i in range(a, b+1):
    if i % 2 != 0:
        print(i)



