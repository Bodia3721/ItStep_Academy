"""
x = int(input('Введите число: '))

n_min = x
n_max = x
s = x

while True:
    x = int(input('Введите число: '))
    if x == 7:
        break
    if x < n_min:
        n_min = x
    if x > n_max:
        n_max = x
    s += x

"""
"""
l = []

while True:
    x = int(input('Введите число: '))
    if x == 7:
        break
    l.append(x)

print(l)
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
"""

"""
x = int(input('Введите число: '))
for i in range(x):
    print('*' * (i+1))

"""

"""
x = "range(5, 10)"

print(list(x))
"""
"""
x = []

x.append(10)

print(x)

x.append('123')

print(x)

x.append('qwe')
x.append(None)

print(x)"""

"""
y = 'Ника'
x = ['Дима', 'Саша', 'Игорь', 'Нина', 'Ира', y, 'y']

while True:
    name = input('Введите имя: ')

    if name in x:
        print(name, '     есть в списке')
    else:
        print('Такого в списке нет')
"""

"""
x = 15

y = [x, 70, True, None, False, 5.123]

"""

'''
1) В цикле добавляем имена гостей, которых вы пригласили на вечеринку.
Восле ввода строки "всё" вы выходите из списка

2) Затем в цикле снова запрашиваем имя гостя, и проверяем есть ли он в списке
приглашенных.
'''

"""
guests = []

while True:
    name = input('Введите имя гостя: ')
    if name == 'всё':
        break
    guests.append(name)

print('Вечеринка началась!')


while True:
    name = input('Введите имя гостя: ')
    if name in guests:
        print('Вход разрешен')
        guests.remove(name)
    else:
        print('Вход запрещен')
    if len(guests) == 0:
        print('Все гости пришли!')
        break
"""

"""
x = [123, 'qwerty', True, True, 0, [2]]

input('123: ')

x.pop(0)

print(x)

"""
"""
x = [1, 2, 3]

x.pop(0)

print(x)
"""
"""
x = [123, 'qwerty', True, True, 0, [2]]

for i in range(len(x)):
    x.pop(0)

x = []

print(x)
"""

"""
Написать программу, которая запрашивает название покупки, и её цену.
Название сохраняет в список, а цену добавляет к общей сумме.
Для выхода из цикла ввести "всё"

В конце выводит список всех покупок и их сумму.

"""

"""
list_of_items = []
full_sum = 0

while True:
    name = input('Введите название: ')
    if name == '':
        break
    cost = int(input('Стоимость товара: '))
    list_of_items.append(name)
    full_sum += cost

print(full_sum)"""


"""x = ''
for i in list_of_items:
    x += i + '\n'

print(x)"""


"""
x = ['Кроссовки', 'футболка', 'Шорты']

y = '?-'.join(x)
"""