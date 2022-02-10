"""
x = 532
x2 = '482372'
x3 = 124124.9
x4 = False
x5 = None


y = 20 != 20

print(y == x4)
"""

'''
not - инвертирует значение

'''
"""
banana = True
apple = False
kiwi = False
print(banana or apple and kiwi)
"""
"""
x = 10

if x > 100:
    print(1)
elif x > 40:
    print(2)
elif x > 35:
    print(3)

if x > 20:
    print(4)
else:
    print(5)
"""

"""
x1 = int(input('Введите число 1: '))
x2 = int(input('Введите число 2: '))
znak = input('Введите "-" или "+": ')
"""

"""
if x2 == 0:
    print('Нельзя делить на ноль!')
else:
    print(x1 / x2)
"""
"""
x = 'dima sasha nika'
name = 'dim'
if name in x:
    print('Вы есть в списке!')
else:
    print('нет')
"""
"""
x1 = int(input('x1: '))
x2 = int(input('x2: '))
y = input('+ or -: ')

if y == '+':
    print(x1+x2)
elif y == '-':
    print(x1-x2)
elif y == '/':
    if x2 != 0:
        print(x1/x2)
    else:
        print('Нельзя делить на ноль.')
else:
    print('Некорректное действие!')

"""
"""
banana = True
apple = False

x = input('Что хочет Саша?: ')

if x == 'банан':
    if banana:
        print('Саша съел банан!')
    else:
        print('Банана нет, Саша остально голодным :( ')
elif x == 'яблоко':
    if apple:
        print('Саша съел яблоко!')
    else:
        print('Яблока нет, Саша остально голодным :( ')
else:
    print('Саше такого еще нельзя!')"""

"""
если есть или банан или яблоко - у вас есть один фрукт
если есть банан и яблоко - у вас есть два фрукта
если ничено нет - ничено нет
"""
"""
banana = False
apple = False

if banana and apple:
    print('у вас есть два фрукта')
elif banana or apple:
    print('у вас есть один фрукт')
else:
    print('ничего нет')
"""
'''
У нас есть логин и пароль для входа в админ панель сайта.
1) Запросить логин
2) Запросить пароль.
3) Если данные верны - вывести "вход разрешен", если нет - "неверный логин или пароль
!использовать 1 if
'''
"""login = 'admin'
password = 'qwerty'

l = input('Введите логин: ')
p = input('Введите пароль: ')

if l == login and p == password:
    print('Вход в личный кабинет')
else:
    print('Неверный логин или пароль')
"""
'''
У Миши есть 1000грн
Ему нужно зайти в 2 магазина - купить штаны и кофту.
После чего, миша должен будет зайти в магазин купить пельменей за 80грн на ужин
Введите стоимость кофты и штанов, и узнайте будет ли миша сегодня голодным.
'''
"""
money = 1000
cost = input('Введите стоимость кофты: ')

if int(cost) > money:
    print("У вас не хватит денег на эту кофту!")
else:
    money = money - int(cost)
    print('Вы успешно купили кофту!')

cost = input('Введите стоимость штанов: ')

if int(cost) > money:
    print("У вас не хватит денег на эти штаны!")
else:
    money = money - int(cost)
    print('Вы успешно купили штаны!')

if money < 80:
    print('Миша модник остался голодным')
else:
    money = money - 80
    print('Миша поел')
"""

x = 100
x += 25
print(x)