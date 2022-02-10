#---------------Домашнее задание--Задание №1-----------------
# x = int(input('Enter the num: '))
#
# for i in range(1, x+1):
#     print('*' * i)

#---------------Домашнее задание--Задание №2-----------------
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
s = 0
for i in range(num1, num2+1):
    if i % 5 == 0 and i % 2 != 0:
        s += i
print(s)
