def factorial(n: int) -> int:
    """
        Функція для обчислення факторіалу за допомогою рекурсії
        -------------------------------------------------------
        т! = т * (т - 1)!
        -----------------
        5! = 5 * (4 * 3 * 2 * 1) = 5 * 4!
        4! = 4 * 3!
        3! = 3 * 2!
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_demo() -> None:
    for i in range(1, 16):
        x = i
        y = factorial(x)
        print(f'{x}! = {y}')
