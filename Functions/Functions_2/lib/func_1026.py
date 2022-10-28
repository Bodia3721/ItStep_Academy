# 1026
def nsd2(x: int, y: int) -> int:
    """ Функція для обчислення найбільшого спільного дільника двох чисел """
    a = x
    b = y
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nsd3(x: int, y: int, z: int) -> int:
    """ Функція для обчислення найбільшого спільного дільника трьох чисел """
    return nsd2(nsd2(x, y), z)
