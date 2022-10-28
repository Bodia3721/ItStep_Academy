# 657

def my_pow(a: float, n: int) -> float:
    """Функція для піднесення дійсного числа до заданого степеня"""
    res = 1
    if n >= 0:
        for i in range(n):
            res *= a
    else:
        for i in range(-n):
            res /= a
    return res