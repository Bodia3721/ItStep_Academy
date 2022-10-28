from math import sqrt


def greeting(name: str) -> None:
    """ Функція для виведення на екран привітання"""
    print(f'Hello, {name}!')


def copy_of_string(text: str, num: int) -> None:
    """ Функція клонування заданого рядка задану кількість разів """
    #print(text*num)
    for i in range(num):
        print(text, end = '. ')


def calc_fraction(x: int) -> float:
    """Функція для обичслення заданого дробу: (sqrt(x)+x)/2"""
    return (sqrt(x) + x) / 2


def factorial(n: int) -> int:
    """Функція для обчислення факторуалу натурального числа n! = 1 * 2 * 3 *... *m"""
    f = 1
    for i in range(1, n):
        f *= i



if __name__ == '__main__':

    greeting('Alex')
    greeting('Max')

    copy_of_string('I love coding', 3)

    result = calc_fraction(6) + calc_fraction(13) + calc_fraction(21)
    print(f'\nResult: {round(result, 4)}')

    result_factorial = (2 * factorial(5) + 3 * factorial(8)) / (factorial(6) + factorial(4) )
