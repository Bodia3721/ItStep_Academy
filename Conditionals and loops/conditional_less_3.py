"""x = 24

y = 10
while True:
    print(x)
    print('abc')
    print(123)
    if x == 25:
        break
    x += 1
print('Конец цикла')"""
"""
while 10 > 5:
    n1 = int(input('1 число: '))
    n2 = int(input('2 число: '))
    if n2 == 0:
        print('На ноль делить нельзя!')
        break
        continue

    print(n1/n2)
"""
"""
x = 10

while x < 15:
    x += 1
    print(x)
else:
    print('Цикл закончился')
"""
"""
while True:
    x += 1
    print(x)
    if not x < 15:
        break
else:
    print('Цикл закончился')

"""

'''
1) Сделать программу, в которой нужно угадать имя.
Программа будет спрашивать его, до тех пор пока ей не дадут правильный ответ
Если угадал имя, то на экран выводиться "Вы угадали!"

1.1) Усложнить игру, на угадывание есть всего 10 попыток. "Вы не угадали :("
'''
"""
while True:
    x = input('Введите имя: ')
    if x == 'Ира':
        print('Вы угадали')
        break
"""
"""
x = input('Введите имя: ')
while x != 'Ира':
    x = input('Введите имя снова: ')
print("Вы угадали")
"""
"""
c = 0
while True:
    name = input('Введите имя: ')
    c += 1
    if name == 'Дима':
        print('Вы угадали!')
        break
    elif c == 10:
        print('Попытки закончились')
        break

"""

"""
x = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

chet = 0
not_chet = 0
dev_9 = 0
s = 0
c = 0
while x <= end:
    if x % 2 == 0:
        chet += x
    else:
        not_chet += x

    if x % 9 == 0:
        dev_9 += x

    s += x
    c += 1

    x += 1

print('Сумма четных: ', chet)
print('Сумма нечетных: ', not_chet)
print('Сумма кратных 9: ', dev_9)
print('Среднее: ', s / c)

"""
"""
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

chet = 0
not_chet = 0
dev_9 = 0
s = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        chet += i
    
    if i % 2 == 1:
        not_chet += i

    if i % 9 == 0:
        dev_9 += i

    s += i

print('Сумма четных: ', chet)
print('Сумма нечетных: ', not_chet)
print('Сумма кратных 9: ', dev_9)
print('Среднее: ', s / (end - start + 1))
"""
"""
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

chet = 0
not_chet = 0
dev_9 = 0
s = 0

while True:
    for i in range(start, end + 1):
        if i % 2 == 0:
            chet += i

        if i % 2 == 1:
            not_chet += i
        if i % 9 == 0:
            dev_9 += i
        s += i

    ex = input('Для повтора введите "да": ')
    if ex != 'да':
        break
    start = int(input('Введите начало диапазона: '))
    end = int(input('Введите конец диапазона: '))

print('Сумма четных: ', chet)
print('Сумма нечетных: ', not_chet)
print('Сумма кратных 9: ', dev_9)
print('Среднее: ', s / (end - start + 1))

"""


