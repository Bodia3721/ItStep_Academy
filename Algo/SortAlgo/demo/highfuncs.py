import functools
from math import sqrt
from random import randint


if __name__ == '__main__':

    # Анонімні функції:
    func1 = lambda x1, y1, x2, y2: sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    distance = func1(2, 5, 3, 11)
    print(f'distance = {distance:.2f}')

    # MAP:
    # ====================================
    # Функція відображення map - example1:
    data1 = ['10', '20', '30', '40', '50']
    print(data1)
    data2 = list(map(lambda x: int(x), data1))
    print(data2)

    # Функція відображення map - example2:
    numbers = list(range(10, 31))
    print(numbers)
    squares = list(map(lambda x: x ** 2, numbers))
    print(squares)

    # Функція відображення map - example3:
    persons = ['yAnG', 'MASk', 'thoMas', 'LIsa']
    print(persons)
    correct = list(map(str.capitalize, persons))
    print(correct)

    # Функція відображення map - example4:
    arr1 = [10, 20, 30]
    arr2 = [40, 50, 60]
    arr3 = list(map(lambda x, y: x + y, arr1, arr2))
    print(arr1)
    print(arr2)
    print(arr3)

    # FILTER:
    # ====================================
    # Функція фільтрації - example1:
    data = [randint(10, 99) for i in range(20)]
    print(data)
    result = list(filter(lambda x: x > 50, data))
    print(result)

    # Функція фільтрації - example2:
    integers = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]
    positive = list(filter(lambda x: x >= 0, integers))
    negative = list(filter(lambda x: x < 0, integers))
    print(integers)
    print(positive)
    print(negative)

    # Функція фільтрації - example3:
    prices = [randint(100, 999) for i in range(30)]
    select = list(filter(lambda x: 400 < x < 600, prices))
    print(prices)
    print(select)

    # REDUCE:
    # ====================================
    # Агрегуюча функція - example1:
    collection1 = [100, 200, 300, 400, 500]
    s = functools.reduce(lambda x, y: x + y, collection1)
    print(f's = {s}')

    # Агрегуюча функція - example2:
    collection2 = [randint(100, 999) for i in range(10)]
    min_element = functools.reduce(lambda x, y: x if x < y else y, collection2)
    print(collection2)
    print(f'm = {min_element}')

    # ZIP:
    # ====================================
    # Об'єднуюча функція - example1:
    array1 = [10, 20, 30]
    array2 = [40, 50, 60]
    array3 = [70, 80, 90]
    union = list(zip(array1,array2, array3))
    print(f'union = {union}')