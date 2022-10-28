def power_of_number(a: float, n: int) -> float:
    if n == 0:
        return 1
    return a * power_of_number(a, n-1)