"""
num = input('Введите число: ')

if num == "1":
    print('понедельник')
elif num == "2":
    print('Вторник')
else:
    print('Неверное значение')
"""
"""
str()
int()
bool()
list()
"""
"""
x = [1, 2, 3, [], 5]

x[3].append('abc')
x.append('qwerty')
x[3].append([])
x[3][1].append('iii')
print(x)
"""
"""
x = [[[['abc']]]]

print(x[0][0][0][0][0])
"""
"""
s = 'qwerty'

print(s[3])
"""
"""
x = [[[['abc']]]]

print(x[0][0][0][0])"""
"""
x = [4, 5, 6, True, False]

x.append(True)
x.remove(5)
x.pop(0)

x.insert(1, 'abc')
y = x.index(True)
x.reverse()
c = x.count(523)
x.extend([1,3,5])

print(x)
print(c)


for i in x:
    print(i*2)
"""
"""
print(len([1, 2, 6, 2, 7, 3]))


"""
"""
x = [1, 6, 3, 6, -5]

num_max = x[0]
num_min = x[0]
s = 0
c = 0
for i in x:
    if i > num_max:
        num_max = i
    if i < num_min:
        num_min = i
    s += i
    c += 1
print(num_max)
print(s)
print(c)
"""
"""
x = [1, 2, 3, 4, 5, 6, 7, 8, 'asf']

print(x[:8])
"""
"""
x = 'qwerty'

print(x[1:4])
"""
"""
x = (1, 2, 3, 5, 6, 7, 8, 4)

print(x[3:8])

print(x)

print(tuple('4536789yug'))
"""
"""
x = (1, (2, 5))

print(type(x))
print(x)"""
'''
print(x[1][1])
'''

'''

1)У нас есть тумбочка, в котором мы храним свою одежду.
Футболки в 1 ящике
Штаны во 2
Кофты в 3
Добавить через append по 2 вещи в каждую тумбу, затем вывести кофты и футболки 

'''
'''
items = [[], [], []]
items[0].extend(['berhka', 'adidas'])
items[1].extend(['nike', 'levis'])

items[2].append('штаны-1')
items[2].append('штаны-2')

print(items[0]+items[2])
'''

'''

2)Написать программу, которая будет запрашивать имя и возраст клиента,
после чего заносить их в список, до тех пор пока не будет введено "всё"
В конце вывести данные в виде "Коля, возраст - 20"

Все данные хранить в 1 переменной.

*После того как вы заполнили список, нужно будет ввести имя, и вывести возраст 
этого человека
'''
"""x = ['Коля', 20]

print(x[0] + ', возраст - ' + str(x[1]))
print(f'{x[0]}, возраст - {x[1]}')

"""
"""
users = []

while True:
    name = input('Введите имя: ')
    if name == 'всё':
        break
    age = int(input('Введите возраст: '))

    users.append((name, age))
"""
who = input('Введите имя пользователя: ')
users = [['Дима', 22], ['Маша', 23]]
find = False

for i in users:
    if i[0] == who:
        print(i[1])
        find = True
        break

if not find:
    print('Юзер не найден')

"""
y = []
y.extend([5, 6])

print(y)
"""

"""x = {12, 15, 55, True, 15}

x.add(345)
x.add(345)
x.add(2)
x.add(345)

for i in x:
    print(i)"""
"""
x = [6, 1, 2, 4, 5, 6, 3, 4, 1]
print(sorted(x))
"""

"""
x1 = {1, 2, 3}
x2 = {2, 3, 4, 5}

print(x2.difference(x1))
"""
"""
x = [1,2,4,21,3,4,1,2,4,5]

x = list(set(x))

print(x)

"""
"""
x = {}

print(type(x))
"""
"""
x = {'1', 1+4, 5}

for i in x:
    print(i)
"""
