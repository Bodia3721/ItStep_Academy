#---------------Домашнее задание--Задание №1-----------------
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
#
# even = 0
# even_num = 0
# odd = 0
# odd_num = 0
# multiples_9 = 0
# multiples_9_num = 0
# sum_of_num = 0
# average = 0
#
# if num1 == 0:
#     even_num = -1
#
# for i in range(num1, num2+1):
#
#     if i % 2 == 0:
#         even += i
#         even_num += 1
#
#     if i % 2 == 1:
#         odd += i
#         odd_num += 1
#
#     if i % 9 == 0:
#         multiples_9 += i
#         multiples_9_num += 1
#
#     sum_of_num += i
#
# print('Sum of even numbers: ', even)
# print('Average of even numbers', even / even_num)
# print('Sum of odd numbers: ', odd)
# print('Average of odd numbers', odd / odd_num)
# print('Sum of multiples of 9: ', multiples_9)
# print('Average of multiples of 9: ', multiples_9 / multiples_9_num)
# print('Average: ', sum_of_num / (num2 - num1 + 1))

#---------------Домашнее задание--Задание №2-----------------

# length = int(input('Enter the length:'))
# symbol = input('Enter the symbol:')
#
# for i in range(length):
#     print(symbol)

#---------------Домашнее задание--Задание №3-----------------
# number = int(input('Enter the number: '))
# test = True
# while test:
#     if number == 7:
#         print('Good bue!')
#         break
#     elif number > 0:
#         print('Number is positive')
#         break
#     elif number == 0:
#         print('Number is equal to zero')
#         break
#     else:
#         print('Number is negative')
#         break

#---------------Домашнее задание--Задание №4-----------------
arr = []
sum_of_num = 0
n = int(input('Enter how many elements you want: '))
for i in range(n):
    x = int(input('Enter the numbers: '))
    arr.append(x)
    if 7 in arr:
        print('Good bue!')
        break
if 7 not in arr:
    for i in arr:
        sum_of_num += i

    min_num = min(arr)
    max_num = max(arr)

    print('Sum of numbers: ', sum_of_num)
    print('Minimum value', min_num)
    print('Maximum value', max_num)




