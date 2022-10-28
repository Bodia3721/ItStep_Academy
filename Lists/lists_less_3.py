"""
x = []

while True:
    a = input('Введите число: ')
    if a == '':
        break
    x.append(int(a))

min_x = x[0]

max_x = x[0]
"""
"""
x = ''
while x != 'wwwwww':
    x += 'www'
    if x == 'ww':
        break

    print(x)
"""
"""
x = ('abc', 'qwerty', 'bbb')

for i in x:
    print(15, 44, 66, sep=' ')
    if i == 'qwerty':
        break

print(x)
"""
"""

x = [123, 4124, 12512, 123, 444]

"""
# x.append('123')
# y = x.pop(0)
# x.remove(4124)
# x.extend([123, 44, 333])

# print(x[1])
"""
print(x[:])
"""
"""
y = print
x = len


y(x('qwerdfhdfhty'))
"""
"""
x = 'бежал заяц за машиной'

x = x.upper()

print(x)
"""
"""x = ['Дима', 'Саша', 'Ника']

name = input('Введите имя: ').lower().capitalize()

if name in x:
    print('Есть в списке!')
else:
    print('Такого нет!')
"""
"""
for i in x:
    if name == i.lower():
        print(True)
        break
else:
    print(False)
"""
"""
x = '124'

print(x.isdigit())
"""
"""
x = input('Введите число: ')
y = input('Введите число: ')

if x.isdigit() and y.isdigit():
    print(int(x) + int(y))
else:
    print('Вы ввели не число!')
    
"""
"""
x = 'dasdaf fsaffaf safsfasf asfasfasf asfasfsf'

y = x.split(' f')

print(''.join(y))

"""
"""
x = 'Илья,привет, Илья!'

print(x.replace('п', 'в').replace('в', 'п'))

"""

''.upper()  # Возвращает строку в верхнем регистре
''.lower()  # Возвращает строку в нижнем регистре

''.capitalize()  # Первый символ в верхнем регистре, остальные в нижнем
''.title()  # Первый символ каждого слова в верхнем регистре, остальные в нижнем

"""
x = 'ABC'

y = 'BIC'.replace('A', 'C')

print(x)
print(y)
"""

''.isalpha()  # Все символы являютья буквами. В любом регистре
''.isdigit()  # Все символы являютья числами
''.isalnum()  # Все символы являються или буквами, или числами

"""x = 'Какой сегодня день! А ты как думаешь?'
l = '!?. '
for i in l:
    x = x.replace(i, '')

print(x.isalpha())
"""
"""
x = 'adffafasf'

has_int = False

for i in x:
    if i.isdigit():
        has_int = True

print(has_int)"""

"""''.replace('1', '222')  # заменяет все первые подстроки на вторые
''.split('.')  # Разрезает строку по указанному символу, и формирует из них список
''.join([])  # склеивает список строк"""
"""x = '123456712 4146124612 41246'

print(x.split('89dfsdhsgh'))"""
"""
print(''.join(['1', '23', '3123']))

name = 'Сергей'
age = 35

print(name + ', вам уже ' + str(age) + ' лет!')

print('{}, вам уже {} лет!'.format(name, age))
print(f'{name}, вам уже {age} лет!')

print('12' in 'fdsf21dasfs')
"""

"""valid = True
print('@' not in x)

if len(x) < 8:
    valid = False

if '@' not in x:
    valid = False

if valid:
    print('почта верная!')
else:
    print('Неверно указана почта!')"""

# lvl-1
# почта не меньше чем 8 симполов
# есть собачка

# lvl-2
# Есть ли в строке 1 собачка?
# Есть ли символы справа и слева от собачки?
# Есть ли в правой части точка?


# 'asdasd@asdas.dasd'

x = input('Введите почту: ')

l = x.split('@')

valid = True

if len(l) == 2:
    if len(l[0]) == 0:
        valid = False
    else:
        l_right = l[1].split('.')
        if len(l_right) == 1:
            valid = False
        else:
            if len(l_right[0]) == 0 or len(l_right[1]) == 0:
                valid = False

'asdasd@dadas.dgds'