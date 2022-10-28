from math import sqrt

#614

def check_triangle(a: float, b: float, c: float) -> bool:
    """Функція для перевірки існування трикутника"""
    if a + b > c or a + c > b or c + b > a:
        print(True)
    else:
        print(False)


#616

def calc(x: float, y: float, operation: str) -> float:
    """Функція проведення математичних дій над двома числами"""
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    else:
        print('Unknown operation!')


#Златопольский 10.1 (b)

def calc_fraction(x: int, y: int) ->float:
    """ Функція для обчислення заданного дробу: (x + sqrt(x)) / ((sqrt(y) + y)) """
    return (x + sqrt(x)) / (sqrt(y) + y)


#Златопольский 10.21

def is_palindrom(x: int) -> bool:
    """Функція визначення чи є число паліндромом"""
    if str(x) == str(x)[::-1]:
        print(True)
    else:
        print(False)
