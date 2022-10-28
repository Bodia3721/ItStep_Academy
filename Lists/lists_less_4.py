"""
print('Привет'[::-1])


x = list(x)
print(x)

print(''.join(x[::-1]))


print(x)
"""
"""
x = 'xfyguhilbvgdytuiyhkvju'

for i in x:
    print(i)

"""
"""
x = 'aFSAsafasFSAfFSAFSAFSAFSASFA'

print(x.upper())
print(x.lower())

print(len(x.split('FSA')) - 1)
"""
"""
x = '214--421--fasfsaf--12424'

print(' -0_0- '.join(x.split('--')))

"""
"""
x = ['123', 'fff', '2d2']
s = '+++'

print(s.join(x))
"""
"""
x = 'fff123dsafafffsfffff'

print(x.rstrip('fsa'))
"""

"""
input('4124')
"""
'Если указано число, то вывести квадрат из *'
'Если введен символ, то сообщить об ошибке'

'''
*****
*****
*****
*****
*****
'''
'''
Вариант 2: вывести пустой квадрат:
*****
*   *
*   *
*   *
*****
'''
"""
x = input('Введите ширину квадрата: ')

if x.isdigit():
    for _ in range(int(x)):
        print('*' * int(x))
else:
    print('Вы ввели не число!!!')
"""
# x = input('Введите ширину квадрата: ')
#
# if x.isdigit():
#     print('*' * int(x))
#     for _ in range(int(x) - 2):
#         spaces = ' ' * (int(x) - 2)
#         print(f'*{spaces}*')
#     print('*' * int(x))

"""
print(int('100101000110', 2))
"""
"""
x = 'Олег'
y = 20

z = f'Здравствуйте {x}, вам сейчас {y} лет!'

"""

"""
s = {1, 23, 4, 6, 7, 4, 2}
print(1 in s)
"""
"""
x = [1, 23, 4, 6, 7, 4, 2]

del x[3]

print(x)
"""
"""
x = frozenset([1, 4, 6, 12, 5, 1, 2])
"""
"""x = 0
y = 0
try:
    print(15 / x)
    try:
        print(10/y)
    except:
        print('Ошибка внутри!')
    print('Что-то важное')
    print('Что-то важное')
    print(15 / x)
    print('Что-то важное')
    print('Что-то важное')
    print('Что-то важное')
    print('Что-то важное')
except:
    print('Возникла ошибка')
    print('Возникла ошибка')
    print('Возникла ошибка')
    print('Возникла ошибка')
    print('Возникла ошибка')


print('Программа выполняется дальше')

"""
"""
x = '0'

try:
    print(200 / int(x))
except ValueError:
    print('Вы ввели не число!')
except ZeroDivisionError:
    print('Делить на ноль нельзя!')
"""
"""x = 0
if x < 10:
    ''
elif x > 20:
    pass
else:
    print(123)
"""

'''
1) Запросить через input индекс элемента.
2) Попробуйте достать элемент по введенному индексу
3) В случае возникновения ошибок, обработайте их, и выведите сообщение на экран
'''
"""while True:
    try:
        y = int(input('Введите индекс: '))
        print(x[y])
    except ValueError:
        print('Вы ввели не число')
    except IndexError:
        print('Вы за пределами индексов списка')
"""
"""
x = [1, 4, 12, 4, 1, 2]

y = int(input('Введите индекс'))

class MyException(Exception):
    pass

if y >= len(x):
    raise MyException('Неверный индекс')

"""
